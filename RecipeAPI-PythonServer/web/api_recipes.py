# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer
import requests
from urllib.parse import urlparse, parse_qs
import json
import argparse
from collections import OrderedDict, Counter
from requests.auth import HTTPBasicAuth
import pandas as pd
from pandas import DataFrame
import urllib.request,urllib.error , sys, re, base64
from postgresqlconnector import*

###----------------------------------------- RECIPES LIST -----------------------------------------####

RECIPES = [
    {'id': 1, 'name': 'salad', 'prep_time': 30, 'difficulty': 2, 'vegetarian': True},
    {'id': 2, 'name': 'tasty goulash', 'prep_time': 60, 'difficulty': 3, 'vegetarian': True},
    {'id': 3, 'name': 'stew',  'prep_time': 95, 'difficulty': 2, 'vegetarian': False},
    {'id': 4, 'name': 'sadza',  'prep_time': 45, 'difficulty': 1, 'vegetarian': True},
    {'id': 5, 'name': 'salad and chips', 'prep_time': 30, 'difficulty': 2, 'vegetarian': True},
    {'id': 6, 'name': 'mince goulash', 'prep_time': 60, 'difficulty': 3, 'vegetarian': True},
    {'id': 7, 'name': 'lamb stew',  'prep_time': 45, 'difficulty': 2, 'vegetarian': False},
    {'id': 8, 'name': 'sadza',  'prep_time': 55, 'difficulty': 3, 'vegetarian': False},
    {'id': 9, 'name': 'tomato salad', 'prep_time': 30, 'difficulty': 2, 'vegetarian': True},
    {'id': 10, 'name': 'moms best goulash', 'prep_time': 60, 'difficulty': 3, 'vegetarian': True},
    {'id': 11, 'name': 'stew',  'prep_time': 45, 'difficulty': 2, 'vegetarian': False},
    {'id': 12, 'name': 'sadza nedovi',  'prep_time': 90, 'difficulty': 1, 'vegetarian': True},
    ] #Values for testing

#RECIPES = [] #Initial Production value

###----------------------------------------- RATINGS LIST -----------------------------------------####

RATINGS = [
    {'id': 1, 'rating': 3},
    {'id': 1, 'rating': 3},
    {'id': 1, 'rating': 5},
    {'id': 2, 'rating': 5},
    {'id': 2, 'rating': 4},
    {'id': 2, 'rating': 4},
    {'id': 3, 'rating': 2},
    {'id': 3, 'rating': 2}
    ] # Values for Testing

#RATINGS = [] # Initial Prod value

###--------------------------- TO VERIFY VALIDITY OF DATA SENT IN REQUESTS ---------------------------####

def checkPostedData(postedData, functionName):
    if (functionName == "add_recipe"):
        if "name" not in postedData:
            return 332
        elif "prep_time" not in postedData:
            return 333
        elif "difficulty" not in postedData:# or "difficulty" > 3 or "difficulty" < 1:
            return 334
        elif "vegetarian" not in postedData: #or "vegetarian" is not bool:
            return 335
        else:
            return 200

    if (functionName == "recipe_delete"):
        if "id" not in postedData:
            return 331
        else:
            return 200

    if (functionName == "update_recipe"):
        if "id" not in postedData:
            return 331
        elif "name" not in postedData:
            return 332
        elif "prep_time" not in postedData:
            return 333
        elif "difficulty" not in postedData:
            return 334
        elif "vegetarian" not in postedData:
            return 335
        else:
            return 200

    if (functionName == "rate_recipe"):
        if "id" not in postedData:
            return 331
        elif "rating" not in postedData:
            return 336
        else:
            return 200
###---------------------------------------- ERROR HANDLING ----------------------------------------####
#Error handling of data sent. These are messages sent if there is an error

