from __future__ import annotations

import argparse
import os.path
import pprint

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    visible_map = []
    lines = s.splitlines()
    height_map = [[] for _ in lines[0]]
    for row, line in enumerate(lines):
        max_height = -1
        visible_map.append([])
        for col, tree in enumerate(line):
            height_map[col].append(int(tree))
            if int(tree) > max_height:
                max_height = int(tree)
                visible_map[row].append(1)
            else:
                visible_map[row].append(0)

        max_height = -1
        for idx, tree in enumerate(reversed(line), 1):
            if int(tree) > max_height:
                max_height = int(tree)
                visible_map[row][-idx] = 1
            else:
                visible_map[row][-idx] = 0 if visible_map[row][-idx] == 0 else 1

    for col_idx, col in enumerate(height_map):
        max_height = -1
        for row_idx, row in enumerate(col):
            if row > max_height:
                max_height = row
                visible_map[row_idx][col_idx] = 1
            else:
                visible_map[row_idx][col_idx] = 0 if visible_map[row_idx][col_idx] == 0 else 1

        max_height = -1
        for row_idx, row in enumerate(reversed(col), 1):
            if row > max_height:
                max_height = row
                visible_map[-row_idx][col_idx] = 1
            else:
                visible_map[-row_idx][col_idx] = 0 if visible_map[-row_idx][col_idx] == 0 else 1

    return sum(sum(r) for r in visible_map)


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 21


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
