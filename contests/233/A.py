class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = -math.inf
        current = -math.inf
        previous = math.inf
        
        for num in nums:
            if num <= previous:
                answer = max(answer, current)
                current = 0
            current += num
            previous = num
        
        return max(answer, current)
