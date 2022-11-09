original_prices = [-12, 3, 5, -2, 1]
temp_prices = original_prices[:]
last_prices = [price if price > 0 else 0 for price in temp_prices]
print(original_prices)
print(last_prices)