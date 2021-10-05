import json
import sys
import uuid
from operator import itemgetter

# add.py category link [title description]

# Get data
with open("links.json") as f:
  data = json.load(f)

# Get template
with open("template.html") as f:
  html = f.read()

output = []
output.append('<html><head></head><body>')

# Sort categories
lcat = []
for c in data['categories'].keys():
  lcat.append({'key': c, 'order': data['categories'][c]['order']})
slcat = sorted(lcat, key=itemgetter('order'))

# Write HTML
for c in slcat:
  output.append(f"<h1>{c['key'].capitalize()}</h1><ul>")
  for l in data['categories'][c['key']]['items']:
    if l['title'] != "":
      output.append(f"<li><a href=\"{l['link']}\">{l['title']}</a></li>")
    else:
      output.append(f"<li><a href=\"{l['link']}\">{l['link']}</a></li>")

  output.append('</ul>')

output.append('</body></html>')

# Write
html = html.replace('{content}', ("\n".join(output)))
with open("../index.html", "w") as f:
  f.write(html)
