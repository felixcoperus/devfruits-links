import json
import sys
from operator import itemgetter

# Get data
with open("links.json") as f:
  data = json.load(f)


# Get input
key = sys.argv[1]
order = int(sys.argv[2])

# Tranform
cats = data['categories']
lcats = []
for c in cats.keys():
  corder =  data['categories'][c]['order']
  
  if corder >= order:
    data['categories'][c]['order'] += 1
  if c == key:
    data['categories'][c]['order'] = order
  
  lcats.append({'key':c, 'order': data['categories'][c]['order']})

# Order output
slcats = sorted(lcats, key=itemgetter('order'))
for c in slcats:
  print(data['categories'][c['key']]['order'], c['key'])

# Write
with open("links.json", "w") as f:
  json.dump(data, f, indent = 2)

