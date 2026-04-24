class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge case for overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Work with positive numbers
        dvd, dvs = abs(dividend), abs(divisor)
        result = 0
        
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dvd -= temp
            result += multiple
        
        return sign * result