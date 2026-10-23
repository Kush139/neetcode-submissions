class Solution:
    def longestPalindrome(self, s: str) -> str:
        #dp[i] = palindrome length at that index

        max_len = 1
        res = s[0]
        for i in range(len(s)):
            # odd case
            l, r = i-1, i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            len_sub = r-l+1
            if len_sub > max_len:
                max_len = len_sub
                res = s[l:r+1]

            #even case
            l, r = i, i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            len_sub = r-l+1
            if len_sub > max_len:
                max_len = len_sub
                res = s[l:r+1]
        return res

        

            
            
