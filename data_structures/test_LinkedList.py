import unittest
from LinkedList import LinkedList

class TestLnkedListInsert(unittest.TestCase):
    def test_empty_insert(self):
        testList = LinkedList()
        testList.insert(5)
        self.assertEqual(5, testList.head.value)

    def test_multi_insert(self):
        testValues = [1, 45, 60, 12]
        testList = LinkedList()

        for val in testValues:
            testList.insert(val)

        currentNode = testList.head
        for val in testValues:
            with self.subTest(val=val):
                self.assertEqual(val, currentNode.value)
                currentNode = currentNode.next

class TestLinkedListContains(unittest.TestCase):
    def setUp(self) -> None:
        test_values = [5, 43, 92, 100, 4, 88, 23, 46]
        self.test_list = LinkedList()
        for val in test_values:
            self.test_list.insert(val)

    def test_find_first(self):
        self.assertTrue(self.test_list.contains(5))

    def test_find_last(self):
        self.assertTrue(self.test_list.contains(46))

    def test_find_100(self):
        self.assertTrue(self.test_list.contains(100))

    def test_find_no_value(self):
        self.assertFalse(self.test_list.contains(29))

class TestLinkedListRemove(unittest.TestCase):
    def setUp(self) -> None:
        test_values = [5, 43, 92, 100, 4, 88, 23, 46]
        self.test_list = LinkedList()
        for val in test_values:
            self.test_list.insert(val)

    def test_remove_first(self):
        self.test_list.remove(5)
        self.assertFalse(self.test_list.contains(5))

    def test_remove_last(self):
        self.test_list.remove(46)
        self.assertFalse(self.test_list.contains(46))

    def test_remove_100(self):
        self.test_list.remove(100)
        self.assertFalse(self.test_list.contains(100))

    def test_empty_list(self):
        new_test_list = LinkedList()
        self.assertFalse(new_test_list.remove(0))

class TestLinkedListTraverse(unittest.TestCase):
    def test_traversal(self):
        test_values = [5, 43, 92, 100, 4, 88, 23, 46]
        test_list = LinkedList()
        for val in test_values:
            test_list.insert(val)

        for val in test_values:
            with self.subTest(val=val):
                self.assertEqual(val, test_list.traverse())

class TestLinkedListReverseTraverse(unittest.TestCase):
    def test_reverse_traverse(self):
        test_value = [5, 10, 1, 40]
        test_list = LinkedList()

        for val in test_value:
            test_list.insert(val)
        for _ in range(4):
            test_list.traverse()

        for val in reversed(test_value[:3]):
            with self.subTest(val=val):
                self.assertEqual(val, test_list.reverseTraverse())


if __name__=='__main__':
    unittest.main()