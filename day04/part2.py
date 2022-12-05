from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def fully_overlap(elf1_start, elf2_start, elf1_end, elf2_end):
    return (
        (elf1_start <= elf2_start and elf1_end >= elf2_end)
        or (elf2_start <= elf1_start and elf2_end >= elf1_end)
        or (elf1_start <= elf2_start <=  elf1_end)
        or (elf2_start <= elf1_start <= elf2_end)
    )


def compute(s: str) -> int:
    lines = s.splitlines()
    counter = 0
    for line in lines:
        elf1, _ ,elf2 = line.partition(',')
        elf1_start, _, elf1_end = elf1.partition('-')
        elf2_start, _ ,elf2_end = elf2.partition('-')
        if fully_overlap(int(elf1_start), int(elf2_start), int(elf1_end), int(elf2_end)):
            counter += 1

    return counter


INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 4


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
