class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for i in range(len(nums))]
        frequency_dict = {}
        result = []
        for i in nums:
            frequency_dict[i] = 1 + frequency_dict.get(i, 0)
        for i, fq in frequency_dict.items():
            frequency[fq-1].append(i)
        for i in range(len(nums)-1, -1, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result
