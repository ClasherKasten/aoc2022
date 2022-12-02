from __future__ import annotations

import argparse
import os.path

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


opponent_alphabet = 'ABC'
my_alphabet = 'XYZ'
p2_mapping = {
    'A': ('Z', 'X', 'Y'),
    'B': ('X', 'Y', 'Z'),
    'C': ('Y', 'Z', 'X')
}

def calc_points(opponent_move: str, my_move: str) -> int:
    if my_alphabet.index(my_move) == opponent_alphabet.index(opponent_move):
        return 3 + my_alphabet.index(my_move) + 1
    elif (
            (my_move == 'X' and opponent_move == 'C')
            or (my_move == 'Y' and opponent_move == 'A')
            or (my_move == 'Z' and opponent_move == 'B')
    ):
        return 6 + my_alphabet.index(my_move) + 1
    else:
        return my_alphabet.index(my_move) + 1


def compute(s: str) -> int:
    points = 0

    lines = s.splitlines()
    for line in lines:
        opponent_move, my_move = line.split()
        my_move = p2_mapping[opponent_move][my_alphabet.index(my_move)]
        points += calc_points(opponent_move, my_move)

    return points


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 12


@pytest.mark.parametrize(
    ('m', 'res'),
    (
        (('A', 'X'), 4),
        (('A', 'Y'), 8),
        (('A', 'Z'), 3),

        (('B', 'X'), 1),
        (('B', 'Y'), 5),
        (('B', 'Z'), 9),

        (('C', 'X'), 7),
        (('C', 'Y'), 2),
        (('C', 'Z'), 6),

    )
)
def test_calc(m, res):
    assert calc_points(*m) == res


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
