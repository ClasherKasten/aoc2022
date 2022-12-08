from __future__ import annotations

import argparse
import os.path
import pprint

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    dirs = {'/': [0, []]}
    path = '/'
    for line in lines[1:]:
        if line.startswith('$'):
            line = line.replace('$ ', '')
            command, _, new_dir = line.partition(' ')
            if new_dir == '..':
                p1, p2, _ = path.rpartition('/')
                path = '/' if p1 == '' else p1
                continue
            if command == 'cd':
                path = os.path.join(path, new_dir)
                dirs[path] = [0, []]
        else:
            size, _, name = line.rpartition(' ')
            if size == 'dir':
                dirs[path][1].append(os.path.join(path, name))
                continue
            dirs[path][0] += int(size)
            pass

    while True:
        ufound = False
        for k, v in dirs.items():
            for uncalc in v[1]:
                if dirs[uncalc][1] == []:
                    v[0] += dirs[uncalc][0]
                    v[1].remove(uncalc)
                    ufound = True
        if not ufound:
            break

    return sum(v[0] for v in dirs.values() if v[0] < 100_000)


INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
EXPECTED = 95437


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
