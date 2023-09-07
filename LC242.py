class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_content = {}
            t_content = {}
            for i in s:
                s_content[i] = 1 + s_content.get(i, 0)
            for j in t:
                t_content[j] = 1 + t_content.get(j, 0)
            return s_content == t_content