import json
import os
from config import DATA_FILE

# create a blank json file if not exist json file
def create_json_file():
    if not os.path.exists(DATA_FILE):
      try:
         with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(list(), file)
      except OSError:
         print('Error: Unable to create data file.')

# save json file with content
def save_expense(expenses):
   try:
      with open(DATA_FILE, 'w', encoding='utf-8') as file:
         json.dump(expenses, file, indent=4)
   except OSError:
      print('Error: Unable to save task to disk.')

# load json file (i.e. deserialize file-like object containing the JSON document to be deserialized)
def load_expenses():   
   create_json_file() 
   try:
      with open(DATA_FILE, 'r', encoding='utf-8') as file:
         return json.load(file) 
   except json.JSONDecodeError as e:
      print('Warning: Task data could not be loaded. An empty list will be used.')
      return []
   