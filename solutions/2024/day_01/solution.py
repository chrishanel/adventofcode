# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    def list_build(self):
        left = []
        right = []
        for i in self.input:
            print(i)
            j = i.split("   ")
            print(j)
            left.append(int(j[0]))
            right.append(int(j[1]))

        left.sort()
        right.sort()

        return(left, right)

    # @answer(1234)
    def part_1(self) -> int:
        left, right = self.list_build()

        answer = 0
        for idx, i in enumerate(left):
            answer += abs(i - right[idx])

        return answer

    # @answer(1234)
    def part_2(self) -> int:
        left, right = self.list_build()

        answer = 0

        for idx, i in enumerate(left):
            answer+= i * right.count(i)

        return answer

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
