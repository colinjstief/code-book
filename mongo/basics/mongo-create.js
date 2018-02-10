const MongoClient = require('mongodb').MongoClient;

// const {MongoClient, ObjectID} = require('mongodb') // Using ES6 destructuring
// var obj = new ObjectID();
// console.log(obj);

MongoClient.connect('mongodb://localhost:27017/TodoApp', (err, db) => {
    if (err) {
        return console.log('Unable to connect to Mongo server');
    }
    console.log('Connected to mongo');

    db.collection('Todos').insertOne({
        text: 'Learn Mongodb',
        completed: false
    }, (err, result) => {
        if (err) {
            return console.log('Unable to insert todo', err);
        }
        console.log(JSON.stringify(result.ops, undefined, 2));
    });

    db.collection('Users').insertOne({
        name: 'Colin',
        age: 30,
        location: 'Washington, D.C.'
    }, (err, result) => {
        if (err) {
            return console.log('Unable to insert user', err);
        }
        // Get the timestamp
        console.log(JSON.stringify(result.ops[0]._id.getTimestamp(), undefined, 2));
    });

    db.close();
});