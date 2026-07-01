prices = [135, -345, 785, 0, 250, -100, 500]
mprices = [i if i > 0 else 0 for i in prices]
print(mprices)