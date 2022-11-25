sandwich_orders = ['Chicken Sandwich', 'Pastarami', 'Beef Sandwich','Vegetables Sanwich','Pastarami', 'Zinker Sandwich', 'Pastarami']
finishedsandwiches = []

print("I'm sorry, we're all out of Pastrami today.")
while 'Pastarami' in sandwich_orders:
    sandwich_orders.remove('Pastarami')
    print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Preparing your {current_sandwich}")
    finishedsandwiches.append(current_sandwich)

print("\n")
for sandwich in finishedsandwiches:
    print(f"{sandwich} is ready.")