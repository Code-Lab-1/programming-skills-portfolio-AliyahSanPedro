age = input("How old are you? ")
age = int(age)
if age < 3:
     print("ticket is free.")
elif age >= 3 and age <= 12:
     print("Your ticket is $10")
elif age > 12:
     print("Your ticket is $15")