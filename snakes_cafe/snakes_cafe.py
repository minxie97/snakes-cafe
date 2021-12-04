#Thank you user52028778 on Stack Overflow for showing me Counter
from collections import Counter

#intro message
intro = '''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
'''

#menu
menu = {
    'Appetizer': ['Wings', 'Cookies', 'Spring Rolls'],
    'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    'Desserts': ['Ice Cream', 'Cake', 'Pie'],
    'Drinks': ['Coffee', 'Tea', 'Unicorn Tears']
}

#order message
order_message = '''***********************************
** What would you like to order? **
***********************************'''

#print intro, menu, and order message
print(intro)

for key, values in menu.items():
    print(key + '\n' + '------')
    for item in values:
        print(item)
    print('\n', end='')

print(order_message)

#order input

ordering = True
full_order = []
available = False
complete_order = Counter(full_order)

while ordering:
    order = input('> ')

    if order == 'quit':
        print('Your total order:')
        for key, value in Counter(full_order).items():
            print(f'{value}x {key}')
        ordering = False
        break

    for categories in menu.values():
        if order in categories:
            full_order.append(order)
            available = True
            print(f'** {full_order.count(order)} order of {order} have been added to your meal **')

    if available == False: 
        print(f'Sorry! We don\'t have {order} here!')

    available = False