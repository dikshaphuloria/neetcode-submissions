class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_dict = {}
        for num in nums:
            val_dict[num] = 1 + val_dict.get(num, 0)

        val_list = []
        for key, value in val_dict.items():
            val_list.append((value, key))

        val_list.sort()

        ans = []

        while k:
            ans.append(val_list.pop()[1])
            k-=1

        return ans

        