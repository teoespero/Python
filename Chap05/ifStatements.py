# if statements in Python
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# define an empty list
cars = []

# populate our list
cars.append('bmw')
cars.append('audi')
cars.append('subaru')
cars.append('toyota')

# print our list
for car in cars:
    # upper case specific brands
    if (car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())

# check if brand is already there
newcarbrand = 'BMW'

if (newcarbrand.lower() in cars):
    print('Car brand already listed')
else:
    cars.append(newcarbrand)

newcarbrand = 'mercedez'
if (newcarbrand.lower() in cars):
    print('car brand already listed')
else:
    cars.append(newcarbrand)
    print('car has been added')
    # print our list
    for car in cars:
        # upper case specific brands
        if (car == 'bmw'):
            print(car.upper())
        else:
            print(car.title())
