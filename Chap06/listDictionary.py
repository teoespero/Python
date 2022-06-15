# a list of dictionaries
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# define an empty list of cars
print('\ndefine an empty list of cars\n')
my_cars = []
print(my_cars)
print('-----------------------------------------------------------------------')

# create a nissan model
print('\ncreate a nissan model\n')
nissan = {
    'brand': 'nissan',
    'year' : 2014,
    'color' : 'platinum',
    'model' : 'rogue',
    'mileage' : 103356
}
for key, value in nissan.items():
    print(key, ':', value)
print('-----------------------------------------------------------------------')

# create a toyota model
print('\ncreate a toyota model\n')
toyota = {
    'brand': 'toyota',
    'year' : 2016,
    'color' : 'blue',
    'model' : 'corrolla',
    'mileage' : 85050
}
for key, value in toyota.items():
    print(key, ':', value)
print('-----------------------------------------------------------------------')

# add both cars to my list
print('\nadd both cars to my list\n')
my_cars.append(toyota)
my_cars.append(nissan)
print('-----------------------------------------------------------------------')

# show my cars
print('\nshow my list of cars\n')
for car in my_cars:
    for key, value in car.items():
        print(key, ':', value)
    print('\n')
print('-----------------------------------------------------------------------')

# add a dream car
print('\nadd a dream car\n')
porsche = {
    'brand': 'porsche',
    'year': 1995,
    'color': 'yellow',
    'model': 'boxster',
    'mileage': 150650
}
for key, value in porsche.items():
    print(key, ':', value)
print('-----------------------------------------------------------------------')

# add it to my list of cars
print('\nadd it to my list of cars\n')
my_cars.append(porsche)
print('-----------------------------------------------------------------------')

# show my cars
print('\nshow my new list of cars\n')
for car in my_cars:
    for key, value in car.items():
        print(key, ':', value)
    print('\n')
print('-----------------------------------------------------------------------')

# show car count
print('\nyou have a total of ' + str(len(my_cars)) + ' cars.\n')
print('-----------------------------------------------------------------------')
# eof