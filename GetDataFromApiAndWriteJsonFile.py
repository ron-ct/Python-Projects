import requests
import json

def getHoroscopeData():
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today"

    response = requests.get(url)

    if response.status_code == 200:
        response_data = response.json()
        print("Successfuly obtained data from API")
        return response_data
    else:
        print("Error in fetching data")
        return False

horoscopeData = getHoroscopeData()

if horoscopeData:
    with open("horoscopeData.json", "w") as file:
        json.dump(horoscopeData, file)
        print("Successfuly created json file.")


#Try to read the pokemon_data.json file. Not required just for fun

with open("pokemon_data.json", "r") as infile:
    pokemonData = json.load(infile)
    print(pokemonData['name'])


