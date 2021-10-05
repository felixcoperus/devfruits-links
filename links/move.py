import json
import sys

# Get data
with open("links.json") as f:
  data = json.load(f)

# Set values for new link
link_uuid = sys.argv[1]
target_cat = sys.argv[2]

# Add new category (if not exists)
if target_cat not in data['categories'].keys():
  data['categories'][target_cat] = {'order':0, 'items':[]}

# Move link
found = False
for c in data['categories'].keys():
  for l in data['categories'][c]['items']:
    if l['uuid'] == link_uuid:
      data['categories'][target_cat]['items'].append(l)
      data['categories'][c]['items'].remove(l)
      found = True
      break
  if found:
    break

# Write
with open("links.json", "w") as f:
  json.dump(data, f, indent = 2)
