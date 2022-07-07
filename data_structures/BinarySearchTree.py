


from typing import List, Optional
from typing_extensions import Self

class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: TreeNode = None
        self.count = 0

    def insert(self, value: int):
        if self.root is not None:
            self.root = TreeNode(value)
        else:
            self.insert_node(self.root, value)
        self.count += 1
            
    def insert_node(self, current: TreeNode, value: int):
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
            else:
                self.insert_node(current.left, value)
        else:
            if current.right is None:
                current.right = TreeNode(value)
            else:
                self.insert_node(current.right, value)

    def contains(self, value: int) -> bool:
        def inner_func(node: TreeNode, value: int):
            if node is None:
                return False
            if node.value is value:
                return True
            elif value < node.value:
                return inner_func(node.left, value)
            else: 
                return inner_func(node.right, value)

        return inner_func(self.root, value)

    def remove(self, value: int):
        nodeToBeRemoved = self.find_node(value)
        if nodeToBeRemoved is None:
            return False
        parent: Optional[TreeNode] = self.find_parent(value)
        if self.count == 1:
            self.root = None 
        elif nodeToBeRemoved.left is None and nodeToBeRemoved.right is None:
            if nodeToBeRemoved.value < parent.value:
                parent.left = None
            else:
                parent.right = None
        elif nodeToBeRemoved.left is None and nodeToBeRemoved.right is not None:
            if nodeToBeRemoved.value < parent.value:
                parent.left = nodeToBeRemoved.right
            else:
                parent.right = nodeToBeRemoved.right
        elif nodeToBeRemoved.left is not None and nodeToBeRemoved.right is None:
            if nodeToBeRemoved.value < parent.parent.value:
                parent.left = nodeToBeRemoved.left
            else:
                parent.right = nodeToBeRemoved.left
        else:
            largestValue: TreeNode = nodeToBeRemoved.left
            while largestValue.right is not None:
                largestValue = largestValue.right
            self.find_parent(largestValue).right = None
            nodeToBeRemoved.value = largestValue.value
        self.count -= 1

    def find_parent(self, value: int) -> Optional[TreeNode]:
        def inner_func(value, root: TreeNode):
            if value == root.value:
                return None
            if value < root.value:
                if root.left is None:
                    return None
                elif root.left.value == value:
                    return root
                else:
                    return inner_func(value, root.left)
            else:
                if root.right is None:
                    return None
                elif root.right.value == value:
                    return root
                else:
                    return inner_func(value, root.right)
        
        return inner_func(value, self.root)

    def find_node(self, value: int) -> Optional[TreeNode]:
        def inner_func(node: TreeNode,value: int):
            if self.root is None:
                return None
            if self.root.value == value:
                return self.root
            elif value < node.value:
                return inner_func(node.left, value)
            else:
                return inner_func(node.right, value)

        return inner_func(self.root, value)

    def find_min(self):
        def inner_func(root: TreeNode) -> TreeNode:
            if root.left is None:
                return root.value
            else:
                return self.find_min(root.left)

        inner_func(self.root)
    
    def find_max(self):
        def inner_func(root: TreeNode) -> TreeNode:
            if root.right is None:
                return root.value
            else:
                return self.find_max(root.right)

        return inner_func(self.root)

    def preorder_traverse(self) -> List[int]:
        def inner_func(node: TreeNode, list: List[int]):
            if node is not None:
                list.append(node.value)
                inner_func(node.left, list)
                inner_func(node.right, list)

        tree_contents: List[int] = []
        inner_func(self.root, tree_contents)
        return tree_contents
        
                
    def postorder_traverse(self) -> List[int]:
        def inner_func(node: TreeNode, list: List[int]):
            if node is not None:
                inner_func(node.left, list)
                inner_func(node.right, list)
                list.append(node.value)
        
        tree_contents: List[int] = []
        inner_func(self.root, tree_contents)
        return tree_contents

    def inorder_traverse(self) -> List[int]:
        def inner_func(node: TreeNode, list: List[int]):
            if node is not None:
                inner_func(node.left, list)
                list.append(node.value)
                inner_func(node.right, list)

        tree_contents: List[int] = []
        inner_func(self.root, tree_contents)
        return tree_contents

    def breadth_first(self) -> List[int]:
        q: List[TreeNode] = []
        visitedNodes: List[int] = []
        current_node = self.root
        while current_node is not None:
            visitedNodes.append(current_node.value)
            if current_node.left is not None:
                q.append(current_node.left)
            if current_node.right is not None:
                q.append(current_node.right)
            if len(q) != 0:
                current_node = q.pop(0)
            else:
                current_node = None
