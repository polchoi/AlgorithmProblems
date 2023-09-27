class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []

        if len(nums) == 1:
            return [nums[:]]
        else:
            for i in nums:
                x = nums.pop(0)
                permuted = self.permute(nums)
                for j in permuted:
                    j.append(x)
                    permutation.append(j)
                nums.append(x)
        return permutation
