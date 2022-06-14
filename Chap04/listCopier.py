# Copying a List
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# define the list that we want
my_diecast_cars = ['hotwheels','johnny lightning', 'greelight', 'matchbox', 'tomica']

# define the new list base on our current list
top_diecast_car_brands = my_diecast_cars[:]

# show our list
print('show our list')
for mycars in my_diecast_cars:
    print('\t',mycars)
print('total cars: ', len(my_diecast_cars))
print('--------------------------------------------------------------------------------------------')


# show their list
print('show their list')
for theircar in top_diecast_car_brands:
    print('\t',theircar)
print('total cars: ', len(top_diecast_car_brands))
print('--------------------------------------------------------------------------------------------')

# add brands that we have
my_diecast_cars.append('kyosho')
my_diecast_cars.append('maisto')
my_diecast_cars.append('kinsmart')
my_diecast_cars.append('welly')

# show our list
print('show our list')
for mycars in my_diecast_cars:
    print('\t',mycars)
print('total cars: ', len(my_diecast_cars))
print('--------------------------------------------------------------------------------------------')


# add brands that they have
top_diecast_car_brands.append('kyosho')
top_diecast_car_brands.append('maisto')
top_diecast_car_brands.append('kinsmart')
top_diecast_car_brands.append('welly')
top_diecast_car_brands.append('Bburago')
top_diecast_car_brands.append('Amalgam')
top_diecast_car_brands.append('Exoto')
top_diecast_car_brands.append('MR Collection')
top_diecast_car_brands.append('CMC')
top_diecast_car_brands.append('BBR')

# show their list
print('show their list')
for theircar in top_diecast_car_brands:
    print('\t',theircar)
print('total cars: ', len(top_diecast_car_brands))
print('--------------------------------------------------------------------------------------------')

# copy the brands they have to our list
print('copy the brands they have to our list')
for theircar in top_diecast_car_brands:
    if (theircar not in my_diecast_cars):
        print('\tadding ', theircar)
        my_diecast_cars.append(theircar)
print('--------------------------------------------------------------------------------------------')


# show our list
print('show our new list')
for mycars in my_diecast_cars:
    print('\t',mycars)
print('total cars: ', len(my_diecast_cars))
print('--------------------------------------------------------------------------------------------')




