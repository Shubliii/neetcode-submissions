class StockSpanner:

    def __init__(self):
        self.stack = []          # stores (price, span)

    def next(self, price: int) -> int:

        span = 1                 # today counts as 1

        # Remove all previous prices that are <= today's price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        # Store today's price and its span
        self.stack.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)