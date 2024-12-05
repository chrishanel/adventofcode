# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2018/day/5

from ...base import TextSolution, answer
from string import ascii_lowercase as alc
import string
import re


class Solution(TextSolution):
    _year = 2018
    _day = 5

    def scanner(self, units):
        searching = True
        pattern = '|'.join([''.join(i) for i in zip(list(string.ascii_uppercase), list(string.ascii_lowercase))] + [''.join(i) for i in zip(list(string.ascii_lowercase), list(string.ascii_uppercase))])
        new_units = units
        while searching:
            old_units = new_units
            new_units = re.sub(f'{pattern}', "", new_units)
            if len(new_units) == len(old_units):
                return len(new_units)
        

    # @answer(1234)
    def part_1(self) -> int:
        solve = self.scanner(self.input)

        return solve

    # @answer(1234)
    def part_2(self) -> int:
        s = self.input
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        M = {}
        for c in alpha:
            M[c.lower()] = c.upper()
            M[c.upper()] = c.lower()

        ans = 1e5
        for rem in alpha:
            s2 = [c for c in s if c!=rem.lower() and c!=rem.upper()]
            stack = []
            for c in s2:
                if stack and c == M[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(c)
            ans = min(ans, len(stack))

        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
