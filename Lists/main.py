diecast_cars = ['Hotwheels', 'Matchbox', 'Johnny Lightning', 'Greenlight', 'Tomica']
print('Initial list: ', diecast_cars)

del diecast_cars[0]
print('Deleting 0th element', diecast_cars)

diecast_cars.append('Hotwheels')
print('Adding an element to the end: ', diecast_cars)

diecast_brand = diecast_cars.pop()
print('Popping the last element: ', diecast_cars)
print('Popped element: ', diecast_brand)


diecast_brand = diecast_cars.pop(0)
print('Popping a specific element: ', diecast_cars)

diecast_cars.remove('Greenlight')
print('Removing a specific element: ', diecast_brand)

diecast_cars.insert(1,'Greenlight')
print('Inserting an element at a specific point: ', diecast_cars)

diecast_cars.sort()
print('Sorted ascending order: ', diecast_cars)

diecast_cars.sort(reverse=True)
print('Sorted descending order: ', diecast_cars)

print('List length: ', len(diecast_cars))