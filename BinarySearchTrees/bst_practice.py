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

    def preorder(self) -> List[int]:
        """Pre order traversal of the BinarySearchTree
        """
        if self.is_empty():
            return []
        else:
            return [self._root] + self._left.preorder() + \
                self._right.preorder()

    def inorder(self) -> List[int]:
        """In order traversal of the BinarySearchTree
        """
        if self.is_empty():
            return []
        else:
            return self._left.inorder() + [self._root] + \
                self._right.inorder()

        # return self._left.inorder() + [self._root] + \
            # self._right.inorder() if not self.is_empty() else []

    def postorder(self) -> List[int]:
        """Post order traversal of the BinarySearchTree
        """
        if self.is_empty():
            return []
        else:
            return self._left.postorder() + self._right.postorder() + \
                [self._root]

    def levelOrder(self) -> List[int]:
        """Level order traversal of the BinarySearchTree
        """
        levels = []
        if self.is_empty():
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node._root)

            # process child nodes for the next level
            if node._left:
                helper(node._left, level + 1)
            if node._right:
                helper(node._right, level + 1)
        helper(self, 0)
        return levels[:-1]

    def max_depth(self) -> int:
        """ Return the maximum depth of this tree """
        if self.is_empty():
            return 0
        else:
            return max(self._left.max_depth(), self._right.max_depth()) + 1

    def is_symmetric(self) -> bool:
        """ Return if BST is symmetric. """
        lst = self.inorder()
        return lst[:len(lst) // 2] == lst[len(lst) // 2 + 1:]

    def is_valid_bst(self, root) -> bool:
        # TODO Fix
        def helper(node, lower, upper):
            if not node:
                return True
            if node._root >= upper or node._root <= lower:
                return False
            return helper(self._left, lower, self._root) and \
                helper(self, self._root, upper)

        return helper(self._root, float('-inf'), float('inf'))

    def searchBST(self, val) -> bool:
        """ Searches for <val> in BST. 
        If it exists. It returns True, otherwise False"""
        if self.is_empty():
            return False
        if self._root == val:
            return True
        elif self._root > val:
            return self._left.searchBST(val)
        else:
            return self._right.searchBST(val)

    def insertIntoBST(self, val) -> BinarySearchTree:
        """ Insert <val> into BST """
        if self.is_empty():
            return BinarySearchTree(val)
        if val > self._root:
            self._right = self._right.insertIntoBST(val)
        else:
            self._left = self._left.insertIntoBST(val)
        return self

    def deleteFromBST(self, val):
        """ Remove one occurrence of <val> from BST """
        if self.is_empty():
            pass
        elif self._root == val:
            self.deleteRoot()
        elif val < self._root:
            self._left.deleteFromBST(val)
        else:
            self._right.deleteFromBST(val)

    def deleteRoot(self) -> None:
        """ Remove the root of this tree 
        Precondition: This tree is *non-empty*
        """
        if self._left.is_empty() and self._right.is_empty():
            self._root = None
            self._left = None
            self._right = None
        elif self._left.is_empty():
            # Promote the right subtree
            # self = self._right does NOT work!
            self._root, self._left, self._right = \
                self._right._root, self._right._left, self._right._right
        elif self._right.is_empty():
            # Promote the left subtree
            self._root, self._left, self._right = \
                self._left._root, self._left._left, self._left._right
        else:
            # Both subtrees are non-empty. Can choose to replace the root
            # from either the max value of the left subtree, or the minimum
            # value of the right subtree
            self._root = self._left.maximum()

    def minimum(self) -> int:
        """ Returns the minimum value in the BST """
        if self.is_empty():
            return None
        elif self._left.is_empty():
            return self._root
        else:
            return self._left.minimum()

    def maximum(self) -> int:
        """ Returns the maximum value in the BST """
        if self.is_empty():
            return None
        elif self._right.is_empty():
            return self._root
        else:
            return self._right.maximum()

    def successor(self) -> int:
        """ Returns the successor of this BST """
        self = self._right
        return self.minimum()

    def predecessor(self) -> int:
        """ Returns the predecessor of this BST """
        self = self._left
        return self.maximum()

    def isBalanced(self) -> bool:
        """ Return True if the BST is balanced.
        A binary tree in which the left and right subtree of every node differ
        in height by no more than 1 """
        if self.is_empty():
            return True
        return abs(self._left.max_depth() - self._right.max_depth()) < 2 and \
            self._left.isBalanced() and self._right.isBalanced()


def sortedArrayToBST(num_list: List[int]) -> BinarySearchTree:
    """ Convert a sorted array <num> to BST"""
    def helper(left, right):
        if left > right:
            return None
        # choose left middle node as a root
        p = (left + right) // 2

        # inorder traversal: left -> node -> right
        root = BinarySearchTree(num_list[p])
        root._left = helper(left, p - 1)
        root._right = helper(p + 1, right)
        return root

    return helper(0, len(num_list) - 1)

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
