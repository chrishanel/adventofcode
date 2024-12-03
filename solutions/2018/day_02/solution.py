# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2018/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2018
    _day = 2

    # @answer(1234)
    def part_1(self) -> int:
        pair = 0
        trips = 0

        for i in self.input:
            this_pair = False
            this_trips = False
            for j, char in enumerate(i):
                if i.count(char) == 2:
                    this_pair = True
                if i.count(char) == 3:
                    this_trips = True
            if this_pair: pair += 1
            if this_trips: trips += 1

        return pair * trips

    # @answer(1234)
    def part_2(self) -> str:
        for idx, i in enumerate(self.input):
            for j in range (idx, len(self.input)):
                test_i = i
                test_j = j
                count = 0
                for idx, k in enumerate(i):
                    if i[idx] != self.input[j][idx]:
                        test_i = test_i[:idx] + test_i[idx+1:]
                        count += 1
                if count == 1:
                    return test_i

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
