class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        
        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix