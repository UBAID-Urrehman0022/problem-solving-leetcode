class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            #i = 1==>flower will be compared
            for s in strs: #for s= 0 compares 1st(flower )with and 1 and 2
                if i == len(s) or strs[0][i] !=s[i]:
                    return res
            res += strs[0][i]
        return res
       