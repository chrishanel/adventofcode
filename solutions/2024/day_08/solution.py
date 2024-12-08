# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/8

from ...base import StrSplitSolution, answer
import itertools
from operator import sub
from operator import add
import math


class Solution(StrSplitSolution):
    _year = 2024
    _day = 8

    def generate_nodes(self):
        nodes = {}
        for idx, i in enumerate(self.input):
            for idx2, j in enumerate(i):
                if j == ".":
                    continue
                else:
                    if j in nodes:
                        nodes[j].append((idx2, idx))
                    else:
                        nodes[j] = [(idx2, idx)]

        return nodes

    # @answer(1234)
    def part_1(self) -> int:
        nodes = self.generate_nodes()

        antinodes = []
        gridsize = len(self.input[0])

        for key, value in nodes.items():
            for i, j in itertools.combinations(range(len(value)), r=2):
                node1 = value[i]
                node2 = value[j]
                diff = tuple(map(sub, node2, node1))
                antiA = tuple(map(sub, node1, diff))
                if antiA[0] >= 0 and antiA[1] >= 0 and antiA[0] < gridsize and antiA[1] < gridsize:
                    antinodes.append(antiA)
                antiB = tuple(map(add, node2, diff))
                if 0 <= antiB[0] < gridsize and 0 <= antiB[1] < gridsize:
                    antinodes.append(antiB)


        allnodes = set(antinodes)
        return len(allnodes)

    # @answer(1234)
    def part_2(self) -> int:
        nodes = self.generate_nodes()
        antinodes = []
        gridsize = len(self.input[0])

        for key, value in nodes.items():
            for i, j in itertools.combinations(range(len(value)), r=2):
                
                node1 = value[i]
                node2 = value[j]

                antinodes.append(node1)
                antinodes.append(node2)
                diff = tuple(map(sub, node2, node1))
                gcd = math.gcd(diff[0], diff[1])
                rootDiff = (diff[0]/gcd, diff[1]/gcd)
                bound1 = True
                search = node1
                while bound1:
                    search = tuple(map(sub, search, rootDiff))
                    if 0 <= search[0] < gridsize and 0 <= search[1] < gridsize:
                            antinodes.append(search)
                    else: bound1 = False

                bound2 = True
                search = node1
                while bound2:
                    search = tuple(map(add, search, rootDiff))
                    if 0 <= search[0] < gridsize and 0 <= search[1] < gridsize:
                            antinodes.append(search)
                    else: bound2 = False
        
        allnodes = list(set(antinodes))
        allnodes.sort()
        return len(allnodes)




    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
