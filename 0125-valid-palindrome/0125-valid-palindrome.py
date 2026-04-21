class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = "".join(filter(str.isalnum, s)).lower()
        reverse_s = s[::-1]
        if s == reverse_s:
            return True
        else:
            return False