# Slicing Through an Entire List
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# define the list that we want
diecast_cars = ['hotwheels','johnny lightning', 'greenlight', 'matchbox', 'tomica']

# print the initial list
print('print the initial list')
print(diecast_cars)
print('--------------------------------------------------------------------')

# show first 3
print('show first 3')
print(diecast_cars[0:3])
print('--------------------------------------------------------------------')

# insert a brand
newbrand = 'kyosho'
print('insert a brand ', newbrand)
diecast_cars.insert(0,newbrand)
print('--------------------------------------------------------------------')

# print the new list
print('print the new list')
print(diecast_cars)
print('--------------------------------------------------------------------')

# show first 3
print('show first 3')
print(diecast_cars[0:3])
print('--------------------------------------------------------------------')

# show 3rd element to the end
print('show 3rd element to the end')
print(diecast_cars[3:])
print('--------------------------------------------------------------------')

# show first 3 brands
print('show first 3 brands')
for brands in diecast_cars[:3]:
    print(brands)
print('--------------------------------------------------------------------')

# show last 3 brands
print('show last 3 brands')
for brands in diecast_cars[3:]:
    print(brands)