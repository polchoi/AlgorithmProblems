class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in strs:
            sorted_i = str(sorted(i))
            if sorted_i not in groups:
                groups[sorted_i] = []
            groups[sorted_i].append(i)
        return groups.values()
