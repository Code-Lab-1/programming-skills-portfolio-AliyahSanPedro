sandwichorders = ['Chicken Sandwich', 'Beef Sandwich', 'vegetables Sanwich', 'Zinker Sandwich']
finishedsandwiches = []

while sandwichorders:
    currentsandwich = sandwichorders.pop()
    print(f"Preparing your {currentsandwich}")
    finishedsandwiches.append(currentsandwich)

print("\n")
for sandwich in finishedsandwiches:
    print(f"{sandwich} is ready.")
