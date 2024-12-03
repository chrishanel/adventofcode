# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2018/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2018
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        voltage = 0
        for i in self.input:
            op = i[0]
            j = i[1:]
            if op == "+":
                voltage += int(j)
            else:
                voltage -= int(j)

        return voltage

    # @answer(1234)
    def part_2(self) -> int:
        voltage = 0
        looking = True
        logged = []
        while looking:
            for i in self.input:
                op = i[0]
                j = i[1:]
                if op == "+":
                    voltage += int(j)
                else:
                    voltage -= int(j)
                logged.append(voltage)
                print(voltage)
                if logged.count(voltage) > 1:
                    return voltage


        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
