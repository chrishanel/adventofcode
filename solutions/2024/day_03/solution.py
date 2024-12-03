# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import TextSolution, answer
import re


class Solution(TextSolution):
    _year = 2024
    _day = 3

    @answer(153469856)
    def part_1(self) -> int:
        total = 0
        i = re.findall('mul\(\\d+,\\d+\)', self.input)
        for j in i:
            nums = re.findall('\\d+', j)
            nums = [ int(x) for x in nums]
            total += nums[0] * nums[1]

        return total

    @answer(77055967)
    def part_2(self) -> int:
        total = 0
        enabled = True
        i = re.findall('(mul\(\\d+,\\d+\)|do\(\)|don\'t\(\))', self.input)
        print(i)
        for j in i:
            if j == "do()":
                enabled = True
            elif j == "don't()":
                enabled = False
            else:
                if enabled:
                    nums = re.findall('\\d+', j)
                    nums = [ int(x) for x in nums]
                    total += nums[0] * nums[1]
        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
