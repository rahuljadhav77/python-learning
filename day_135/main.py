# Day 135: List Comprehensions
numbers = range(1, 11)
squares = [x**2 for x in numbers if x % 2 == 0]
print(f'Even squares: {squares}')
