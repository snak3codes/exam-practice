"""Prep 8 Synthesize

=== CSC148 Winter 2020 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
Your task in this prep is to implement each of the unimplemented Tree methods
in this file.
The starter code has a recursive template that includes the "size-one" case;
you may or may not choose to use this in your final implementations.
"""
from __future__ import annotations
from typing import Any, List, Optional


class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and RecursiveList; the only major
    difference is that _rest has been replaced by _subtrees to handle multiple
    recursive sub-parts.
    """
    # === Private Attributes ===
    # The item stored at this tree's root, or None if the tree is empty.
    _root: Optional[Any]
    # The list of all subtrees of this tree.
    _subtrees: List[Tree]

    # === Representation Invariants ===
    # - If self._root is None then self._subtrees is an empty list.
    #   This setting of attributes represents an empty Tree.
    #
    #   Note: self._subtrees may be empty when self._root is not None.
    #   This setting of attributes represents a tree consisting of just one
    #   node.

    def __init__(self, root: Any, subtrees: List[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If <root> is None, the tree is empty.
        Precondition: if <root> is None, then <subtrees> is empty.
        """
        self._root = root  # Sets the root of the Tree to be root
        self._subtrees = subtrees  # Sets the subtree of the Tree to be the list
        # of trees

    def __str__(self) -> str:
        """Return a string representation of this tree.
        """
        return self._str_indented(0)

    def is_empty(self) -> bool:
        """Return True if this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None  # no root => return empty

    def __len__(self) -> int:
        """Return the number of items contained in this tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        """
        # BASE CASE - TREE IS EMPTY
        if self.is_empty():  # self is a leaf => return 0 (leaf has no subtrees)
            return 0  # do not increase the count
        size = 1  # count the root
        for subtree in self._subtrees:  # iterate through the subtrees of self
            size += subtree.__len__()  # could also do len(subtree) here
            # increase size by the length of the subtree
        return size

    def num_positives(self) -> int:
        """Return the number of positive integers in this tree.

        Precondition: all items in this tree are integers.

        Remember, 0 is *not* positive.

        >>> t1 = Tree(17, [])
        >>> t1.num_positives()
        1
        >>> t2 = Tree(-10, [])
        >>> t2.num_positives()
        0
        >>> t3 = Tree(1, [Tree(-2, []), Tree(10, []), Tree(-30, [])])
        >>> t3.num_positives()
        2
        """
        if self.is_empty():
            return 0
        num_pos = 0
        if self._root > 0:
            num_pos += 1
        for subtree in self._subtrees:
            num_pos += subtree.num_positives()
        return num_pos

    def maximum(self: Tree) -> int:
        """Return the maximum item stored in this tree.

        Return 0 if this tree is empty.

        Precondition: all values in this tree are positive integers.

        >>> t1 = Tree(17, [])
        >>> t1.maximum()
        17
        >>> t3 = Tree(1, [Tree(-2, []), Tree(10, []), Tree(-30, [])])
        >>> t3.maximum()
        10
        """
        # BASE CASE - IF TREE IS EMPTY
        if self.is_empty():
            return 0
        largest = self._root
        for subtree in self._subtrees:
            contender = subtree.maximum()
            if contender > largest:
                largest = contender
        return largest

    def height(self: Tree) -> int:
        """Return the height of this tree.

        Please refer to the prep readings for the definition of tree height.

        >>> t1 = Tree(17, [])
        >>> t1.height()
        1
        >>> t2 = Tree(1, [Tree(-2, []), Tree(10, []), Tree(-30, [])])
        >>> t2.height()
        2
        """
        if self.is_empty():
            return 0
        if not self._subtrees:  # if self is a leaf and leaf.subtrees == []
            return 1
        depths = []
        tallest = 0
        for subtree in self._subtrees:
            depths.append(subtree.height() + 1)
        if depths:
            tallest = max(depths)
        return tallest

    def __contains__(self, item: Any) -> bool:
        """Return whether this tree contains <item>.

        >>> t = Tree(1, [Tree(-2, []), Tree(10, []), Tree(-30, [])])
        >>> t.__contains__(-30)  # Could also write -30 in t.
        True
        >>> t.__contains__(148)
        False
        """
        if self.is_empty():  # If root is None return False
            return False
        occurs = False  # Occurs flag set to false
        if self._root == item:  # If the root of the current node is equal to the item
            return True  # Item is in the tree => return True

        for subtree in self._subtrees:
            # if self._root == item (it is contained)
            if subtree.__contains__(item):
                # Change the occurs flag to True
                occurs = True
                break
        return occurs

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + str(self._root) + '\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is
                # modified.
                s += subtree._str_indented(depth + 1)
            return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all()
