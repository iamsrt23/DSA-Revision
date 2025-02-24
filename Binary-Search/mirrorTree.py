#User function Template for python3
from collections import deque

class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        
        if root is None:
            return
        
        queue = deque([root])
        
        while queue:
            rootNode = queue.popleft()
            rootNode.left , rootNode.right = rootNode.right,rootNode.left
            
            if rootNode.left:
                queue.append(rootNode.left)
            if rootNode.right:
                queue.append(rootNode.right)
                
    
    def levelorder(root):
        if root is None:
            return
        
        queue = deque([root])
        res = []
        
        while queue:
            rootNode = queue.popleft()
            res.append(rootNode.data)
            
            if rootNode.left:
                queue.append(rootNode.left)
            if rootNode.right:
                queue.append(rootNode.right)

        return res            
        
        
        


