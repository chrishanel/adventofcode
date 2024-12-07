# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer
import numpy as np
import re


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    def loopcheck(self, b, space, start, width, path):
        #print("###########")
        #print(space)
        #print("###########")
        if space == start:
            return False
        
        if space in path:
            return False
        
        next = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        if len(path) < 2:
            turns = 0
        else:
            #print(path[-2], path[-1])
            dir = tuple(np.subtract(path[-1], path[-2]))
            turns = next.index(dir)
        
        newblocks = b.copy()
        newblocks.append(space)
        here = path[-1]
        moving = True
        while moving:
            next_space = tuple(map(sum, zip(here, next[turns % 4])))
            if any(x < 0 for x in next_space) or any(x > width-1 for x in next_space):
                return False
            if next_space in newblocks:
                turns += 1
            else:
                following = [path[x+1] if x+1 < len(path) else None for x in range(len(path)) if path[x] == here]
                if next_space in following:
                    return space
                here = next_space
                path.append(here)




    # @answer(1234)
    def part_1(self) -> int:
        height = len(self.input)
        width = len(self.input[0])
        turns = 0
        next = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        blocks = []
        path = []
        for idx, i in enumerate(self.input):
            brow = [m.start() for m in re.finditer('#', i)]
            for j in brow:
                blocks.append((j, idx))

            if "^" in i:
                start = (i.find('^'), idx)

        path.append(start)
        here = start
        moving = True
        while moving:
            next_space = tuple(map(sum, zip(here, next[turns % 4])))
            if any(x < 0 for x in next_space) or any(x > width-1 for x in next_space):
                return len(path)
            if next_space in blocks:
                turns += 1
            else:
                if next_space not in path:
                    path.append(next_space)
                here = next_space

    # @answer(1234)
    def part_2(self) -> int:
        width = len(self.input[0])
        turns = 0
        next = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        blocks = []
        path = []
        for idx, i in enumerate(self.input):
            brow = [m.start() for m in re.finditer('#', i)]
            for j in brow:
                blocks.append((j, idx))

            if "^" in i:
                start = (i.find('^'), idx)

        path.append(start)
        here = start
        moving = True
        while moving:
            next_space = tuple(map(sum, zip(here, next[turns % 4])))
            if next_space in blocks:
                turns += 1
            elif any(x < 0 for x in next_space) or any(x > 129 for x in next_space):
                moving = False
            else:
                path.append(next_space)
                here = next_space

        
        options = []
        escaped = 0
        loop = 0

        for idx, space in enumerate(path):
            print(loop)
            loop+=1
            if self.loopcheck(blocks, space, start, width, path[:idx]):
                if space not in options:
                    options.append(space)
            else:
                escaped += 1

        print(escaped)
        return len(options)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
