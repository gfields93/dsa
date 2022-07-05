

class BinarySearchTree:
    class TreeNode:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None

    def __init__(self) -> None:
        self.root: self.TreeNode = None

    def insert(self, value):
        if self.root != None:
            self.root = self.TreeNode(value)
        else:
            self.insert_node(self.root, value)
            
    def insert_node(self, current, value):
        if value < current.value:
            if current.left == None:
                current.left = self.TreeNode(value)
            else:
                self.insert_node(current.left, value)
        else:
            if current.right == None:
                current.right = self.TreeNode(value)
            else:
                self.insert_node(current.right, value)