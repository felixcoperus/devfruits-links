import json
import sys
#import uuid

# Get data
with open("links.json") as f:
  data = json.load(f)

# Set values for new link
cat_to_delete = sys.argv[1]

target_cat = ''
if len(sys.argv) > 2:
  target_cat = sys.argv[2]

# Move links to target category
if target_cat != '':
  # Create category if not exists
  if target_cat not in data['categories'].keys():
    data['categories'][target_cat] = {'order':0, 'items':[]}

  # Move links
  for c in data['categories'].keys():
    if c == cat_to_delete:
      for l in data['categories'][c]['items']:
        data['categories'][target_cat]['items'].append(l)
      break

# Delete category
data['categories'].pop(cat_to_delete)

# Write
with open("links.json", "w") as f:
  json.dump(data, f, indent = 2)
