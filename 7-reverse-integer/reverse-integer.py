class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        
        reversed_num = int(str(num)[::-1])
        
        reversed_num = reversed_num if x >= 0 else -reversed_num

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        else:
            return reversed_num
