class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        for i in range(len(digits)-1, 0, -1):
            if digits[i] == 9:
                digits[i] = 0
            else: 
                digits[i] += 1
                return digits
        if digits[0] == 9:
            return [1] + [0]*len(digits)
        digits[0] += 1
        return digits
