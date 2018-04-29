# @@@@@@@@@@@@  SHOPPING APP @@@@@@@@@@@@

# Menu - Choices

food = ['Spaghetti', 'Burger', 'Chicken', 'Hotdog']
beverages = ['Waterbottle', 'Softdrinks', 'Juice', 'Smoothies']

menus = {'food': {'spaghetti': 3.25, 'burger': 4.75, 'chicken': 3.5, 'hotdog': 1.25},
         'beverages': {'waterbottle': 0.99, 'softdrinks': 1.5, 'juice': 1.25, 'smoothies': 2.25}}
# Welcome Message
print('Welcome to ABC\'s Mini Cafeteria!')
user_input = (input('Would you like to see today\'s menu? [Y/n]\n>'))
if user_input.upper() == 'Y':
    print('Today\'s current food menu is:')
    for index, item in list(enumerate(food)):
        print(index,'.', item)
    print('The available beverages are:')
    for index, item in list(enumerate(beverages)):
        print(index,'.', item)


# Get User Input


# user_food = input('> ')
# if user_food in food:
#     print(user_food, 'is there.')
# else:
#     print(user_food, 'is not there.')

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

