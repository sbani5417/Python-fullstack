product_prices=(400,200,100,300)
print("product_prices:",product_prices)
try:
  product_prices[1]=250
except TypeError:
  print("tuple value cannot be modified")
print("price of product3:",product_prices[3])
