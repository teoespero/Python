# a sample dictionary in python
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# create a sample dictionary
print('\ncreate a sample dictionary\n')
my_car = {
    'brand' : 'nissan',
    'color' : 'platinum',
    'model' : 'rogue',
    'year' : 2014
}
print(my_car)
print('\n------------------------------------------------------------------------------')

# access some of my car attributes
print('\naccess some of my car attributes\n')
print(my_car['color'])
print(my_car['model'])
print('\n------------------------------------------------------------------------------')

# add new attributes
print('\nadd new attributes\n')
my_car['sub-model'] = 'sv'
print(my_car)
print('\n------------------------------------------------------------------------------')

# change an attribute
print('\nchange an attribute\n')
my_car['color'] = 'grey'
print(my_car)
print('\n------------------------------------------------------------------------------')

# add a new attribute
print('\nadd a new attribute\n')
my_car['mileage'] = 103367
print(my_car)
print('\n------------------------------------------------------------------------------')

# delete an attribute
print('\ndelete an attribute\n')
del my_car['sub-model']
print(my_car)
print('\n------------------------------------------------------------------------------')

# display the fields
print('\ndisplay the fields\n')
for field in my_car.keys():
    print(field)
print('\n------------------------------------------------------------------------------')

# display the data
print('\ndisplay the data\n')
for data in my_car.values():
    print(data)
print('\n------------------------------------------------------------------------------')


# loop through the dictionary
print('\nloop through the dictionary\n')
for field, data in my_car.items():
    print(field,': ' + str(data))
print('\n------------------------------------------------------------------------------')


# eof