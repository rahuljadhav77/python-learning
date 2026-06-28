# Day 79: Dictionary Mapping
prices = {'apple': 0.5, 'banana': 0.3}
stock = {'apple': 10, 'banana': 20}
total_value = sum(prices[k] * stock[k] for k in prices)
print(f'Total stock value: ${total_value:.2f}')
