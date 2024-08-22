def getDataFromAnyApi(url):
    import requests
    response = requests.get(url)

    try:

        if response.status_code == 200:                
                print("Successfuly obtained data from API.")
                response_data = response.json()
                wants_json = input("Do you need a JSON file created for this? (Y) or just return the json data(N): ").lower() == "y"
        
                if wants_json:
                    import json
                    jsonFileName = input("Enter a name for your json file: ")
                    with open(f"{jsonFileName}.json", "w") as file:                        
                        json.dump(response_data, file)
                        print(f"The {jsonFileName} json file has been created successfully.")
                        return None
                else:
                    return response_data
        else:                        
            raise Exception("Error Fetching data From your API")
    except Exception as ex:            
            print(f"Exception: {ex}")