def code_action(self, status_code):
    def send_error(status_code, retMap):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data_json = json.dumps(({'data':retMap}), indent=4, separators=(',', ': '))
        self.wfile.write(str(data_json).encode())

    if (status_code == 331):
        retMap = {
        'Message':"Missing or incorrect id value",
        'Status Code': status_code
        }
        send_error(status_code,retMap)
    elif (status_code == 332):
        retMap = {
        'Message':"Missing or incorrect name value",
        'Status Code': status_code
        }
        send_error(status_code,retMap)
    elif (status_code == 333):
        retMap = {
        'Message':"Missing or incorrect prep_time value",
        'Status Code': status_code
        }
        send_error(status_code,retMap)
    elif (status_code == 334):
        retMap = {
        'Message':"Missing or incorrect difficulty value",
        'Status Code': status_code
        }
        send_error(status_code,retMap)
    elif (status_code == 335):
        retMap = {
        'Message':"Missing or incorrect vegetarian value",
        'Status Code': status_code
        }
        send_error(status_code,retMap)
    elif (status_code == 336):
        retMap = {
        'Message':"Missing or incorrect rating value",
        'Status Code': status_code
        }
        send_error(status_code,retMap)
    else:
        pass

###----------------------------------------- MAPPED ACTIONS -----------------------------------------####
#After routing by the HTTPS values, these are the functions that control what happens. Like 'views'

