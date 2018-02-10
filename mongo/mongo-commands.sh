## Create mongo-data directory next to mongo folder with bin of commands
## Navigate to mongo command directory
cd mongo/bin

## Start server to create active connection
./mongod --dbpath ~/mongo-data

## In new tab, run mongo console and connect to server we just started
./mongo

## Insert a document to the db
db.Todos.insert({text: 'Learn MongoDB'})

## Fetch documents
db.Todos.find()