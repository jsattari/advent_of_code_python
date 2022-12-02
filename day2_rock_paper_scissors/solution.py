#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import List, Dict, cast


# load input data from file
folder_filename = "/day2_rock_paper_scissors/input.txt"
data = open(str(pathlib.Path().absolute()) + folder_filename).read()

rounds = [pair.split(" ") for pair in data.split("\n")]

choices = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
pts = {"Rock": 1, "Paper": 2, "Scissors": 3}


def total_score(
    scores: List[List[str]], methods: Dict[str, str], scoring: Dict[str, int]
) -> int:
    opp_pts = 0
    my_pts = 0

    win = 6
    tie = 3

    for game in scores:
        opp = game[0]
        me = game[1]

        opp_choice = cast(str, methods.get(opp))
        my_choice = cast(str, methods.get(me))

        # points for round
        my_total = cast(int, scoring.get(my_choice))
        opp_total = cast(int, scoring.get(opp_choice))

        if opp_choice == my_choice:
            my_pts += my_total + tie
            opp_pts += opp_total + tie

        elif my_choice == "Rock":
            if opp_choice == "Scissors":
                my_pts += my_total + win
                opp_pts += opp_total

            else:
                my_pts += my_total
                opp_pts += opp_total + win

        elif my_choice == "Paper":
            if opp_choice == "Rock":
                my_pts += my_total + win
                opp_pts += opp_total

            else:
                my_pts += my_total
                opp_pts += opp_total + win

        elif my_choice == "Scissors":
            if opp_choice == "Paper":
                my_pts += my_total + win
                opp_pts += opp_total

            else:
                my_pts += my_total
                opp_pts += opp_total + win
        else:
            my_pts += 0
            opp_pts += 0

    return my_pts


if __name__ == "__main__":
    print(total_score(rounds, choices, pts))
