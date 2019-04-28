# -*- coding: utf-8 -*-
"""
Created on Sun Dec  18 18:10:32 2018

@author: Tasos
"""
import yaml
from alchemist.laboratory import Laboratory


def test_randomness():

    with open("alchemist/tests/fixture.yml", 'r') as shelvesIn:
        fixt_loaded = yaml.load(shelvesIn)


    fixt_lab1 = Laboratory(fixt_loaded["lower"], fixt_loaded["upper"])
    fixt_lab2 = Laboratory(fixt_loaded["lower"], fixt_loaded["upper"])
    fixt_lab3 = Laboratory(fixt_loaded["lower"], fixt_loaded["upper"])
    fixt_lab4 = Laboratory(fixt_loaded["lower"], fixt_loaded["upper"])

    randomness = True

    if fixt_lab1.upper == fixt_lab2.upper and fixt_lab1.upper == fixt_lab3.upper:
        randomness = (fixt_lab1.upper == fixt_lab4.upper)

    assert randomness


def test_can_react():
    with open("alchemist/tests/fixture.yml", 'r') as shelvesIn:
        fixt_loaded = yaml.load(shelvesIn)
        fixt_lab = Laboratory(fixt_loaded["lower"], fixt_loaded["upper"])

    creact = fixt_lab.can_react('alcea', 'antialcea')
    assert creact


def test_update_shelves():
    with open("alchemist/tests/fixture.yml", 'r') as shelvesIn:
        fixt_loaded = yaml.load(shelvesIn)
        fixt_lab = Laboratory(fixt_loaded["lower"], fixt_loaded["upper"])

    new_upper = fixt_lab.upper[1:]
    new_lower = fixt_lab.lower[1:]
    fixt_lab.update_shelves('antialcea', 0)

    update = (new_upper == fixt_lab.upper and new_lower == fixt_lab.lower)

    assert update


def test_do_a_reaction():

    with open("alchemist/tests/fixture.yml", 'r') as shelvesIn:
        fixt_loaded = yaml.load(shelvesIn)
        fixt_lab = Laboratory(fixt_loaded["lower"], fixt_loaded["upper"])

    new_upper1 = fixt_lab.upper[1:]
    new_upper2 = fixt_lab.upper[:3]
    new_lower = fixt_lab.lower[1:]
    fixt_lab.do_a_reaction()

    d_reaction = False
    if new_upper1 == fixt_lab.upper or new_upper2 == fixt_lab.upper:
        d_reaction = (new_lower == fixt_lab.lower)

    assert d_reaction


def test_run_full_experiment():

    with open("alchemist/tests/fixture.yml", 'r') as shelvesIn:
        fixt_loaded = yaml.load(shelvesIn)
        fixt_lab = Laboratory(fixt_loaded["lower"], fixt_loaded["upper"])

    full = False
    count = fixt_lab.run_full_experiment()
    full = (count == 1)

    assert full


def test_antianti_upper():
    print("\n'test_antianti_upper' is a negative test")
    upper = ["antiantialcea", "firma"]
    lower = ["antifirma", 'psittaccina']
    check = Laboratory(lower, upper)


def test_antianti_lower():
    print("\n'test_antianti_lower' is a negative test")
    upper = ["antifirma", 'psittaccina']
    lower = ["antiantialcea", "firma"]
    check = Laboratory(lower, upper)

