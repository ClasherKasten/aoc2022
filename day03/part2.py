from __future__ import annotations

import argparse
import os.path
import string

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    priority = 0
    lines = s.splitlines()
    tmp_lines = []
    counter = 0
    for line in lines:
        tmp_lines.append(line)
        counter += 1
        if counter == 3:
            (common_item,) = set(tmp_lines[0]) & set(tmp_lines[1]) & set(tmp_lines[2])
            priority += alphabet.index(common_item) + 1
            counter = 0
            tmp_lines = []

    return priority


INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
EXPECTED = 70


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
