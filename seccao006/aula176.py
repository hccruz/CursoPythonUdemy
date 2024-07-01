# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple    array
# string        string
# int, float    number
# True          true
# False         false
# None          null

import json
# from pprint import pprint
from typing import TypedDict


class Filme(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list
    budget: int | None


string_json = """
{
    "title": "Senhor do Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandolf", "Legolas", "Bormir"],
    "budget": null
}
"""

filme: Filme = json.loads(string_json)
# pprint(filme, width=40)
# print(filme['title'])
# print(filme['characters'][0])
# print(filme['year'])
# print(filme['characters'][1])

json_string = json.dumps(filme, indent=4, ensure_ascii=False)
print(json_string)
