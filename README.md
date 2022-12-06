advent of code 2022
===================

https://adventofcode.com/2022

### about

for 2022, I'm planning to implement in python

### timing

- comparing to these numbers isn't necessarily useful
- normalize your timing to day 1 part 1 and compare
- alternate implementations are listed in parens
- these timings are very non-scientific (sample size 1)

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
+ python ./day01/part1.py ./day01/input.txt
71780
> 568 μs
+ python ./day01/part2.py ./day01/input.txt
212489
> 578 μs
+ python ./day02/part1.py ./day02/input.txt
15422
> 1590 μs
+ python ./day02/part2.py ./day02/input.txt
15442
> 2048 μs
+ python ./day03/part1.py ./day03/input.txt
8176
> 641 μs
+ python ./day03/part2.py ./day03/input.txt
2689
> 549 μs
+ python ./day04/part1.py ./day04/input.txt
444
> 851 μs
+ python ./day04/part2.py ./day04/input.txt
801
> 946 μs
+ python ./day05/part1.py ./day05/input.txt
GFTNRBZPF
> 892 μs
+ python ./day05/part2.py ./day05/input.txt
VRQWPDSGP
> 828 μs
+ python ./day06/part1.py ./day06/input.txt
1142
> 389 μs
+ python ./day06/part2.py ./day06/input.txt
2803
> 1683 μs
```
