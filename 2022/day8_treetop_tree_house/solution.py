#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import List, Tuple
from math import prod

# load input data from file
folder_filename = "/2022/day8_treetop_tree_house/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()
parsed = [[int(val) for val in row] for row in data]


def find_trees(lot: List[List[int]]) -> Tuple[int, int]:
    zipped = [*zip(*lot)]
    invisible: int = 0
    best_score: int = 0

    for num in range(1, len(lot) - 1):
        row = parsed[num]

        for val in range(1, len(lot[0]) - 1):
            col = zipped[val]
            tgt = lot[num][val]

            # get row of trees before and after current row
            # get trees ahead of and behind current tree
            batch = (
                row[val - 1 :: -1],  # noqa: E203
                row[val + 1 :],  # noqa: E203
                col[num - 1 :: -1],  # noqa: E203
                col[num + 1 :],  # noqa: E203
            )

            # find which trees are taller than target tree
            invisible += all(any(tree >= tgt for tree in bat) for bat in batch)

            # apply scoring to trees
            score = prod(
                next(
                    (key + 1 for key, val in enumerate(bat) if val >= tgt),
                    len(bat),  # noqa: E501
                )
                for bat in batch
            )
            best_score = max(best_score, score)

    return (len(lot[0]) * len(lot)) - invisible, best_score


if __name__ == "__main__":
    x, y = find_trees(parsed)
    print(f"Part 1: {x}")
    print(f"Part 2: {y}")
