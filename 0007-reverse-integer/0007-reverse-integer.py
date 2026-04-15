class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            reverse_num = -int(str(abs(x))[::-1])
        else:
            reverse_num = int(str(x)[::-1])
        if reverse_num < -2**31 or reverse_num > 2**31 - 1:
            return 0
        return reverse_num 
        
        