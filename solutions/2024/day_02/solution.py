# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    def makearray(self, str):
        entries = str.split()
        log = []
        for x in entries:
            log.append(int(x))
        return log

    def check_entry(self, entry):
        entry_asc = entry.copy()
        entry_desc = entry.copy()
        entry_asc.sort()
        entry_desc.sort(reverse=True)

        if entry != entry_asc and entry != entry_desc:
            return False
        
        flag = True

        for idx, i in enumerate(entry):
            try:
                measure = abs(entry[idx] - entry[idx + 1])
            except:
                continue
            if measure > 3 or measure < 1:
                flag = False

        return flag
    
    # @answer(1234)
    def part_1(self) -> int:
        safe = 0
        for i in self.input:
            entry = self.makearray(i)
            if self.check_entry(entry):
                safe+= 1

        return safe


    # @answer(1234)
    def part_2(self) -> int:
        safe = 0
        fail = 0
        for i in self.input:
            entry = self.makearray(i)
            if self.check_entry(entry):
                safe += 1
            else:
                count_check = 0
                for idx, j in enumerate(entry):
                    entry_new = entry.copy()
                    entry_new.pop(idx)
                    if self.check_entry(entry_new):
                        count_check += 1
                if count_check > 0:
                    safe += 1
                else: fail+= 1

        return safe

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
