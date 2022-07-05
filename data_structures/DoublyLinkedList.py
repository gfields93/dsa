
from typing import Optional
from LinkedList import LinkedList

class DoublyLinkedList(LinkedList):
    class DoublyListNode(LinkedList.ListNode):
        def __init__(self, value) -> None:
            # super().__init__(value)
            self.value = value
            self.prev: Optional['DoublyListNode'] = None
            self.next: Optional['DoublyListNode'] = None

    def __init__(self) -> None:
        super().__init__()
        self.head: Optional[self.DoublyListNode] = None
        self.tail: Optional[self.DoublyListNode] = None
        self.traveralNode: Optional[self.DoublyListNode] = None

    def insert(self, value) -> None:
        n = self.DoublyListNode(value)
        if self.head == None:
            self.head = n
            self.tail = n
            self.traveralNode = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n

    # def contains(self, value) -> bool:
    #     """
    #     algorithm Contains(head, value)
    #     Pre: head is the head node in the listvalue is the value to search for
    #     Post: the item is either in the linked list, true; otherwise false
    #     """
    #     n: self.DoublyListNode = self.head
    #     while n != None and n.value != value:
    #         n = n.next
    #     if n == None:
    #         return False
    #     else: 
    #         return True

    def remove(self, value) -> bool:
        if self.head == None:
            return False
        if value == self.head.value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return True
        n = self.head.next
        while n != None and value != n.value:
            n = n.next
        if n == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return True
        elif n != None:
            n.prev.next = n.next
            n.next.prev = n.prev
            return True
        return False

    def reverseTraverse(self) -> int:
        if self.traveralNode != self.head:
            rval = self.traveralNode.value
            self.traveralNode = self.traveralNode.prev
            return rval