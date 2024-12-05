# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2021/day/1

from ...base import IntSplitSolution, answer


class Solution(IntSplitSolution):
    _year = 2021
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        count = 0
        for idx, x in enumerate(self.input):
            try:
                if self.input[idx] > self.input[idx - 1]:
                    count += 1
            except:
                continue

        return count

    # @answer(1234)
    def part_2(self) -> int:
        count = 0
        newlist = []
        for idx, x in enumerate(self.input):
            newlist.append(sum(self.input[idx:idx+3]))

        for idx, x in enumerate(newlist):
            try:
                if newlist[idx] > newlist[idx - 1]:
                    count += 1
            except:
                continue

        return count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
