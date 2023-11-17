pets = []
pet = {
    'name': 'anna',
    'type of animal': 'panda',
    'fav food': 'leaf',
    'owner': 'ann',
    'color': 'black and white',
}
pets.append(pet)
pet = {
    'name': 'lovely',
    'type of animal': 'cat',
    'fav food': 'fish',
    'owner': 'ayesha',
    'color': 'black',
}
pet = {
    'name': 'ashley',
    'type of animal': 'elephant',
    'fav food': 'watermelon',
    'owner': 'jake',
    'color': 'grey',
}
pets.append(pet)
pet = {
    'name': 'lizzy',
    'type of animal': 'puppy',
    'fav food': 'bone',
    'owner': 'billy',
    'color': 'white',
}
pets.append(pet)
pet = {
    'name': 'belle',
    'type of animal': 'hamster',
    'fav food': 'lettuce',
    'owner': 'ayesha',
    'color': 'orange and white',
}
pets.append(pet)
for pet in pets:
    print("\nInfo about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))