# Creating Tuples
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# define the tuple that we want
my_diecast_cars = (
                   'hotwheels',
                   'johnny lightning',
                   'greelight',
                   'matchbox',
                   'tomica'
            )

# print our tuple
print(my_diecast_cars)

# print individual elements
print('my tuple')
for index in range(0,len(my_diecast_cars)):
    print(index, '.', my_diecast_cars[index])
print('------------------------------------------')

# print their tuple
their_tuple = (
                    'kyosoho',
                    'maisto',
                    'kinsmart',
                    'candylabs',
                    'hotwheels',
                    'johnny lightning',
                    'greelight',
                    'matchbox',
                    'tomica'
            )

print('their tuple')
for cars in their_tuple:
    print(cars)
print('------------------------------------------')

# overwrite my tuple
my_diecast_cars = their_tuple

print('my new tuple')
for index in range(0,len(my_diecast_cars)):
    print(index, '.', my_diecast_cars[index])
print('------------------------------------------')

