from __future__ import annotations
from typing import Any, List, Optional


class Queue:
    def __init__(self):
        self._queue = []

    def is_empty(self):
        return self._queue == []

    def enqueue(self, item):
        self._queue.insert(0, item)

    def dequeue(self):
        return self._queue.pop()


class BinarySearchTree:

    def __init__(self, root: Optional[Any]) -> None:
        """Initialize a new BST containing only the given root value.

        If <root> is None, initialize an empty tree.
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def is_empty(self) -> bool:
        """Return True if this BST is empty.
        """
        return self._root is None

    def __contains__(self, value):
        if self.is_empty():
            return False
        elif self._root == value:
            return True
        elif value < self._root:
            return value in self._left
        else:
            return value in self._right

    def preorder(self):
        """Pre order traversal of the BinarySearchTree
        """
        if self.is_empty():
            return None
        else:
            print(self._root)
            self._left.preorder()
            self._right.preorder()

    def inorder(self):
        """In order traversal of the BinarySearchTree
        """
        if self.is_empty():
            return None
        else:
            self._left.inorder()
            print(self._root)
            self._right.inorder()

    def postorder(self):
        """Post order traversal of the BinarySearchTree
        """
        if self.is_empty():
            return
        else:
            self._left.postorder()
            self._right.postorder()
            print(self._root)

    def levelOrder(self):
        """Level order traversal of the BinarySearchTree using 1 Queue
        """
        Q = Queue()
        Q.enqueue(self)
        while not Q.is_empty():
            to_deq = Q.dequeue()
            if to_deq._root:
                print(to_deq._root)
            else:
                break
            if self._left and self._right:
                Q.enqueue(to_deq._left)
                Q.enqueue(to_deq._right)

    def insert_node(self, item_to_insert: int) -> int:
        # @date_implemented: 09-03-2020
        """Insert <item_to_insert> as a new node in the BinarySearchTree
        """
        if self.is_empty():
            self = BinarySearchTree(item_to_insert)
        elif item_to_insert <= self._root:
            self._left = self._left.insert_node(item_to_insert)
        else:
            self._right = self._right.insert_node(item_to_insert)
        return self

    def delete_node(self, item_to_delete):
        """Delete <item_to_delete> node from the BinarySearchTree"""
        # TODO Fix this
        # At the moment it deletes the tree beneath
        if self.is_empty():
            return None
        if item_to_delete < self._root:
            self._left.delete_node(item_to_delete)
        elif item_to_delete > self._root:
            self._right.delete_node(item_to_delete)
        else:
            if self._left and self._right:
                successor = self.find_successor()
                self = successor
                del successor
            elif item_to_delete._left:
                self = self._left
            elif item_to_delete._right:
                self = self._right
            else:
                self._root = None
        return self

    def delete_root(self) -> None:
        """ Delete the root of this BST
        """
        if self._left.is_empty() and self._right.is_empty():
            self._root = self._left = self._right = None
        elif self._left.is_empty():
            self._root, self._left, self._right = self._right.root,
            self._right.left, self._right.right
        elif self._right.is_empty():
            self._root, self._right, self._right
# TODO FINISH TOP

    def extract_max(self) -> Any:
        if self._right.is_empty():
            max_item = self._root
            self._root, self._left, self._right = \
                self, _left._root, self._left._left, self._left._right
            return max_item
        else:
            return self._right.extract_max()

    def delete(self, item: Any) -> None:
        """Remove *one* occurrence of <item> from this BST.
        DO nothing if <item> is not in the BST.
        """
        # Locate the item to delete, by traversing the tree
        # If BST is empty
        if self.is_empty():
            pass
        elif self._root == item:
            # delete self._root
            self.delete_root()
        # If item to delete is *less* than the value self,_root
        if item < self._root:
            self._left.delete(item)
        elif item > self._root:
            self._right.delete(item)

    def find_successor(self):
        """Helper function to find the successor of the node to be deleted
        """
        if self.is_empty():
            return None
        elif self._left.is_empty():
            return self._root
        else:
            self = self._right
            return self._left.find_successor()

    def find_predecessor(self):
        """Helper function to find the predecessor of the node to be deleted
        """
        if self.is_empty():
            return None
        elif self._right.is_empty():
            return self._root
        else:
            self = self._left
            return self._right.find_successor()
    # -------------------------------------------------------------------------

    # Additional BST methods
    # -------------------------------------------------------------------------

    def __str__(self) -> str:
        """Return a string representation of this BST.
        This string uses indentation to show depth.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this BST.
        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            answer = depth * '  ' + str(self._root) + '\n'
            answer += self._left._str_indented(depth + 1)
            answer += self._right._str_indented(depth + 1)
            return answer


if __name__ == '__main__':
    # bst = BinarySearchTree(3)
    # bst._right = BinarySearchTree(5)
    # bst._left = BinarySearchTree(2)
    bst = BinarySearchTree(7)
    left = BinarySearchTree(3)
    left._left = BinarySearchTree(2)
    left._right = BinarySearchTree(5)
    right = BinarySearchTree(11)
    right._left = BinarySearchTree(9)
    right._right = BinarySearchTree(13)
    bst._left = left
    bst._right = right
