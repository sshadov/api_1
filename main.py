import requests
from pprint import pprint
import json


# response = requests.get("https://superheroapi.com/api/2619421814940190/search/hulk")
#
#
# x = response.json()
#
# y = x['results']
# pprint(int(y[1]['id']))


class superhero:
    def __init__(self, name):
        self.name = name

    def id(self):
        response = requests.get("https://superheroapi.com/api/2619421814940190/search/" + self.name)
        information_character = response.json()
        id_ = []
        id_ = (information_character['results'][0]['id'])
        return id_

    def intelligence(self):
        response = requests.get("https://www.superheroapi.com/api.php/2619421814940190/" + self.id() + "/powerstats")
        powerstats = response.json()
        return int(powerstats['intelligence'])

def most_intelligence():
    dict_intelligence = {"thanos": thanos.intelligence(), "captain_america": captain_america.intelligence(), "hulk": hulk.intelligence()}
    keymax = max(dict_intelligence, key=dict_intelligence.get)
    return keymax

hulk = superhero("hulk")
captain_america = superhero("Captain_America")
thanos = superhero("thanos")
print(hulk.intelligence())
print("Самый умный: ", most_intelligence())