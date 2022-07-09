from lib2to3.pgen2.token import SLASHEQUAL
import unittest
from BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.test_values = [5, 43, 92, 100, 4, 88, 23, 46]
        self.test_tree = BinarySearchTree()
        for val in self.test_values:
            self.test_tree.insert(val)

    def test_insert(self) -> None:
        self.assertEqual(len(self.test_values), self.test_tree.count)

    def test_contains(self) -> None:
        for val in self.test_values:
            with self.subTest(val=val):
                self.assertTrue(self.test_tree.contains(val))

    def test_removal(self):
        removal_vals = [5, 92, 46, 88, 23]
        for num, val in enumerate(removal_vals):
            with self.subTest(val=val):
                self.test_tree.remove(val)
                self.assertFalse(self.test_tree.contains(val))
                self.assertEqual(len(self.test_values)-(num+1), self.test_tree.count)

    def test_min(self):
        self.assertEqual(4, self.test_tree.find_min().value)

    def test_max(self):
        self.assertEqual(100, self.test_tree.find_max().value)

    def test_preorder(self):
        answer_list = [5, 4, 43, 23, 92, 88, 46, 100]
        self.assertSequenceEqual(answer_list, self.test_tree.preorder_traverse())

    def test_postorder(self):
        answer_list = [4, 23, 46, 88, 100, 92, 43, 5]
        self.assertSequenceEqual(answer_list, self.test_tree.postorder_traverse())
    
    def test_inorder(self):
        answer_list = [4, 5, 23, 43, 46, 88, 92, 100]
        self.assertSequenceEqual(answer_list, self.test_tree.inorder_traverse())

    def test_breadth(self):
        answer_list = [5, 4, 43, 23, 92, 88, 100, 46]
        self.assertSequenceEqual(answer_list, self.test_tree.breadth_first())

if __name__=="__main__":
    unittest.main()