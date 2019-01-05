import json
from pprint import pprint

with open('queue.txt') as f:
  data = json.load(f)

pprint(data)