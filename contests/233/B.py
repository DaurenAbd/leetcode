class Backlog:
    def __init__(self):
        self.sell_heap = []
        self.buy_heap = []
        
    def buy(self, buy_price: int, buy_amount: int):
        while buy_amount > 0 and self.sell_heap:
            sell_price, sell_amount = self.sell_heap[0]
            
            if sell_price > buy_price:
                break
                
            x = min(buy_amount, sell_amount)
            
            buy_amount -= x
            sell_amount -= x
            
            if sell_amount == 0:
                heapq.heappop(self.sell_heap)
            else:
                heapq.heapreplace(self.sell_heap, (sell_price, sell_amount))
        
        if buy_amount > 0:
            heapq.heappush(self.buy_heap, (-buy_price, buy_amount))
    
    def sell(self, sell_price: int, sell_amount: int):
        while sell_amount > 0 and self.buy_heap:
            buy_price, buy_amount = (-self.buy_heap[0][0], self.buy_heap[0][1])
            
            if sell_price > buy_price:
                break
                
            x = min(buy_amount, sell_amount)
            
            buy_amount -= x
            sell_amount -= x
            
            if buy_amount == 0:
                heapq.heappop(self.buy_heap)
            else:
                heapq.heapreplace(self.buy_heap, (-buy_price, buy_amount))
        
        if sell_amount > 0:
            heapq.heappush(self.sell_heap, (sell_price, sell_amount))
    
    def count_backlog(self) -> int:
        return (sum(sell_amount for _, sell_amount in self.sell_heap) + 
                sum(buy_amount for _, buy_amount in self.buy_heap)) 

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        backlog = Backlog()
        for price, amount, order_type in orders:
            if order_type == 0:
                backlog.buy(price, amount)
            else:
                backlog.sell(price, amount)
        return backlog.count_backlog() % (10**9 + 7)
