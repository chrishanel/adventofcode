# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer
import numpy as np


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    # @answer(1234)
    def part_1(self) -> int:
        coords = {(x, y): cell for y, row in enumerate(self.input) for x, cell in enumerate(row)}
        def resolve(coordinates): return ''.join(coords.get(c, '.') for c in coordinates)
        def p1(x,y): return map(resolve, zip(*[[(x+i,y), (x,y+i), (x+i,y+i), (x-i, y+i)] for i in range(4)]))
        return sum(sum(part in ['XMAS', 'SAMX'] for part in p1(x,y)) for x,y in coords)


    # @answer(1234)
    def part_2(self) -> int:
        coords = {(x, y): cell for y, row in enumerate(self.input) for x, cell in enumerate(row)}
        def resolve(coordinates): return ''.join(coords.get(c, '.') for c in coordinates)
        def p2(x,y): return map(resolve, zip(*[[(x-1+i,y-1+i), (x+1-i, y-1+i)] for i in range(3)]))
        return sum(all(part in ['MAS',  'SAM' ] for part in p2(x,y)) for x,y in coords)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
