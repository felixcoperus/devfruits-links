import json
import sys
import uuid

# add.py category link [title description]

# Get data
with open("links.json") as f:
  data = json.load(f)

# Set values for new link
cat = sys.argv[1]
title = sys.argv[3]
link = sys.argv[2]
description = ""
link_uuid = str(uuid.uuid4())

if len(sys.argv) > 4:
  description = sys.argv[4]

# Add new category (if not exists)
if cat not in data['categories'].keys():
  data['categories'][cat] = {'order':0, 'items':[]}

# Add new link to tree
data['categories'][cat]['items'].append({"title": title, "link": link, "description": description, "uuid": link_uuid})

# Write
with open("links.json", "w") as f:
  json.dump(data, f, indent = 2)
