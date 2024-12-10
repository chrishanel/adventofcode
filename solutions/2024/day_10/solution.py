# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/10

from ...base import StrSplitSolution, answer
import networkx as nx


class Solution(StrSplitSolution):
    _year = 2024
    _day = 10




    # @answer(1234)
    def part_1(self) -> int:
        score = 0
        G = nx.DiGraph()
        coords = {(x, y): int(cell) for y, row in enumerate(self.input) for x, cell in enumerate(row)}
        for i in coords:
            G.add_node(i)

        for i in G:
            x = i[0]
            y = i[1]
            height = coords[i]
            dirs = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            for d in dirs:
                try: 
                    target = coords[d]
                    print(target, height)
                    if target == height + 1:
                        print("ping")
                        G.add_edge(i, d)
                except:
                    pass

        for i in G:
            if coords[i] == 0:
                spaces = nx.descendants(G, i)
                for j in spaces:
                    if coords[j] == 9:
                        score += 1

            
        return score

    # @answer(1234)
    def part_2(self) -> int:
        score = 0
        G = nx.DiGraph()
        coords = {(x, y): int(cell) for y, row in enumerate(self.input) for x, cell in enumerate(row)}
        for i in coords:
            G.add_node(i)

        for i in G:
            x = i[0]
            y = i[1]
            height = coords[i]
            dirs = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            for d in dirs:
                try: 
                    target = coords[d]
                    print(target, height)
                    if target == height + 1:
                        print("ping")
                        G.add_edge(i, d)
                except:
                    pass

        for i in G:
            if coords[i] == 0:
                spaces = nx.descendants(G, i)
                for j in spaces:
                    if coords[j] == 9:
                        for path in nx.all_simple_paths(G, i, j):
                            score += 1

            
        return score

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
