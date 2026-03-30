# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def postorder(self, root):
        if root is None :
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.postorder(root)
        return self.ans



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self):
#         self.ans = []
#     def preorder(self, root):
#         if root is None :
#             return
        
#         self.ans.append(root.val)
#         self.preorder(root.left)
#         self.preorder(root.right)


#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         self.ans = []
#         self.preorder(root)
#         return self.ans