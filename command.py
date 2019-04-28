# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 00:34:37 2018

@author: Tasos
"""

from argparse import ArgumentParser
from alchemist.laboratory import Laboratory
import yaml


def process():

    parser = ArgumentParser(description="Calculation of shelves' final state")
#
    parser.add_argument('--reactions', '-r', action="store_true")
    parser.add_argument('laboratory')

    arguments = parser.parse_args()
   
    with open(arguments.laboratory, "r") as data:
        shelves = yaml.load(data)
    #the above code takes a yaml input from the console and it loads its data into the dictionary 'shelves'

    ######################Testing code#####################################################################
    testing_shelf_number = list(shelves.keys())
    if not (len(testing_shelf_number) == 2):
        raise TypeError('\nNumber of shelves must be exactly 2')

    #######################################################################################################

    lab = Laboratory(shelves["lower"], shelves["upper"])
    if arguments.reactions:
        print("\n")
        print(lab.run_full_experiment())

    else:
        lab.run_full_experiment()
        final_dict = {"upper": lab.upper,
                      "lower": lab.lower}
        print("\n", yaml.safe_dump(final_dict, default_flow_style=False))


if __name__ == "__main__":
    process()