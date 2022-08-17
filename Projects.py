import time
print('XXXXXXX POS Machine XXXXXXXXX')
print('''
Welcome to ShadyExpress supermarket. Thank you for your patronage
''')
time.sleep(3)
available_items = [
    {'Fruit type': 'Mango', 'Quantity available': 20, 'Average wieght (g)': 400, 'Price per unit (N)': 200},
    {'Fruit type': 'Orange', 'Quantity available': 40, 'Average wieght (g)': 200, 'Price per unit (N)': 50},
    {'Fruit type': 'Pineapple', 'Quantity available': 12, 'Average wieght (g)': 12, 'Price per unit (N)': 500},
    {'Fruit type': 'Lemon', 'Quantity available': 33, 'Average wieght (g)': 100, 'Price per unit (N)': 50},
    {'Mango': 20, 'Orange': 40, 'Pineapple': 12, 'Lemon': 33},
]
time.sleep(3)
selected_item = []
while (len(selected_item)<=5):
    print(f' These are the available fruits and quantities: {available_items}')
    selectFruit = input('Please type the fruit you want to purchase: ')
    selectFruit= selectFruit.capitalize()
    time.sleep(2)
    if selectFruit == 'Mango':
        print(available_items[0])
        selectQuantity = int(input('How many mangoes do you want?: '))
        if selectQuantity >= available_items[0]['Quantity available']:
            print('Quantity not available')
        else:
            selected_item.append('Mango')
            print(selected_item)
            print(f'{selectQuantity} mango(es) added to your chart, {len(selected_item)} fruits requested')
            again = input('Do you want to buy another fruit?: ')
            again2 = again.capitalize()
            if again2 == 'No':
                print(f'{selected_item} fruit was bought. Thanks for your patronage')
            elif again2=='Yes':
                print(available_items)
            else:
                print('Invalid command')
    elif selectFruit == 'Orange':
        print(available_items[1])
        selectQuantity = int(input('How many oranges do you want?: '))
        if selectQuantity >=available_items[1]['Quantity available']:
            print('Quantity not available')
        else:
            selected_item.append('Orange')
            print(selected_item)
            print(f'{selectQuantity} Orange(s) added to chart')
            again = input('Do you want to buy another fruit?: ')
            again2 = again.capitalize()
            if again2 == 'No':
                print(f'{selected_item} fruit was bought. Thanks for your patronage')
            elif again2=='Yes':
                print(available_items)
            else:
                print('Invalid command')
    elif selectFruit == 'Pineapple':
        print(available_items[2])
        selectQuantity = int(input('How many pineapples do you want?: '))
        if selectQuantity >=12:
            print('Quantity not available')
        else:
            selected_item.append('Pineapple')
            print(selected_item)
            print(f'{selectQuantity} of Pineapple(s) added to chart')
            again = input('Do you want to buy another fruit?: ')
            again2 = again.capitalize()
            if again2 == 'No':
                print(f'{selected_item} fruit was bought. Thanks for your patronage')
            elif again2=='Yes':
                print(available_items)
            else:
                print('Invalid command')
    elif selectFruit == 'Lemon':
        print(available_items[3])
        selectQuantity = int(input('How many lemon(s) do you want?: '))
        if selectQuantity >=50:
            print('Quantity not available')
        else:
            selected_item.append('Lemon')
            print(selected_item)
            print(f'{selectQuantity} lemon(s) added to chart')
            again = input('Do you want to buy another fruit?: ')
            again2 = again.capitalize()
            if again2 == 'No':
                print(f'{selected_item} fruit was bought. Thanks for your patronage')
            elif again2=='Yes':
                print(available_items)
            else:
                print('Invalid command')

    else:
        print('Fruit requested not available. Thank you')

else:
    print('Maximum number of fruits reached')
# again = input('Do you want to buy another fruit?: ')
# again2 = again.capitalize()
# if again2 == 'No':
print(f'{selected_item} fruit was bought. Thanks for your patronage')
# elif again2=='Yes':
#     print(available_items)
# else:
#     print('Invalid command')