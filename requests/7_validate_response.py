import json
import requests
from pprint import pprint

def find_mismatched_data(url, file_name):

    response = requests.get(url)
    api_data = response.json()


    with open(file_name, 'r') as file:
        expected_data = json.load(file)

    
    mismatches = {}
    for expected_planet in expected_data['results']:
        planet_name = expected_planet['name']

        if planet_name in api_data['results']:
            api_planet = api_data['results'][planet_name]
            mismatched_values = {}

            for key, expected_val in expected_planet.items():
                if key in api_planet and api_planet[key] != expected_val:
                    mismatched_values[key] = {'Expected': expected_val, 'Actual': api_planet[key]}

            if mismatched_values:
                mismatches[planet_name] = mismatched_values

    return mismatches

if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"

    pprint(find_mismatched_data(url, file_name))
