class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_copy = set(nums)

        return len(num_copy) != len(nums)
        