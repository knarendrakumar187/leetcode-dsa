class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = sorted(Counter(s).items())
        h = "".join(c * (k // 2) for c, k in counts)
        m = "".join(c * (k % 2) for c,k in counts)

        return h + m + h[::-1]