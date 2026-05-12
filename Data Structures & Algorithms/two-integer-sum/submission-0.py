class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_dict = {}

        for i,num in enumerate(nums):
            if target - num in pair_dict:
                return [pair_dict[target - num], i]
            
            pair_dict[num] = i

            



        