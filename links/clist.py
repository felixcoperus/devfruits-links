import json
import sys
from operator import itemgetter

# Get data
with open("links.json") as f:
  data = json.load(f)

cats = data['categories']
lcats = []
for c in cats.keys():
  lcats.append({'key':c, 'order': cats[c]['order']})

slcats = sorted(lcats, key=itemgetter('order'))
for c in slcats:
  print(c['order'], c['key'])
