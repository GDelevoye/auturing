import os
from auturing.constants import PROGRAMS
from auturing.turing_automata import TuringAutomata
import pandas as pd


def runit(loglevel, progress_bar,resources,args):

    program_path = os.path.join(PROGRAMS,args["program_name"])
    transition_table = pd.read_csv(program_path,
                                   sep="\t",
                                   skiprows=[0],
                                   header=[0]).fillna(0)

    machine = TuringAutomata(transition_table=transition_table,
                             tape=args["tape"],
                             begin_state=args["begin_state"],
                             head_position=args["head_position"],
                             return_begin=args["return_begin"],
                             return_end=args["return_end"],
                             max_steps=args["max_steps"])

    print(machine.compute())

    return
