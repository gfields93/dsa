
from abc import ABC, abstractmethod
from typing import List


class Heap(ABC):
    def __init__(self) -> None:
        self.heap: List[int] = []

    def __len__(self):
        return len(self.heap)

    def __contains__(self, value: int):
        i = 0
        while i < len(self.heap) and self.heap[i] != value:
            i += 1
        return i < len(self.heap)

    def add(self, value: int):
        self.heap.append(value)
        self._heapify()

    @abstractmethod
    def _heapify(self):
        pass

    @abstractmethod
    def remove(self, value: int):
        pass

    def contains(self, value: int):
        i = 0
        while i < len(self.heap) and self.heap[i] != value:
            i += 1
        return i < len(self.heap)

    def _swap(self, pos1: int, pos2: int):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]


class MinHeap(Heap):
    def _heapify(self):
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self._swap(i, (i-1) // 2)
            i = (i - 1) // 2

    def remove(self, value: int):
        left = lambda x: 2 * x + 1
        right = lambda x: 2 * x + 2
        try:
            index = self.heap.index(value)
        except:
            index = -1

        if index < 0:
            return False

        self.heap[index] = self.heap[len(self.heap)-1]
        del self.heap[len(self.heap)-1]

        while (left(index) < len(self.heap)) and ((self.heap[index] > self.heap[left(index)]) or (self.heap[index] > self.heap[right(index)])):
            if self.heap[left(index)] < self.heap[right(index)]:
                self._swap(left(index), index)
                index = left(index)
            else:
                self._swap(right(index), index)
                index = right(index)

    def contains(self, value: int):
        parent = lambda index: (index - 1) // 2
        start = 0
        nodes = 1
        while start < len(self.heap):
            start = nodes - 1
            end = nodes + start
            count = 0
            while start < len(self.heap) and start < end:
                if value == self.heap[start]:
                    return True
                if value > self.heap[parent(start)] and value < self.heap[start]:
                    count += 1
                start += 1
            if count == nodes:
                return False
            nodes *= 2
        return False

    def __contains__(self, value: int):
        parent = lambda index: (index - 1) // 2
        start = 0
        nodes = 1
        while start < len(self.heap):
            start = nodes - 1
            end = nodes + start
            count = 0
            while start < len(self.heap) and start < end:
                if value == self.heap[start]:
                    return True
                if value > self.heap[parent(start)] and value < self.heap[start]:
                    count += 1
                start += 1
            if count == nodes:
                return False
            nodes *= 2
        return False
    

class MaxHeap(Heap):
    def _heapify(self):
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self._swap(i, (i-1) // 2)
            i = (i-1) // 2

    def remove(self, value: int):
        left = lambda x: 2 * x + 1
        right = lambda x: 2 * x + 2
        try:
            index = self.heap.index(value)
        except:
            index = -1

        if index < 0:
            return False

        self.heap[index] = self.heap[len(self.heap)-1]
        del self.heap[len(self.heap)-1]

        while (left(index) < len(self.heap)) and ((self.heap[index] < self.heap[left(index)]) or (self.heap[index] < self.heap[right(index)])):
            if self.heap[left(index)] > self.heap[right(index)]:
                self._swap(left(index), index)
                index = left(index)
            else:
                self._swap(right(index), index)
                index = right(index)

    def contains(self, value: int):
        parent = lambda index: (index - 1) // 2
        start = 0
        nodes = 1
        while start < len(self.heap):
            start = nodes - 1
            end = nodes + start
            count = 0
            while start < len(self.heap) and start < end:
                if value == self.heap[start]:
                    return True
                if value < self.heap[parent(start)] and value > self.heap[start]:
                    count += 1
                start += 1
            if count == nodes:
                return False
            nodes *= 2
        return False

    def __contains__(self, value: int):
        parent = lambda index: (index - 1) // 2
        start = 0
        nodes = 1
        while start < len(self.heap):
            start = nodes - 1
            end = nodes + start
            count = 0
            while start < len(self.heap) and start < end:
                if value == self.heap[start]:
                    return True
                if value < self.heap[parent(start)] and value > self.heap[start]:
                    count += 1
                start += 1
            if count == nodes:
                return False
            nodes *= 2
        return False