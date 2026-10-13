class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store_val = defaultdict(list)

        for s in strs:
            key_str = ('').join(sorted(s))

            store_val[key_str].append(s)

        return list(store_val.values())

            
        