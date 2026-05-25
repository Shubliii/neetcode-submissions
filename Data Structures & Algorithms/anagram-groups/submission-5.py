

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for w in strs:

            # Create frequency array
            count = [0] * 26

            # Count characters
            for c in w:
                count[ord(c) - ord("a")] += 1

             ##convert list to tuple , Because Python dictionaries CANNOT use lists as keys. 
            ans[tuple(count)].append(w)

        return list(ans.values())





