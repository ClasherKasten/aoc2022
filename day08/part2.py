from __future__ import annotations

import argparse
import os.path
import pprint

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _calc_line(line: list[int]):
    l = 0
    for i in line:
        if i == 0:
            break
        l += 1
    return l


def calc_scenic_score(top: list[int], bottom: list[int], left: list[int], right: list[int]) -> int:
    return _calc_line(top) * _calc_line(bottom) * _calc_line(left) * _calc_line(right)



def visible(line: list[int], max_height: int) -> int:
    count = 0
    for tree in line:
        count += 1
        if tree >= max_height:
            break
    return count


def max_scenic_score(height_map: list[list[int]], rotated_hm: list[list[int]]) -> int:
    max_score = 0
    for row_idx, row in enumerate(height_map):
        for col_idx, col in enumerate(row):
            column = rotated_hm[col_idx]
            left = row[:col_idx][::-1]
            right = row[col_idx+1:]
            top = column[:row_idx][::-1]
            bottom = column[row_idx+1:]
            if 0 in (row_idx, col_idx) or len(height_map) - 1 in (row_idx, col_idx):
                continue
            max_score = max(
                    max_score,
                    (
                        visible(left, col) * visible(right, col)
                        * visible(top, col) * visible(bottom, col)
                    )
            )
    return max_score



def compute(s: str) -> int:
    lines = s.splitlines()
    height_map = [[int(x) for x in line] for line in lines]
    rotated_hm = [
        [row[idx] for row in height_map]
        for idx, _ in enumerate(height_map[0])
    ]
    return max_scenic_score(height_map, rotated_hm)


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 8


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
