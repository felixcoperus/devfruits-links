import json
import sys
#import uuid

# Get data
with open("links.json") as f:
  data = json.load(f)

# Set values for new link
link_uuid = sys.argv[1]

# Remove listitem
for c in data['categories']:
  for l in data['categories'][c]['items']:
    if l['uuid'] == link_uuid:
      data['categories'][c]['items'].remove(l)

# Write
with open("links.json", "w") as f:
  json.dump(data, f, indent = 2)
