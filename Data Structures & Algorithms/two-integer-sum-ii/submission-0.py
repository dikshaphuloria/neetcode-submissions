class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}

        for i,num in enumerate(numbers):
            if target - num in my_dict:
                return [my_dict[target - num]+1, i+1]
            
            my_dict[num] = i



            