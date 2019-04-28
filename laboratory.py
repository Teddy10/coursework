# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:18:46 2018

@author: Tasos
"""

import random


class Laboratory(object):

    def __init__(self, lower, upper):

        for up in upper:
            up_list = up.split("anti")
            if len(up_list) > 2:
                raise ValueError("\nNo such substance beginning with antianti as %s in upper shelf", up)

        for low in lower:
            low_list = low.split("anti")
            if len(low_list) > 2:
                raise ValueError(("\nNo such substance beginning with antianti as %s in lower shelf", low))

        self.lower = lower
        self.upper = upper

    def can_react(self, substance_lower, substance_upper):
        return (substance_lower == "anti" + substance_upper) or (substance_upper == "anti" + substance_lower)

    def update_shelves(self, substance_lower, substance_upper_index):
        lower = self.lower
        index1 = lower.index(substance_lower)

        self.lower = self.lower[:index1] + self.lower[index1+1:]
        self.upper = self.upper[:substance_upper_index] + self.upper[substance_upper_index+1:]

    def do_a_reaction(self):
        for substance_lower in self.lower:
            possible_targets = [i for i, target in enumerate(self.upper) if self.can_react(substance_lower, target)]
            if not possible_targets:
                continue
            else:
                substance_upper_index = random.choice(possible_targets)
                self.update_shelves(substance_lower, substance_upper_index)
                return substance_upper_index

    def run_full_experiment(self):
        count = 0
        ended = False

        while not ended:
            lower = self.lower
            upper = self.upper

            self.do_a_reaction()

            if self.lower != lower:
                count += 1

            ended = (self.lower == lower) and (self.upper == upper)

        return count
