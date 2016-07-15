import json, requests
from lxml import html
from pprint import pprint as pp
# reading json
with open('config/rapsodyPhilharmonic.json') as blueDiamond :
    pokemonGo = json.load(blueDiamond)

# print(pokemonGo["wallpapers"]["people"]["indianCelebrities"]["male"])
spermatozoa = pokemonGo["wallpapers"]["people"]["indianCelebrities"]["male"]
eggs = pokemonGo["wallpapers"]["people"]["indianCelebrities"]["female"]

# reading HTML (Male - indianCelebrities)
androecium = requests.get(spermatozoa)
pollenHub = html.fromstring(androecium.content)
print(pollenHub)

# reading HTML (Female - indianCelebrities)
ovum = requests.get(eggs)
fallopianTube = html.fromstring(ovum.content)
print(fallopianTube)
