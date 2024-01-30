import json
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'startlists.json')

def get_db():
    with open(filename) as f:
        data = json.load(f)
    return data 