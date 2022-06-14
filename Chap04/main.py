# Looping Through an Entire List
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# define the list that we want
diecast_cars = ['hotwheels','johnny lightning', 'greelight', 'matchbox', 'tomica']

# create a loop and go through each one
for car_brands in diecast_cars:
    print(car_brands.title())

# add a new car brand to the list
newCar = 'kyosho'
print('---------------------------------')
print('add a new car brand to the list', newCar)
diecast_cars.append(newCar)

print('---------------------------------')
print('Sort the list alphabetically')
diecast_cars.sort()

# create a loop and go through each one
print('---------------------------------')
for car_brands in diecast_cars:
    print(car_brands.title())