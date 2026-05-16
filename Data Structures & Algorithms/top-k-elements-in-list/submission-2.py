from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elements =  Counter(nums)
        elements = elements.most_common(k)

        result = []
        for x,y in elements:
            result.append(x)

        return result


        


        

       
        