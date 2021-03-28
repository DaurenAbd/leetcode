BITS = 15

def get_bit(num: int, i: int) -> int:
    return (num >> i) & 1        
        
class TrieNode:
    def __init__(self, bit: int):
        self.bit = bit
        self.count = 1
        self.link = [None, None]
    
    def add(self, num: int):
        node = self
        for i in range(BITS - 1, -1, -1):
            bit = get_bit(num, i)
            if node.link[bit] is None:
                node.link[bit] = TrieNode(bit)
            else:
                node.link[bit].count += 1
            node = node.link[bit]
            
    def dfs(self, num: int, high: int):
        node = self
        answer = 0
        
        for i in range(BITS - 1, -1, -1):   
            if node is None:
                break
            
            x, y = get_bit(num, i), get_bit(high, i)

            if (x, y) == (0, 1):
                if node.link[0] is not None:
                    answer += node.link[0].count
                node = node.link[1]
            elif (x, y) == (1, 1):
                if node.link[1] is not None:
                    answer += node.link[1].count
                node = node.link[0]
            elif (x, y) == (0, 0):
                node = node.link[0]
            elif (x, y) == (1, 0):
                node = node.link[1]
                
        return answer
        
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        root = TrieNode(None)
        answer = 0
        for i, num in enumerate(nums):
            answer += root.dfs(num, high + 1)
            answer -= root.dfs(num, low)
            root.add(num)
        return answer

    
    # 1. (low, high) -> high
    # 2. bit by bit  
#     class DS:
#         def __init__(self):
#             self.nums = []
            
#         def add(self, e: int):
#             self.nums.append(e)
            
#         def count(self, x: int, high: int) -> int:
#             cnt = 0
#             for e in self.nums:
#                 if e ^ x <= high:
#                     cnt += 1
#             return cnt
    
#     ds = DS()
#     answer = 0
    
#     for e in nums:
#         answer += DS.count(e, high) - DS.count(e, low - 1)
#         DS.add(e)
        
#     return answer
    
