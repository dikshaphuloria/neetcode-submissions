class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = {}

        for val in strs:
            char_val = "".join(sorted(val))

            if char_val not in my_dict:
                my_dict[char_val] = []

            my_dict[char_val].append(val)

        
        return list(my_dict.values())

            




        