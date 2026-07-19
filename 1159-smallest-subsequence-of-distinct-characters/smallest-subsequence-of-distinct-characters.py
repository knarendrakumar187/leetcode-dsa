class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = [0] * 26
        seen = [False] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        res = []

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] -= 1

            if seen[idx]:
                continue

            while res and res[-1] > ch and freq[ord(res[-1]) - ord('a')] > 0:
                seen[ord(res[-1]) - ord('a')] = False
                res.pop()

            res.append(ch)
            seen[idx] = True

        return "".join(res)