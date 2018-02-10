const {MongoClient, ObjectID} = require('mongodb');

MongoClient.connect('mongodb://localhost:27017/TodoApp', (err, db) => {
    if (err) {
        return console.log('Unable to connect to MongoDB', err);
    }
    console.log('Connected to MongoDB');

    // deleteMany()
    // delete all instances that match the given criteria
    db.collection('Todos').deleteMany({
        text: 'Eat lunch'
    }).then((result) => {
        console.log(result);
    });

    // deleteOne()
    // same as above, but stops after the first

    // findOneAndDelete()
    // delete all instance that match the given criteria
    // and also return the object
    db.collection('Todos').findOneAndDelete({
        _id: new ObjectID('a23fs61sdf09df9')
    }).then((result) => {
        console.log(result);
    });

});