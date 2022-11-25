money = int(input("One USB stick costs £6, enter your money "))
cost = int(6)
solution = money//cost
confirm = int(1)
if solution == (8) :
    money = (input("the total of 8 USB sticks cost £48, are you sure you want to purchase, type yes if you are sure and no if not "))
    if money == "yes": 
        print("You have successfully purchased 8 USB sticks and your change is £2")
    else: 
        print("The transaction is cancelled")