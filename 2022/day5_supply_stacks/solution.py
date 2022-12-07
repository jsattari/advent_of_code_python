#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import List, Union, cast


import re
from itertools import zip_longest

# load input data from file
folder_filename = "/2022/day5_supply_stacks/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read()


def crate_maker(filename: str) -> Union[List[List[str]], List[List[str]]]:
    x, y = filename.split("\n\n")

    boxes = [x[1::4] for x in x.splitlines()[:-1]]  # type: ignore
    boxes = [*zip_longest(*boxes[::-1], fillvalue=" ")]  # type: ignore
    boxes = [[e for e in x if not e.isspace()] for x in boxes]  # type: ignore

    acts = re.findall(r"move (\d+) from (\d+) to (\d+)", y)  # type: ignore
    acts = [map(int, act) for act in acts]  # type: ignore
    acts = [[x, y - 1, z - 1] for x, y, z in acts]  # type: ignore

    return boxes, acts  # type: ignore


if __name__ == "__main__":
    crates, moves = crate_maker(data)
    for move in moves:
        a, b, c = cast(List, move)
        for num in range(cast(int, a)):
            box = cast(List, crates[b]).pop()
            crates[c].append(box)
    print("Part 1: ", "".join([val[-1] for val in crates]))

    crates2, moves2 = crate_maker(data)
    for move in moves2:
        a, b, c = cast(List, move)
        chunk = []
        for num in range(a):
            box = crates2[b].pop()
            chunk.append(box)
        chunk = chunk[::-1]
        crates2[c] += chunk
    print("Part 2: ", "".join([val[-1] for val in crates2]))
