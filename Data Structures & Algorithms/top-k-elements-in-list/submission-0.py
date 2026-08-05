class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[i]:
        return [nums[0] for nums in Counter(nums).most_common(k)]
            