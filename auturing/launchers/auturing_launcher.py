#!/usr/bin/env python

import auturing
import argparse
import os
import sys
import logging

import numpy as np

def main():

    LAUNCHER_DIR = os.path.join(os.path.dirname(__file__))
    PYCKAGE_RESOURCES_DIR = os.path.join(os.path.abspath(os.path.join(LAUNCHER_DIR,os.pardir)),"resources")

    parser = argparse.ArgumentParser()

    parser.add_argument('program_name',
                        type=str)

    parser.add_argument('--tape',"-t",
                            help='Input tape (comma-separated values) <DEFAULT:0>',
                            default="0")

    parser.add_argument('--begin_state',"-b",
                            help='Begin state of the program <DEFAULT: "e1">',
                            default="e1")

    parser.add_argument('--head_position',
                            help='Head position on the tape at start <DEFAULT:0>',
                            type=int,
                            default=0)

    parser.add_argument('--return_begin',
                            help='Indice starting from which the tape should be returned <DEFAULT: 0>',
                            type=int,
                            default=0)

    parser.add_argument('--return_end',
                            help='Indice until which the tape should be returned <DEFAULT: end>',
                            default=None)

    parser.add_argument('--max_steps',
                            help='Indice until which the tape should be returned <DEFAULT: 0 (ignored)>',
                            default=0,
                            type=int)

    parser.add_argument('--verbosity',"-v",
                            help='Choose your verbosity. Default: INFO',
                            required=False,
                            default="CRITICAL",
                            choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    parser.add_argument('--progress_bar',"-p",
                            help='Displays a progress bar',
                            action='store_true')


    args = parser.parse_args()

    if args.max_steps == 0:
        args.max_steps = np.inf
    assert args.max_steps > 0


    verboselevel = "logging."+str(args.verbosity)
    logging.basicConfig(level=eval(verboselevel),
                        format='%(asctime)s %(message)s',
                        stream=sys.stdout)

    show_progress_bar = False
    if args.progress_bar:
        show_progress_bar = True

    args = vars(args)

    args["tape"] = [int(x.strip()) for x in args["tape"].split(',')]
    assert len(args["tape"]) >= 0
    logging.debug('[DEBUG] Received tape {}'.format(args["tape"]))


    auturing.run_automata.runit(loglevel = verboselevel, progress_bar = show_progress_bar, resources = PYCKAGE_RESOURCES_DIR, args=args)

if __name__ == "__main__":
    main()
