def linear(n: int) -> int:
    return n * (n + 1) // 2

def linear_range(L: int, R: int) -> int:
    return linear(R) - linear(L - 1)

def get_how_much_sum_is_needed_to_get_x_at_index(n: int, x: int, index: int) -> int:
    left = linear_range(max(1, M - index), M)
    right = linear_range(max(1, M + index + 1 - n), M - 1)
    return left + right


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if maxSum < n:
            return 0
        
        maxSum -= n
        
        answer = 0
        L = 0
        R = maxSum
        
        while L <= R:
            M = (L + R) // 2
            if get_how_much_sum_is_needed_to_get_x_at_index(n, M, index) <= maxSum:
                answer = M
                L = M + 1
            else:
                R = M - 1   
                
        L = 0
        R = len(nums) - 1
        answer = -1
        
        while L <= R:
            M = (L + R) // 2
            if nums[M] == x:
                answer = M
                R = M - 1
            else:
                L = M + 1
            
        return answer + 1
    
#    v
#  0 0 0 0 0 0
#    x
# how_much_sum_is_needed_to_get_x_at_index(n, x, index)
# 
