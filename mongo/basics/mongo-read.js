const {MongoClient, ObjectID} = require('mongodb');

MongoClient.connect('mongodb://localhost:27017/TodoApp', (err, db) => {
    if (err) {
        return console.log('Unable to connect to Mongo server');
    }
    console.log('Connected to mongo');

    // .getCollection('collection').find() returns a cursor with various methods
    // .toArray() returns all the docs as a promise

    //db.collection('Todos').find().toArray().then((docs) => {                      // Fetch all documents
    //db.collection('Todos').find({completed: true}).toArray().then((docs) => {     // Fetch documents that satisfy completed === true
    db.collection('Todos').find({
         _id: new ObjectID('59a5e6319f530a023a58b19e')
    }).toArray().then((docs) => {                                                   // Fetch documents that match the given ID object
        console.log('Todos');
        console.log(JSON.stringify(docs, undefined, 2));
    }, (err) => {
        console.log('Unable to fetch todos', err);
    });

    // .count() does what it says
    // db.collection('Todos').find().count().then((count) => {                                                   // Fetch documents that match the given ID object
    db.collection('Users').find({
        name: 'Colin'
    }).count().then((count) => {                                                   // Fetch documents that match the given ID object
        console.log(`Users named Colin: ${count}`);
    }, (err) => {
        console.log('Unable to count todos', err);
    });

    //db.close();
});