class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            reverse_num = int(str(x)[::-1])
            if reverse_num == x:
                return True
            else:
                return False


            

            
