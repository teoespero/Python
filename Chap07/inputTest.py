# a dictionary of lists
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# get a message the user wants to display
message = input("tell me something, and i will repeat it to you: ")

# get the name and year of birth
yourName = input('enter your name: ')
yearofbirth = int(input('Your year of birth: '))


# compute for the age
yourage = 2022 - yearofbirth

# greet the user with the custom message
print(message + ' ' + yourName)

# provide his current age
# and the rights they has under that age
print('you are now ' + str(yourage) + ' years old.')
if (yourage >= 18):
    print('you can vote')
if (yourage >= 21):
    print('you can buy alcohol')
if (yourage >= 65):
    print('you are now retired')

# eof