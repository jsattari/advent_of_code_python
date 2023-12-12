#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List
import re

import sys
sys.path.append('.')

from src.utility.helpers import file_finder


def part1(dataset: str) -> int:

    total: List[int] = []

    for line in dataset.split("\n"):

        num: str = ""

        for i in range(0, len(line)):
            if line[i].isdigit():
                num = line[i]
                break

        for j in range(len(line) - 1, -1, -1):
            if line[j].isdigit():
                num += line[j]
                break

        if num:
            total.append(int(num))

    return sum(total)


def part2(dataset: str) -> int:

    total: List[int] = []

    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    pattern = re.compile(
        r'(?=(\d|' + '|'.join(
            [word for word in word_to_digit.keys()]
        ) + '))', re.IGNORECASE
    )

    for line in dataset.split("\n"):

        num: str = ""

        matches = pattern.findall(line)

        if len(matches) > 0:
            first, last = matches[0], matches[-1]

            if first.isdigit():
                num = first
            else:
                num = word_to_digit[first.lower()]
            if last.isdigit():
                num += last
            else:
                num += word_to_digit[last.lower()]
            total.append(int(num))

    return sum(total)


if __name__ == "__main__":
    data = open(file_finder()).read()

    print(part1(data))
    print(part2(data))
