##############
## Open file and have it auto close
with open('file.txt', 'w') as file:
    file.write('Hello world')

with open('file.txt', 'r') as file:
    CONTENT = file.readlines()
    print(CONTENT[0])

with open('file.json', 'r') as file:
    JSON_CONTENT = json.load(file)
    for movie in JSON_CONTENT['movies']:
        print(movie['name'])