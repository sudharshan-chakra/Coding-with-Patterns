"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
You can think of the left and right pointers as synonymous to the predecessor 
and successor pointers in a doubly-linked list. 

For a circular doubly linked list, the predecessor of the first element is the 
last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left 
pointer of the tree node should point to its predecessor, and the right pointer 
should point to its successor. You should return the pointer to the smallest 
element of the linked list.

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.visited = None
        self.first = None

        def inOrder(node):
            if node:
                inOrder(node.left)

                if not self.visited:
                    self.first = node
                    self.visited = node
                else:
                    self.visited.right = node
                    node.left = self.visited
                    self.visited = node

                inOrder(node.right)

        inOrder(root)
        self.first.left = self.visited
        self.visited.right = self.first
        return self.first
            

            
        