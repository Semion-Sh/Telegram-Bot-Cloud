import json

ar = []

with open('Warning Words', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n:
            ar.append(n)
with open('cenz.json', 'w', encoding='utf-8') as write_file:
    json.dump(ar, write_file)


