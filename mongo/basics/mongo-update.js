const {MongoClient, ObjectID} = require('mongodb');

MongoClient.connect('mongodb://localhost:27017/TodoApp', (err, db) => {
    if (err) {
        return console.log('Unable to connect');
    }
    console.log('Connected');

    //db.collection('name').findOneAndUpdate(filter, update, options, callback);
    db.collection('Todos').findOneAndUpdate({
        _id: new ObjectID('59a37b888dd7304b72b8dc23')
    }, {
        $set: {
            completed: false
        }
    }, {
        returnOriginal: false
    }).then((result) => {
        console.log(result);
    });

    db.collection('Users').findOneAndUpdate({
        _id: new ObjectID('59a37c8763323a4d4a3d215e')
    }, {
        $set: {
            name: 'Colin'
        },
        $inc: {
            age: -1
        }
    }, {
        returnOriginal: false
    }).then((result) => {
        console.log(result);
    });

    // db.close();

});