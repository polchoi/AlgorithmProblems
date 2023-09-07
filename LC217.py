class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for i in nums:
            num_count[i] = 1 + num_count.get(i, 0)
            if num_count[i] > 1:
                return True
        return False