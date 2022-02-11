"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#429. N-ary Tree Level Order Traversal
#https://leetcode.com/problems/n-ary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        out = []
        currentlevel = [root]
        
        while currentlevel:
            nextlevel = []
            currentlist = []
            for n in currentlevel:
                currentlist.append(n.val)
                if n.children:
                    for i in n.children:
                        nextlevel.append(i)
                    
            out.append(currentlist)
            currentlevel = nextlevel
        return out