#To get all recipes
def list_recipes(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    data_json = json.dumps(({'data':RECIPES}),  indent=4, separators=(',', ': '))
    self.wfile.write(str(data_json).encode())
    return data_json

#To add a recipe
#@authentication
def add_recipe(self):
    if not RECIPES:
        new_id = 1
    else:
        new_id = max([x['id'] for x in RECIPES])+1

    # Get Data
    self._set_headers()
    self.data_string = self.rfile.read(int(self.headers['Content-Length']))
    self.send_response(200)
    self.end_headers()
    data = json.loads(self.data_string)

    #Step 1b: verify data
    status_code = checkPostedData(data,"add_recipe")
    #Error Handling
    code_action(self, status_code)

    if status_code == 200:

        print("new id: %d" % new_id)
        new_name = data['name']
        prep_time = data["prep_time"]
        difficulty = int(data["difficulty"])
        vegetarian = bool(data["vegetarian"])
        dbAddRecipe(new_name,prep_time,difficulty,vegetarian)
        new_recipe = {
            'id': new_id,
            'name': new_name,
            'prep_time':prep_time,
            'difficulty':difficulty,
            'vegetarian':vegetarian
            }
        RECIPES.append(new_recipe)

         #RETURN AND HANDLE HTTP RESPONSE CODE
        self.send_response(201)
        self.end_headers()
        '''
        #Step 2: Send computation back
         retMap = {
             "Message": "Recipe created",
             "Status Code": 201
         }
        '''
        data_json = json.dumps(({'data':new_recipe}), indent=4, separators=(',', ': '))
        self.wfile.write(str(data_json).encode())
        return data_json

#To collect a specific recipe according to ID.
def recipe_get(self, recipe_id):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    recipe_id = int(recipe_id)
    my_recipe = next((recipe for recipe in RECIPES if recipe['id'] == recipe_id), None)

    #find out the rating of the recipe.NOT being sent in the JSON at present, not part of the SCHEMA but can be added
    #already as is to the json if need be. Currently a floating value.
    df_ratings = pd.DataFrame(RATINGS)
    df_output = df_ratings.groupby('id').mean()
    df_output= df_output.to_dict('dict')
    rating= df_output['rating'][recipe_id]

    data_json = json.dumps(({'data':my_recipe}),  indent=4, separators=(',', ': '))
    self.wfile.write(str(data_json).encode())
    return data_json

#Delete recipe according to ID
def recipe_delete(self,recipe_id):
    # Get Data
    self._set_headers()
    self.data_string = self.rfile.read(int(self.headers['Content-Length']))
    self.send_response(200)
    self.end_headers()

    data = json.loads(self.data_string)

    #Step 1b: verify data
    status_code = checkPostedData(data,"recipe_delete")
    #Error Handling
    code_action(self, status_code)

    if status_code == 200:

        #RECIPES[:] = [d for d in RECIPES if d.get('id')!= recipe_id]
        recipe_index = next((index for (index,d) in enumerate(RECIPES) if d["id"]==int(recipe_id)), None)
        del RECIPES[recipe_index]
        self.send_response(201)
        self.end_headers()

        #Step 2: Send computation back
        retMap = {
         "Message": "Recipe deleted",
         "Status Code": 201
        }
        data_json = json.dumps(({'data':retMap}),  indent=4, separators=(',', ': '))
        self.wfile.write(str(data_json).encode())
        return data_json


#Update an existing recipe according to id --> Perhaps create a new Recipe if ID is out of bounds?
def update_recipe(self,recipe_id,):
    # Get Data
    self._set_headers()
    self.data_string = self.rfile.read(int(self.headers['Content-Length']))
    self.send_response(200)
    self.end_headers()

    data = json.loads(self.data_string)

    #Step 1b: verify data
    status_code = checkPostedData(data,"update_recipe")
    #Error Handling
    code_action(self, status_code)

    if status_code == 200:
        this_recipe = next(item for item in RECIPES if item["id"]==int(recipe_id))
        this_recipe["name"]= data["name"]
        this_recipe["prep_time"] = data["prep_time"]
        this_recipe["difficulty"] = int(data["difficulty"])
        this_recipe["vegetarian"] = bool(data["vegetarian"])
        updated_recipe = {
        'name': data["name"],
        'prep_time':data["prep_time"],
        'difficulty':data["difficulty"],
        'vegetarian':data["vegetarian"]
        }

        #RETURN AND HANDLE HTTP RESPONSE CODE
        self.send_response(201)
        self.end_headers()
        data_json = json.dumps(({'data':this_recipe}),  indent=4, separators=(',', ': '))
        self.wfile.write(str(data_json).encode())
        return

#Create a new rating for a specif recipe according to ID. Values are aggregated for each recipe within the recipe_get
#function
def rate_recipe(self,recipe_id):
    # Get Data
    self._set_headers()
    self.data_string = self.rfile.read(int(self.headers['Content-Length']))
    self.send_response(200)
    self.end_headers()
    data = json.loads(self.data_string)


    #Step 1b: verify data
    status_code = checkPostedData(data,"rate_recipe")
    #Error Handling
    code_action(self, status_code)

    if status_code == 200:

         id_recipe = data['id']
         rating = data["rating"]
         new_rating = {
            'id': id_recipe,
            'rating': rating
            }
         RATINGS.append(new_rating)
         #RETURN AND HANDLE HTTP RESPONSE CODE
         self.send_response(201)
         self.end_headers()
         data_json = json.dumps(({'data':new_rating}), indent=4, separators=(',', ': '))
         self.wfile.write(str(data_json).encode())
         return data_json

#Search functionality. Returns all recipes that have the parameter within. Automatically includes any additions we
# might add to the Recipe SCHEMA such as recipe description and/or ingredients for examples. Uses panda data frames
#to enable this.
def search_get(self):
    # Get Data
    self._set_headers()
    self.data_string = self.rfile.read(int(self.headers['Content-Length']))
    self.send_response(200)
    self.end_headers()

    data = json.loads(self.data_string)
    key, value = list(data.items())[0]
    my_search = []

    df_search = pd.DataFrame(RECIPES)
    df_search.name = df_search.name.astype('str')
    df_output = df_search[df_search.name.str.contains(value)]
    #df_output = df[df_ratings.name.str.contains(value)]
    df_output= df_output.to_dict('index')
    #To strip outer layer of dictionary
    for recipe in df_output:
        val = df_output.get(recipe)
        my_search.append(val)

    data_json = json.dumps(({'data':my_search}),  indent=4, separators=(',', ': '))
    self.wfile.write(str(data_json).encode())
    return data_json
