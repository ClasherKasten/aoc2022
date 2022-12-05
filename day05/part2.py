from __future__ import annotations

import argparse
import os.path
import re

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> str:
    container, moves = s.split('\n\n')
    widths = re.findall(fr'\d+', container)
    last_line = container.split('\n')[-1]
    search_places = [last_line.index(width) for width in widths]
    tmp_stacks = [[l[i] for i in search_places] for l in container.split('\n')[:-1]]
    stacks = []
    for i in range(len(tmp_stacks[0])):
        tmp = []
        for j in range(len(tmp_stacks)):
            if tmp_stacks[j][i] != ' ':
                tmp.append(tmp_stacks[j][i])
        stacks.append(tmp)

    cre = re.compile(fr'move (\d+) from (\d+) to (\d+)')

    for command in moves.split('\n')[:-1]:
        num, from_, to = map(int, cre.match(command).groups())
        stacks[to - 1] = stacks[from_ - 1][:num] + stacks[to - 1]
        stacks[from_ -1] = stacks[from_ - 1][num:]

    return ''.join(s[0] for s in stacks)


INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = 'MCD'


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
