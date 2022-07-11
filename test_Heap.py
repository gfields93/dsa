import unittest
from Heap import MaxHeap, MinHeap

class TestHeap(unittest.TestCase):

    def setUp(self) -> None:
        self.list_values = [7, 40, 29, 5, 92, 48, 30, 1, 0, 100]
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

        for val in self.list_values:
            self.min_heap.add(val)
            self.max_heap.add(val)
    
    def test_min_add(self):
        test_min_heap = MinHeap()
        for x in range(10):
            test_min_heap.add(x)
        
        self.assertEqual(10, len(test_min_heap))

    def test_max_add(self):
        test_max_heap = MaxHeap()
        for x in range(10):
            test_max_heap.add(x)
        
        self.assertEqual(10, len(test_max_heap))

    def test_heap_contains(self):
        for val in self.list_values:
            with self.subTest(val=val):
                self.assertTrue(val in self.min_heap)
                self.assertTrue(val in self.max_heap)

    def test_min_delete(self):
        deleted_values = [7, 100, 29, 1, 92]
        for val in deleted_values:
            with self.subTest(val=val):
                self.min_heap.remove(val)
                self.assertFalse(val in self.min_heap)

    def test_max_delete(self):
        deleted_values = [7, 100, 29, 1, 92]
        for val in deleted_values:
            with self.subTest(val=val):
                self.max_heap.remove(val)
                self.assertFalse(val in self.max_heap)


if __name__=="__main__":
    unittest.main()