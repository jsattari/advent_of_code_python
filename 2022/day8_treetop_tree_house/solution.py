#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import List

# load input data from file
folder_filename = "/2022/day8_treetop_tree_house/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()
parsed = [[int(val) for val in row] for row in data]


def find_trees(lot: List[List[int]]) -> int:
    zipped = [*zip(*lot)]
    visible = 0

    for num in range(1, len(lot) - 1):
        row = parsed[num]

        for val in range(1, len(lot[0]) - 1):
            col = zipped[val]
            tgt = lot[num][val]

            batch = (
                row[val - 1 :: -1],  # noqa: E203
                row[val + 1 :],  # noqa: E203
                col[num - 1 :: -1],  # noqa: E203
                col[num + 1 :],  # noqa: E203
            )

            visible += all(any(tree >= tgt for tree in bat) for bat in batch)

    return (len(lot[0]) * len(lot)) - visible


if __name__ == "__main__":
    print(f"Part 1: {find_trees(parsed)}")
