# This file is part of hARPy
# Released under the MIT license
# Copyright (c) Serhat Çelik

"""Module for handling command-line arguments."""

import argparse
from harpy.data import variables as core
from harpy.__version__ import __version__
from harpy.__author__ import __author__, __email__, __gitlink__
from harpy.handlers.argument_handler import ArgumentHandler
from harpy.handlers.interface_handler import InterfaceHandler


class ParserHandler:
    """Handler of command-line arguments."""

    @staticmethod
    def create_arguments():
        """Create new command-line arguments."""

        parser = argparse.ArgumentParser(
            prog='harpy', epilog='Use at your own risk!',
            description=f'By {__author__} <{__email__}> ( {__gitlink__} )'
        )

        parser.add_argument(
            '-a', '--author', action='version', version=parser.description,
            help='show program author information and exit'
        )
        parser.add_argument(
            '-c', default=core.DEF_CNT, type=int, metavar='count', dest='c',
            help='number of times to send each request (def|min: '
                 '%%(default)s|%d)' % core.MIN_CNT
        )
        parser.add_argument(
            '-f', '--filter', action='store_true', dest='f',
            help='filter sniff results using the given scanning range'
        )
        parser.add_argument(
            '-i', default=InterfaceHandler()(), metavar='interface', dest='i',
            help='network device to send/sniff packets'
        )
        parser.add_argument(
            '-l', '--log', action='version', version=core.DEV_LOG,
            help='show where log files are stored and exit'
        )
        parser.add_argument(
            '-n', default=core.DEF_NOD, type=int, metavar='node', dest='n',
            help='last ip octet to be used to send packets (def|min|max: '
                 '%%(default)s|%d|%d)' % (core.MIN_NOD, core.MAX_NOD)
        )
        parser.add_argument(
            '-p', '--passive', action='store_true', dest='p',
            help='enable passive mode, do not send any packets'
        )
        parser.add_argument(
            '-r', metavar='range', dest='r',
            help='scanning range, e.g. 192.168.1.1/24 (valid: /8, /16, /24)'
        )
        parser.add_argument(
            '-s', default=core.DEF_SLP, type=int, metavar='sleep', dest='s',
            help='time to sleep between each request in ms (def|min|max: '
                 '%%(default)s|%d|%d)' % (core.MIN_SLP, core.MAX_SLP)
        )
        parser.add_argument(
            '-t', default=core.DEF_TIM, type=int, metavar='timeout', dest='t',
            help='timeout to stop scanning in sec (def|min: '
                 '%%(default)s|%d)' % core.MIN_TIM
        )
        parser.add_argument(
            '-v', '--version', action='version', version='v' + __version__,
            help='show program version and exit'
        )

        return parser

    @staticmethod
    def check_arguments():
        """Check the command-line arguments."""

        return [
            ArgumentHandler.count_handler(core.COMMANDS.c),
            ArgumentHandler.interface_handler(core.COMMANDS.i),
            ArgumentHandler.node_handler(core.COMMANDS.n),
            ArgumentHandler.range_handler(core.COMMANDS.r),
            ArgumentHandler.sleep_handler(core.COMMANDS.s),
            ArgumentHandler.timeout_handler(core.COMMANDS.t),
            not (not core.COMMANDS.r and core.COMMANDS.f),
            not (not core.COMMANDS.r and not core.COMMANDS.p),
        ]
