class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_dict = defaultdict(list)

        for val in strs:
            s = "".join(sorted(val))
            anagrams_dict[s].append(val)

        return list(anagrams_dict.values())


        