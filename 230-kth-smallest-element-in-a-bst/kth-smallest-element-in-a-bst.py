class Solution:
    def kthSmallest(self, root, k):
        result=[]
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        return result[k-1]