class Solution:
    def plusOne(self,digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i > -1:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                if i != 0:
                    digits[i] = 0
                else:
                    digits[i] = 0
                    digits.insert(0,1)
                    return digits
            i -= 1
        return digits