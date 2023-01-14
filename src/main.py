# Create a class for content aggregation
from functools import reduce

class ContentAggregator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        return reduce(lambda x, y: x*y, args)




# Path: src/main.py
