from __future__ import annotations
from typing import Any, Optional


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self) -> None:
        """Initialize an empty linked list.
        """
        self._head = None
        self._tail = None

    def __len__(self) -> int:
        """Return the number of elements in this list.

        """
        counter = 0
        curr = self._head
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def print_items(self) -> None:
        """Print out each item in this linked list."""
        curr = self._head
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def insert(self, nodeValue, index):
        new_node = _Node(nodeValue)
        if not self._head:
            raise ValueError("Linked List is empty")

        elif index == 0:  # insert at first pos
            new_node.next = self._head
            self._head = new_node

        elif index == (len(self) - 1):
            new_node.next = None
            self._tail.next = new_node
            self._tail = new_node  # update tail

        else:  # insert at specified location
            previous = None
            current = self._head
            current_position = 0
            while (current_position < index) and current.next:
                previous = current
                current = current.next
                current_position += 1
            previous.next = new_node
            new_node.next = current

    def reverse_iterative(self):
        if self._head:
            current_node = self._head
            print("Start_Current_Node = " + str(current_node.item))
            next_node = current_node.next
            print("Start_Next_Node = " + str(next_node.item))
            current_node.next = None
            while next_node:
                tmp = next_node.next
                print("tmp = " + str(tmp.item))
                next_node.next = current_node
                print("next_node.next = " + str(next_node.next.item))
                self._head = current_node
                print("self._head = " + str(self._head.item))
                current_node = next_node
                print("current_node = ", str(current_node.item))
                next_node = tmp
                print("next_node = " + str(next_node.item))
                print("New Self.head is " + str(self._head.item))
        return self._head


if __name__ == '__main__':
    node = _Node(10)
    node2 = _Node(11)
    node3 = _Node(12)
    node4 = _Node(13)
    node5 = _Node(14)
    node6 = _Node(15)

    node.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    LL = LinkedList()
    LL._head = node
    LL._tail = node6

    LL.reverse_iterative()
