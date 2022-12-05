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
1-5,1-5
1-6,2-5
1-5,2-5
1-6,1-5
2-6,3-5
2-6,2-5
2-6,3-6
'''
EXPECTED = 7


@pytest.mark.parametrize(
    ('elfs', 'res'),
    (
        ((1, 1, 5, 5), True),
        ((1, 2, 6, 5), True),
        ((1, 2, 5, 5), True),
        ((1, 1, 6, 5), True),

        ((2, 3, 6, 5), True),
        ((2, 2, 6, 5), True),
        ((2, 3, 6, 6), True),

        ((1, 0, 5, 4), False),
        ((1, 3, 6, 7), False),
        ((0, 2, 4, 5), False),
        ((3, 1, 7, 5), False),

    )
)
def test_overlap(elfs, res):
    assert fully_overlap(*elfs) == res


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
