import api_recipes
import requests
import json
from requests.auth import HTTPBasicAuth


test_resp = add_recipe("Chicken Kebab",30,2,0)
if test_resp.status_code != 201:
    raise ApiError('Cannot create recipe: {}'.format(test_resp.status_code))
print('Created recipe. ID: {}'.format(test_resp.json()["id"]))

test_resp = get_recipes()
if test_resp.status_code != 200:
    raise ApiError('Cannot fetch all recipes: {}'.format(test_resp.status_code))
for recipes_item in test_resp.json():
    print('{} {}'.format(RECIPES['id'], RECIPES['name']))
