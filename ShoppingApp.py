# @@@@@@@@@@@@  SHOPPING APP @@@@@@@@@@@@
from os import system, name

def clear():
    if name == 'nt':
        system('cls')

def food_menu():
    print('Today\'s current food menu is:')
    for index, item in list(enumerate(food)):
        print(index,'.', item, '-', menus['food'][index])

def beverage_menu():
    print('The available beverages are:')
    for index, item in list(enumerate(beverages)):
        print(index, '.', item, '-', menus['beverages'][index])

# Menu - Choices

food = ['Spaghetti', 'Burger', 'Chicken', 'Hotdog']
beverages = ['Waterbottle', 'Softdrinks', 'Juice', 'Smoothies']

menus = {'food': {0: 3.25, 1: 4.75, 2: 3.5, 3: 1.25},
         'beverages': {0: 0.99, 1: 1.5, 2: 1.25, 3: 2.25}}
# Welcome Message
print('Welcome to ABC\'s Mini Cafeteria!')
user_input = (input('Would you like to see today\'s menu? [Y/n]\n>'))
clear()
if user_input.upper() == 'Y':
    clear()
else:
    ('Thank you come again!')
    clear()

# Get User Input
print('Currently getting your order...')
while True:
    food_menu()
    print('Please pick the number of your food:')
    try:
        user_food = int(input('> '))
        if user_food > (len(food) - 1):
            print('Choice out of range. Restarting your order..')
            clear()
            continue
    except ValueError:
        print('That is not a valid number. Restarting your order..')
        clear()
        continue

    clear()
    beverage_menu()
    print('Please pick the number of your beverage:')
    try:
        user_beverage = int(input('> '))
        if user_beverage > (len(beverages) - 1):
            print('Choice out of range. Restarting your order..')
            clear()
            continue
    except ValueError:
        print('That is not a valid number. Restarting your order..')
        clear()
        continue

    else:
        break
print('You ordered {} and {}.'.format(food[user_food], beverages[user_beverage]))




# Get User Input (Validate User Input - Except & try)
# Get User-Input Category
# Get Customer Purchase
# Write Customer Purchased to a database file
# Add Customer name to a Database File
# Get Customer Reward Card ID
# Validate Customer Reward Card ID (Exist not Exist)
# Compute Customer Point Reward (Every 100 == 1 Pts)
# Add Process here
# _______________
# _______________
# _______________
# _______________
# _______________

# End - Print Purchased Item
# End - Print Points Reward

