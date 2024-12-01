# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/7

from ...base import StrSplitSolution, answer

# so i have a line
# on the right, i've identified i wire. I'll give it a dict entry
# on the left, i have either a number OR inputs from other wires along with modifications
# if i have a number, i assign it to the dict and move on
# if i don't, i identify other wires in the string
# if i have the values for all the wires on the left, i perform the operation and assign the value
# if not, i drop it and move on
# i loop through this until i have a value for a


class Solution(StrSplitSolution):
    _year = 2015
    _day = 7

    def can_be_int(self, str):
        flag = True
        try:
            int(str)
        except ValueError:
            flag = False
        return flag
    
    def main_loop(self, part2):
        circuit = {}
        if part2:
            circuit["b"] = 3176
        keyword_list = ["AND", "OR", "NOT", "RSHIFT", "LSHIFT", "->"]
        oper_list = ["AND", "OR", "NOT", "RSHIFT", "LSHIFT"]

        while "a" not in circuit:
            print(circuit)
            for i in self.input:
                ready = True
                inst = i.split()
                operation = ""
                if inst[-1] in circuit:
                    continue

                destination = inst[-1]
                inputs = []

                del inst[-1]

                for j in inst:
                    if j in oper_list:
                        operation = j
                        continue
                    if j in keyword_list:
                        continue
                    if self.can_be_int(j):
                        inputs.append(int(j))
                        continue

                    if j in circuit:
                        inputs.append(circuit[j])
                    else:
                        ready = False

                if not ready:
                    print("NOT READY")
                    continue

                print("READY")

                match operation:
                    case "":
                        circuit[destination] = inputs[0]
                    case "OR":
                        circuit[destination] = inputs[0] | inputs[1]
                    case "AND":
                        circuit[destination] = inputs[0] & inputs[1]
                    case "NOT":
                        circuit[destination] = ~ inputs[0]
                    case "LSHIFT":
                        circuit[destination] = inputs[0] << inputs[1]
                    case "RSHIFT":
                        circuit[destination] = inputs[0] >> inputs[1]
                    case _:
                        print("uhhh")




        return circuit["a"]


    # @answer(1234)
    def part_1(self) -> int:
        answer = self.main_loop(False)
        return answer

    # @answer(1234)
    def part_2(self) -> int:
        answer = self.main_loop(True)
        return answer

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
