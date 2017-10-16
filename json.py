import requests
import json
response = requests.get("""http://www.sbi.uni-rostock.de/triplexrna/
JSON/Human/gene/CDKN1A""")
if response.status_code == 200:
  results = json.loads(response.content) 
# results can be now accessed as a Python dictionary
