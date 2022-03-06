# from auturing.constants import RESOURCES_DIR
# import os
# import pandas as pd

import warnings
import logging
import numpy as np

def dicttape_to_list(dicttape):
    logging.debug('[DEBUG] dicttape_to_dict - Lengtht dicttape = {}'.format(len(dicttape)))
    maxvalue = max(dicttape.keys())
    logging.debug(f'[DEBUG] dicttape_to_dict - maxvalue = {maxvalue}')

    minvalue = min(dicttape.keys())
    logging.debug(f'[DEBUG] dicttape_to_dict - minvalue = {minvalue}')

    return [int(dicttape[x]) for x in range(minvalue,maxvalue+1)]

class TuringAutomata:
    def __init__(self,
                 transition_table,
                 tape,
                 begin_state="e1",
                 head_position=0,
                 return_begin = 0,
                 return_end = "end",
                 max_steps=0):

        logging.debug(f"""[DEBUG] TuringAutomata, received 
                      tape = {tape}
                      begin_state = {begin_state}
                      head_position = {head_position}
                      return_begin = {return_begin}
                      return_end = {return_end}""")

        # The tape is implemented as a dict
        # Trying to access to an unset value ? It will considered as 0
        # The trick is just that, at the end of the program, the dict will be converted to a list of the appropriate length
        # using "dicttape_to_list"
        self.tape = {x:int(tape[x]) for x in range(len(tape))}

        self.return_begin = return_begin
        self.return_end = return_end
        self.steps = 0
        if max_steps:
            logging.debug('[DEBUG] There is a max step : {}'.format(max_steps))
            self.max_steps = max_steps
        else:
            logging.debug('[DEBUG] No max step. Setting to np.inf')
            self.max_steps = np.inf

        self.tt = transition_table # The programmation itself
        # tt stands for 'transition table'

        self.current_state = begin_state
        self.head_position = head_position

    def compute(self):
        tt = self.tt # short alias

        while(True):
            self.steps +=1

            try:
                tape_value = self.tape[self.head_position]
            except KeyError:
                tape_value = 0

            logging.debug('[DEBUG] \n\n\t***** STEP {} *****\n'.format(self.steps))

            logging.debug('[DEBUG] Stepname = {}'.format(self.current_state))
            logging.debug('[DEBUG] Tape = {}'.format(dicttape_to_list(self.tape)))
            logging.debug('[DEBUG] Position in tape = {}'.format(self.head_position))
            logging.debug('[DEBUG] Tape_value = {}'.format(tape_value))


            newline = tt[(tt["old_state"] == self.current_state) & (tt["tape_read"] == tape_value)]


            logging.debug("[DEBUG] Code = \n{}".format(newline))

            assert len(newline) == 1
            newline = dict(newline.iloc[0])

            if str(int(newline["tape_write"])):
                logging.debug('[DEBUG] Writing = {}'.format(int(newline["tape_write"])))
                self.tape[self.head_position] = int(newline["tape_write"])

            if str(newline["move_tape"] == "r"):
                self.head_position += int(newline["move_tape"])

                if int(newline["move_tape"] >= 0):
                    logging.debug('[DEBUG] Moving head = +{}'.format(newline["move_tape"]))
                else:
                    logging.debug('[DEBUG] Moving head = {}'.format(newline["move_tape"]))

            if newline["return"] == True or self.steps >= self.max_steps:
                if self.return_end == "end":
                    self.return_end = max(self.tape.keys())
                tape_tolist = dicttape_to_list(self.tape)
                logging.debug('[DEBUG] Reached the end with steps = {}'.format(self.steps))

                if self.steps >= self.max_steps:
                    logging.debug('[DEBUG] Max step reached')

                return tape_tolist[self.return_begin:self.return_end]

            self.current_state = newline["new_state"]
            logging.debug('[DEBUG] Next step will be : {}'.format(self.current_state))

