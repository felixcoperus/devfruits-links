import json
import sys
#import uuid

# Get data
with open("links.json") as f:
  data = json.load(f)

cat = ""

if len(sys.argv) > 1:
  cat = sys.argv[1]
  for l in data['categories'][cat]['items']:
    print(l['uuid'], l['title'], l['link'])

else:
  for c in data['categories']:
    print('['+c.upper()+']')
    for l in data['categories'][c]['items']:
      print(l['uuid'], l['title'], l['link'])
    print("") 
