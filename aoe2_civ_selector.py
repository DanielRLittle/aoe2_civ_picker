#!python

import random
# import argparse
import logging
import sys

# Takes all_civs.txt and sorts alphabetically
def organise_all_civs(no_pick=[], add_pick=[]):
    all_civs = read_civs()
    all_civs.sort()
    new_civs = ""
    for civ in all_civs:
        print(civ)
        new_civs = new_civs + civ
    amend_civs = open("all_civs.txt", "w")
    amend_civs.write(new_civs)
    amend_civs.close()
    return

def read_civs(file_name="all_civs.txt"):
    file = open(file_name, "r")
    all_civs = file.readlines()
    file.close()
    return all_civs


def civ_selector(no_pick=[], add_pick=[]):
    added_options = no_pick + add_pick
    all_civs = read_civs()
    not_civs = [civ for civ in added_options if civ not in all_civs]

    if len(not_civs) > 0:
        for civ in not_civs:
            logging.error(f"'{civ}' is not an available civ. Either add it to 'all_civs.txt' or choose another civ")
        sys.exit(1)

    banned_civs = read_civs(file_name="banned_civs.txt")
    if len(no_pick) > 0:
        banned_civs.extend(no_pick)

    all_civs_stripped = [civ.strip('\n') for civ in all_civs]
    banned_civs_stripped = [civ.strip('\n') for civ in banned_civs]
    available_civs = [civ for civ in all_civs_stripped if civ not in banned_civs_stripped]
    if len(add_pick) > 0:
        available_civs.extend(add_pick)  # add_pick takes priority over no_pick

    civ_number = random.randint(0, len(available_civs) - 1)
    print(f"You should play {available_civs[civ_number]} this game")
    return 

# organise_all_civs()
civ_selector()
