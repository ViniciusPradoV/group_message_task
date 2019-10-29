import json

with open('U1ZQR43RB.json') as json_file:
    data =  json.load(json_file)

users = {}
for i in range(len(data)):
    if data[i]['user'] in users:                 ## if user already exists, add to the list
        users[data[i]['user']].append(data[i])
    else:                                       ## if user doesn't exist, create the list
        users[data[i]['user']] = [data[i]]


## print(users)

for user in users.keys():
    subgroup = {}
    timestamp = "000"

    ## print(bool(subgroup)) - checking if dict is empty
    for field in users[user]:
        if subgroup: ## checking if dict is empty
            timestamp = field['ts']
            subgroup[timestamp] = [field]
        elif float(field['ts']) - float(timestamp) < 120:  ## comparing current timestamp with last one
            subgroup[timestamp].append(field)               ## adding to the subgroup of the last timestamp
        else:                                               ## creating new subgroup for current timestamp
            timestamp = field['ts']
            subgroup[timestamp] = [field]

    json_file = open("%s.json" % user, 'w')
    json.dump(subgroup, json_file)
