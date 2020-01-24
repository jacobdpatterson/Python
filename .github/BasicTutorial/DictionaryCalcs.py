stocks = {'GOOG' : 520.54, 'FB' : 76.54, 'YHOO' : 39.28 , 'AMZN' : 306.21, 'AAPL' : 99.76}

print(min(stocks)) # - Returns AAPL, the key minimum value, not the lowest-priced stock. We want YHOO.

# - Create a new list with Zip, this switches the order of the key and value (520, GOOG)

min_price = min(zip(stocks.values(), stocks.keys())) # - Puts values first and keys second.

print(min_price) # - Now YHOO is returned like we want. 