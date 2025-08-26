from random_address import random_address, real_random_address


CA = random_address.real_random_address_by_state('CA')
POS = random_address.real_random_address_by_postal_code('32409')

# Generate a dictionary with valid random address information
def address_generation():
    address = real_random_address()
    address1 = address.get('address1')
    city = address.get('city')
    state = address.get('state')
    postalCode = address.get('postalCode')
    coordinates = address.get('coordinates')
    latitude = coordinates.get('lat')
    longitude = coordinates.get('lng')
    return f"{address1}, {city}, {state} {postalCode}, USA"


for _ in range(10):
    print(address_generation())
