class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        order = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in order:
                return [order[remainder], i]
            else:
                order[nums[i]] = i