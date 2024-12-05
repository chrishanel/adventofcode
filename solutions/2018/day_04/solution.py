# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2018/day/4

from ...base import StrSplitSolution, answer
import re


class Solution(StrSplitSolution):
    _year = 2018
    _day = 4

    def create_log(self):
        guards = {}
        log = self.input
        log.sort()
        asleep = False
        lastEntry = 0

        for i in log:
            x = re.findall('(\\d+) begins shift', i)
            y = re.findall('(\\d+)\] falls asleep', i)
            z = re.findall('(\\d+)\] wakes up', i)

            if x:
                if asleep:
                    guards[currentGuard] = self.mark_asleep(guards[currentGuard], lastEntry, 59)
                currentGuard = x[0]
                asleep = False
                if not x[0] in guards:
                    guards[x[0]] = [0] * 60
            
            if y:
                lastEntry = int(y[0])

            if z:
                wakeTime = int(z[0])
                guards[currentGuard] = self.mark_asleep(guards[currentGuard], lastEntry, wakeTime)
        
        return guards


    def mark_asleep(self, graph, start, end):
        for x in range (start, end):
            graph[x] += 1
        return graph

    @answer(19874)
    def part_1(self) -> int:
        guards = self.create_log()
        
        solve = ['', 0, 0]
        for x, key in enumerate(guards):
            total = sum(guards[key])
            if total > solve[1]:
                solve = [key, total, guards[key].index(max(guards[key]))]
        
        return (int(solve[0]) * solve[2])

    @answer(22687)
    def part_2(self) -> int:
        guards = self.create_log()

        solve = ['', 0, 0]
        for x, key in enumerate(guards):
            best = [guards[key].index(max(guards[key])), max(guards[key])]
            if best[1] > solve[2]:
                solve = [key, best[0], best[1]]

        return(int(solve[0]) * solve[1])

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
