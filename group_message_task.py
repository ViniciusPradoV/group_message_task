import json

with open('U1ZQR43RB.json') as json_file:
    data =  json.load(json_file)

users = {}
for i in range(len(data)):
    if data[i]['user'] in users:
        users[data[i]['user']].append(data[i])
    else:
        users[data[i]['user']] = [data[i]]
