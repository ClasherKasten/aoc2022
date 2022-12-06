from __future__ import annotations

import argparse
import os.path

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
HEADER_LENGTH = 14


def compute(s: str) -> int:
    for i, c in enumerate(s):
        sub = set(s[i:i+HEADER_LENGTH])
        if len(sub) == HEADER_LENGTH:
            return i + HEADER_LENGTH
    return -1


INPUT_S = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''
EXPECTED = 19


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)
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
