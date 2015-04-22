import asyncio
import logging
import sys
from aiodocker import Docker
from aiodocker.util import get_config_from_env
from cliff.app import App
from cliff.commandmanager import CommandManager


class DockerApp(App):

    log = logging.getLogger(__name__)

    def __init__(self, loop=None):
        super().__init__(description='aiodocker',
                         version='0.1',
                         command_manager=CommandManager('aiodocker.command'))
        self.loop = loop or asyncio.get_event_loop()

    def initialize_app(self, argv):
        opts = {
            'host': self.options.host,
            'cert_path': self.options.cert_path,
            'tls_verify': self.options.tls_verify
        }
        self.log.debug('initialize with %s' % opts)
        self.client = Docker(**opts)

    def async(self, future):
        self.loop.run_until_complete(future)
        pending = asyncio.Task.all_tasks()
        if pending:
            self.loop.run_until_complete(asyncio.wait(pending))

    def build_option_parser(self, *args, **kwargs):
        parser = super().build_option_parser(*args, **kwargs)
        parser.set_defaults(**get_config_from_env())

        group = parser.add_argument_group('Api configuration')
        group.add_argument('--host',
                           help='define host. can be in the form of '
                                'tcp://127.0.0.1:8000 or unix:///my.socket')
        group.add_argument('--cert-path', help='path to the cert files')
        group = group.add_mutually_exclusive_group()
        group.add_argument('--tls-verify',
                           action='store_true',
                           dest='tls_verify',
                           help='use tls')
        group.add_argument('--no-tls-verify',
                           action='store_false',
                           dest='tls_verify',
                           help='do not use tls')
        return parser


def main(argv=sys.argv[1:]):
    app = DockerApp()
    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
