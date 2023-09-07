class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for i in s:
            if i.isalnum():
                clean_s += i.lower()
        l, r = 0, len(clean_s)-1
        while l < r:
            if clean_s[l] == clean_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
