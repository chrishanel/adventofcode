# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/9

from ...base import TextSolution, answer
import pytermgui as ptg
from .node import Node


class Solution(TextSolution):
    _year = 2024
    _day = 9

    def debugDisk(self, head):
        debug = ""
        current = head
        if isinstance(current.data, int):
            for x in range(current.data):
                debug += "."
        else:
            debug += "[" + str(current.data.getId()) + " " + str(current.data.getSize()) + "]"

        while current.next:
            if isinstance(current.next.data, int):
                for x in range(current.next.data):
                    debug += "."
            else:
                debug += "[" + str(current.next.data.getId()) + " " + str(current.next.data.getSize()) + "]"

            current = current.next

        return debug

    def listSwap(self, disk, first, last):
        disk[first] = disk[last]
        disk.pop(last)
        return disk
        
    def getFreeSector(self, head, size, last):
        search = head
        while search.next:
            if search == last:
                print("i found me")
                return None
            try:
                if search.data >= size:
                    return search
            except:
                pass

            search = search.next

        return None


    # @answer(1234)
    def part_1(self) -> int:
        return('hohoho')
        toggle = True
        disk = []
        diskIdx = 0

        for i in self.input:
            diskVal = int(i)
            if toggle:
                for x in range (diskVal):
                    disk.append(diskIdx)
                diskIdx += 1
                toggle = not toggle
            else:
                for x in range (diskVal):
                    disk.append(".")
                toggle = not toggle

        print(len(disk))

        for i in reversed(range(len(disk))):
            if "." not in disk:
                break
            if disk[i] == ".":
                disk.pop(i)
            else:
                idx2 = disk.index(".")
                if i > idx2:
                    print(disk.count("."), idx2, disk[i], disk[idx2])
                    disk = self.listSwap(disk, idx2, i)

            

               
        print(disk)
        solve = 0
        for idx, i in enumerate(disk):
            try:
                solve += int(i) * idx
            except:
                continue

        return solve

    # @answer(1234)
    def part_2(self) -> int:
        
        def insert_at_end(head, data):
            # Insert a new node at the end of the doubly linked list
            new_node = Node(data)
            if head is None:
                return new_node

            current = head
            while current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current
            return head

        def insert_before_node(node, data):
            if node is None:
                print("Error: The given node is None")
                return

            new_node = Node(data)
            new_node.prev = node.prev
            new_node.next = node

            if node.prev:
                node.prev.next = new_node

            node.prev = new_node

        class File:
            def __init__(self, id, size):
                self.id = id
                self.size = size

            def getId(self):
                return self.id
            
            def getSize(self):
                return self.size

        toggle = True
        diskIdx = 0

        head = None
        for i in self.input:
            diskVal = int(i)
            if toggle:
                if diskVal > 0:
                    newfile = File(diskIdx, int(i))
                    head = insert_at_end(head, newfile)
                diskIdx += 1
                toggle = not toggle
            else:
                if diskVal > 0:
                    head = insert_at_end(head, diskVal)
                toggle = not toggle

        print(self.debugDisk(head))

        current = head
        while current.next:
            current = current.next

        while current.prev:
            print(current.data)
            if isinstance(current.data, int):
                pass
            else:
                if current.data.getId() <= diskIdx:
                    diskIdx = current.data.getId()
                    size = current.data.getSize()
                    slot = self.getFreeSector(head, size, current)
                    if slot == None:
                        pass
                    else:
                        insert_before_node(slot, current.data)
                        current.data = size
                        slot.data -= size

            current = current.prev

        print(self.debugDisk(head))
        diskSector = 0
        checkSum = 0

        
        while current.next:
            if isinstance(current.data, int):
                if current.data > 0:
                    for x in range(current.data):
                        diskSector += 1
            else:
                for x in range (current.data.getSize()):
                    checkSum += diskSector * current.data.getId()
                    diskSector += 1
            current = current.next

        if isinstance(current.data, int):
                if current.data > 0:
                    for x in range(current.data):
                        diskSector += 1
        else:
            for x in range (current.data.getSize()):
                checkSum += diskSector * current.data.getId()
                diskSector += 1

        return checkSum 




    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
