def describe_city(city, country='Dubai'):
    txt = city.title() + " is located in " + country.title() + "."
    print(txt)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')