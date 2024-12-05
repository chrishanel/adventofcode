# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2021/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2021
    _day = 2

    # @answer(1234)
    def part_1(self) -> int:
        forward = 0
        depth = 0
        for x in self.input:
            step = x.split()
            amt = int(step[1])
            if step[0] == "forward":
                forward += amt
            if step[0] == "down":
                depth += amt
            if step[0] == "up":
                depth -= amt

        return forward * depth

    # @answer(1234)
    def part_2(self) -> int:
        forward = 0
        depth = 0
        aim = 0

        for x in self.input:
            step = x.split()
            amt = int(step[1])
            if step[0] == "forward":
                forward += amt
                depth += amt * aim
            if step[0] == "down":
                aim += amt
            if step[0] == "up":
                aim -= amt

        return forward * depth
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
