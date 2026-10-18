class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store_val = defaultdict(list)

        for s in strs:
            val = ('').join(sorted(s))

            store_val[val].append(s)

        return list(store_val.values())



        

            
        