class Solution:
    def kthSmallest(self, root, k):

        stack = []          # Stack to store nodes
        cur = root          # Start from the root
        count = 0           # Counts visited nodes

        # Continue until there are no nodes left
        while cur or stack:

            # Go to the leftmost node
            while cur:
                stack.append(cur)   # Save current node
                cur = cur.left      # Move left

            # Leftmost node reached
            cur = stack.pop()       # Visit the top node

            count += 1              # Increase visited node count

            # If this is the kth visited node
            if count == k:
                return cur.val

            # Now visit the right subtree
            cur = cur.right