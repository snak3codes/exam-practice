#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:40:37 2020

@author: snak3
"""

class _Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None
    
    def print_items(self):
        curr = self._head
        while curr is not None:
            print(curr.item)
            curr = curr.next
            
    def reverse_recursive(self, head):
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            nextNode = head.next
            head.next = None
            rest = self.reverse_recursive(nextNode)
            nextNode.next = head
            return rest
        
    def reverse_iterative(self):
        prev = None
        curr = self._head
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
            
            
            
node1 = _Node(1)
node2 = _Node(2)
node3 = _Node(3)
node4 = _Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

LL = LinkedList()
LL._head = node1
LL.print_items()
rev = LL.reverse_recursive(LL._head)
LL2 = LinkedList()
LL2._head = rev

LL2.print_items()
