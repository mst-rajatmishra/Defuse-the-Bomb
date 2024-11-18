from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n  # Initialize the result array with zeros
        
        if k == 0:
            return result  # If k == 0, all elements are zeroed out
        
        # Loop through each index and calculate the sum
        for i in range(n):
            sum_value = 0
            
            if k > 0:
                # Sum the next k elements
                for j in range(1, k + 1):
                    sum_value += code[(i + j) % n]
            
            elif k < 0:
                # Sum the previous |k| elements
                for j in range(1, -k + 1):
                    sum_value += code[(i - j) % n]
            
            result[i] = sum_value
        
        return result
