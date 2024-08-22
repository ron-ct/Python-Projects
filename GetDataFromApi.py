#Obtaining data from the pokemon api at https://pokeapi.co/
import requests
import json

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_data(name):
    url = f"{base_url}/pokemon/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully Obtained data from Api")
        response_data = response.json()
        return response_data
    else:
        print("Error Fetching data")
        return False


pokemon_name = input("Enter your Favorite Pokemon: ")

pokemon_data = get_pokemon_data(pokemon_name)

if pokemon_data:
    print(f"Pokemon Name: {pokemon_data['name']}")
    print(f"Pokemon Height: {pokemon_data['height']}")
    print(f"Pokemon Weight: {pokemon_data['weight']}")
    with open("pokemon_data.json", "w") as file:
        json.dump(pokemon_data, file)
        print("Successfuly created the json file")


# Try to read the horoscope data from horoscopeData.json and convert to json python object
#json.load is used for reading json data from files

with open("horoscopeData.json", "r") as infile:
    loaded_data = json.load(infile)

print(loaded_data)
print(loaded_data['data'])