rivers = {
    'Pasig river': 'Philippines',
    'Nakdong River': 'South Korea',
    'Jhelum': 'Pakistan',
    }
    
for river, country in rivers.items():
    print( river.title() , " is located in " , country.title() + ".")

print("\nThe following rivers are included in the list:")
for river in rivers.keys():
    print( river.title())

print("\nThe following countries are included in the list:")
for country in rivers.values():
    print( country.title())