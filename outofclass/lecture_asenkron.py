#base
numberOfBook=60
discount=0.4
priceOfBook=24.95
shippingFirstCost = 3
shippingAdditionalCost = 0.75
#book price
withDiscount=(priceOfBook)*(1-discount) #with %40 discount
totalPrice=withDiscount * numberOfBook #==> total price of 60 book
#shipping price
totalShippingCost = shippingFirstCost + shippingAdditionalCost*(numberOfBook-1)
#wholesale
totalWholeSale = totalPrice + totalShippingCost

print(totalWholeSale)






                       
