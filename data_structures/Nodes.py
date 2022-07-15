from typing import Optional, TypeVar

class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class AVLNode():
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height = None

    def _left_rotation(self):
        if self.right is None:
            return

        rightNode = self.right
        self.right = rightNode.left
        rightNode.left = self

    def _right_rotation(self):
        if self.left is None:
            return 
        leftNode = self.left
        self.left = leftNode.right
        leftNode.right = self
    
    def _left_and_right_rotation(self):
        self._left_rotation()
        self._right_rotation()

    def _right_and_left_rotation(self):
        self._right_rotation()
        self._left_rotation()

    def _check_balance(self):
        if self.left is None and self.right is None:
            self.height = -1
        else:
            self.height = max(self.left.height, self.right.height) + 1
        if self.left.height - self.right.value > 1:
            if self.left.left.height - self.left.right.value > 0:
                self._right_rotation()
            else:
                self._left_and_right_rotation()
        elif self.left.height - self.right.value < -1:
            if self.right.left.value - self.right.right.value < 0:
                self._left_rotation()
            else:
                self._right_and_left_rotation()

N = TypeVar("N", TreeNode, AVLNode)