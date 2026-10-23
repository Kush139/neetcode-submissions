class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_p = s[0]

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]

                if substring == substring[::-1]:
                    if len(max_p) < len(substring):
                        max_p = substring

        return max_p