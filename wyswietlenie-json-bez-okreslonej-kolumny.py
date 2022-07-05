# W systemie znajduje się plik states.json o następującej zawartości:
# {
#     "data": [
#         {
#             "State": "Alabama",
#             "Abbrev": "Ala.",
#             "Code": "AL"
#         },
#         {
#             "State": "Alaska",
#             "Abbrev": "Alaska",
#             "Code": "AK"
#         },
# ...
# Napisz program, który wyświetli json z powyższego pliku bez kolumny Code.

import json
file = open('states.json','r')
json_txt = file.read()
states = json.loads(json_txt)
for state in states['data']:
    del state['Code']
print(json.dumps(states))