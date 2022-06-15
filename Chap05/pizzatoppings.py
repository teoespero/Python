# if with lists
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# create our list for toppings
pizza_toppings = []

# populate our available toppings list
pizza_toppings.append('mushrooms')
pizza_toppings.append('green bell pepper')
pizza_toppings.append('cheeze')
pizza_toppings.append('extra cheeze')
pizza_toppings.append('pepperoni')
pizza_toppings.append('ham')
pizza_toppings.append('pineapple')
pizza_toppings.append('chicken')
pizza_toppings.append('bacon')
pizza_toppings.append('anchovies')

# print our available toppings list
print('available toppings')
for pizza_topping in pizza_toppings:
    print(pizza_topping)
print('\n------------------------------------------------')

# populate our user requested toppings
requested_toppings = []
requested_toppings.append('mushrooms')
requested_toppings.append('green bell pepper')
requested_toppings.append('cheeze')
requested_toppings.append('extra cheeze')
requested_toppings.append('ham')
requested_toppings.append('pork')

# print our user requested toppings list
print('requested toppings')
for requested_topping in requested_toppings:
    print(requested_topping)
print('\n------------------------------------------------')


# final pizza make
pizza_final = []

# check if requested topping is available
for requested_topping in requested_toppings:

    # if yes, add it
    if requested_topping in pizza_toppings:
        print('adding ', requested_topping)
        pizza_final.append(requested_topping)

    # otherwise, say it's not available
    else:
        print('sorry ', requested_topping, 'is not available')

# prep final pizza
my_toppings = ''
delimiter = ', '
for pizza_make in pizza_final:
    if (pizza_make == pizza_final[-1]):
        delimiter = ''
    elif pizza_make == pizza_final[-2]:
        delimiter = ' and '
    my_toppings =  my_toppings + str(pizza_make) + delimiter

# deliver pizza
print('\n------------------------------------------------')
print('finished making your ', my_toppings, 'pizza.')
print('bon-a-petit')

# eof
