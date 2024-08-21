#Obtaining data from the pokemon api at https://pokeapi.co/
import requests

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
