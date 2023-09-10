class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle):
                    if i + j == len(haystack):
                        return -1
                    elif haystack[i+j] == needle[j]:
                        j += 1
                    else:
                        break
                if j == len(needle):
                    return i
        return -1
