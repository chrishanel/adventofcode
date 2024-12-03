# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2018/day/3

from ...base import StrSplitSolution, answer
import re


class Solution(StrSplitSolution):
    _year = 2018
    _day = 3

    def markfab(self, fabric, right, down, width, height):
        for i in range (down, down+height):
            for j in range(right, right+width):
                fabric[i][j]+= 1

        return fabric
    
    def checkfab(self, fabric, right, down, width, height):
        perfect = True
        for i in range (down, down+height):
            for j in range(right, right+width):
                if fabric[i][j] != 1:
                    perfect = False

        return perfect


        
    @answer(107043)
    def part_1(self) -> int:
        fabric = [ [0]*1200 for _ in range(1200) ]
        for i in self.input:
            j = re.findall('\\d+', i)
            j = [ int(x) for x in j]
            fabric = self.markfab(fabric, j[1], j[2], j[3], j[4])

        count = 0
        for i in fabric:
            count += sum(k > 1 for k in i)

        return count

    # @answer(1234)
    def part_2(self) -> int:
        fabric = [ [0]*1200 for _ in range(1200) ]
        for i in self.input:
            j = re.findall('\\d+', i)
            j = [ int(x) for x in j]
            fabric = self.markfab(fabric, j[1], j[2], j[3], j[4])

        for i in self.input:
            j = re.findall('\\d+', i)
            j = [ int(x) for x in j]
            if self.checkfab(fabric, j[1], j[2], j[3], j[4]):
                return j[0]

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
