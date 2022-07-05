from typing import Optional

class LinkedList:
    class ListNode:
        def __init__(self, value) -> None:
            self.value = value
            self.next: Optional['ListNode'] = None
    
    def __init__(self) -> None:
        self.tail: Optional[self.ListNode] = None
        self.head: Optional[self.ListNode] = None
        self.traveralNode: Optional[self.ListNode] = None

    def insert(self, value) -> None:
        """
        algorithm Add(value)
        Pre: value is the value to add to the list
        Post: value has been placed at the tail of the list
        """
        newNode = self.ListNode(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.traveralNode = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode

    def contains(self, value) -> bool:
        """
        algorithm Contains(head, value)
        Pre: head is the head node in the listvalue is the value to search for
        Post: the item is either in the linked list, true; otherwise false
        """
        n: self.ListNode = self.head
        while n != None and n.value != value:
            n = n.next
        if n == None:
            return False
        else: 
            return True

    def remove(self, value) -> bool:

        """
        algorithm Remove(head, value)
        Pre: head is the head node in the list value is the value to remove from the list
        Post: value is removed from the list, true; otherwise false
        """
        if self.head == None:
            return False
        n = self.head
        if n.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return True
        while n.next != None and n.next.value != value:
            n = n.next
        if n.next != None:
            if n.next == self.tail:
                self.tail = n
                self.tail.next = None
            else:
                n.next = n.next.next
            return True
        return False

    def traverse(self) -> int:
        """
        algorithm Traverse()
        Pre: head is the head node in the list
        Post: the items in the list have been traversed
        """
        returnVal = self.traveralNode.value
        if self.traveralNode.next != None:
            self.traveralNode = self.traveralNode.next
        return returnVal

    def reverseTraverse(self) -> int:
        """
        algorithm ReverseTraversal(head, tail)
        Pre: head and tail belong to the same list
        Post: the items in the list have been traversed in reverse order
        """
        if self.tail != None and self.traveralNode != self.head:
            curr = self.head
            while curr.next != self.traveralNode:
                curr = curr.next
            self.traveralNode = curr
            return self.traveralNode.value
