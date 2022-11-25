prompt = "\nchoose a topping for your pizza "
prompt += "\nEnter 'quit' if you're done: "
print("\n")
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"{topping} will added to your pizza.")
    else:
        break
