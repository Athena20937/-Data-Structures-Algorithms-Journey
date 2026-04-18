class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        first_char = strs[0]
        last_char = strs[-1]

        common_prefix = []

        for i in range (min(len(first_char),len(last_char))):
            if first_char[i] != last_char[i]:
                break
            common_prefix.append(first_char[i])
        return "".join(common_prefix)        
    