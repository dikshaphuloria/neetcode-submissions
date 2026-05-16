from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elements =  Counter(nums)
        elements = elements.most_common()

        result = []
        n, i = len(elements), 0

        while i!=k:
            result.append(elements[i][0])
            i+=1

        return result
           


        

       
        