# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2021/day/3

from ...base import StrSplitSolution, answer
import numpy as np


class Solution(StrSplitSolution):
    _year = 2021
    _day = 3

    def list_tobin_toint(self, arr):
        solve = [str(item) for item in arr]
        s = ''.join(solve)
        final = int(s, base=2)

        return final

    def prune(self, grid, vip, col):
        newgrid = []

        for row in grid:
            if row[col] == vip:
                newgrid.append(row)

        newgrid = np.array(newgrid)
        return newgrid

    # @answer(1234)
    def part_1(self) -> int:
        a = []
        for x in self.input:
            row = list(x)
            row = [int(item) for item in row]
            a.append(row)

        bingrid = np.array(a)
        bingrid = np.transpose(bingrid)
        solve = []
        for row in bingrid:
            counts = np.bincount(row)
            solve.append(np.argmax(counts))
        
        solve = [str(item) for item in solve]
        s = ''.join(solve)
        inverse_s = ''
 
        for i in s:
        
            if i == '0':
                inverse_s += '1'
                
            else:
                inverse_s += '0'
                
        final = int(s, base=2)
        final_ep = int(inverse_s, base=2)

        return final * final_ep

    # @answer(1234)
    def part_2(self) -> int:
        a = []
        for x in self.input:
            row = list(x)
            row = [int(item) for item in row]
            a.append(row)

        bingrid = np.array(a)

        oxy_grid = bingrid
        co_grid = bingrid

        for col in range(oxy_grid.shape[1]):
            try:
                column = oxy_grid[:, col]
            except:
                break

            count = np.bincount(column)

            if count[0] > count[1]:
                oxy_grid = self.prune(oxy_grid, 0, col)
            else:
                oxy_grid = self.prune(oxy_grid, 1, col)

        for col in range(co_grid.shape[1]):
            try:
                column = co_grid[:, col]
            except:
                break

            count = np.bincount(column)
            if len(count) < 2:
                break
            if count[1] < count[0]:
                co_grid = self.prune(co_grid, 1, col)
            else:
                co_grid = self.prune(co_grid, 0, col)

        return self.list_tobin_toint(oxy_grid[0]) * self.list_tobin_toint(co_grid[0])

        


        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
