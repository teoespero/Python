# if else if statements in Python
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

yourAge = 19

if yourAge < 4:
    ticketPrice = 0
elif yourAge < 18 or yourAge >= 65:
    ticketPrice = 5
else:
    ticketPrice = 10

print('ticket price based on age (' + str(yourAge) + ') is $'+str(ticketPrice)+'.')