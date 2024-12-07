# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/7

from ...base import StrSplitSolution, answer
import re

class Solution(StrSplitSolution):
    _year = 2024
    _day = 7
    
    def ternary (self, n, length) -> str:
        if n == 0:
            base = '0'
        else:
            nums = []
            while n:
                n, r = divmod(n, 3)
                nums.append(str(r))
            base = ''.join(reversed(nums))
        while len(base) < length:
            base = '0' + base
        
        return base
    
    def mathTree(self, target, digits, ternCheck = True):
        if ternCheck:
            iterDepth = 3 ** (len(digits)-1)
        else:
            iterDepth = 2 ** (len(digits)-1)
        for x in range(iterDepth):
            if ternCheck:
                enumeration = str(self.ternary(x, len(digits)-1))
            else:
                enumeration = str(format(x, "0" + str(len(digits)-1) + "b"))
            res = digits[0]
            for idx, char in enumerate(enumeration):
                if char == "0":
                    res += digits[idx+1]
                elif char == "1":
                    res = res * digits[idx+1]
                elif ternCheck:
                    res = int(f"{res}{digits[idx+1]}")
                if res > target:
                    break
            if res == target:
                return True
            
        return False
    
    def genValues(self):
        values = {}
        for i in self.input:
            numtext = re.findall(r'\d+', i)
            digits = [int(y) for y in numtext]
            target = digits.pop(0)

            values[i] = [target, digits]
        
        return values

    @answer(42283209483350)
    def part_1(self) -> int:
        values = self.genValues()
        solved = 0

        for target, digits in values.values():
            if self.mathTree(target, digits, False):
                solved += target

        return solved

    @answer(1026766857276279)
    def part_2(self) -> int:
        values = self.genValues()
        solved = 0
        for target, digits in values.values():
            if self.mathTree(target, digits):
                solved += target

        return solved

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
