const {ObjectID} = require('mongodb');

const {mongoose} = require('./../../node/udemy-complete-nodejs/todo/server/db/mongoose.js');
const {Todo} = require('./../../node/udemy-complete-nodejs/todo/server/models/todo.js');
const {User} = require('./../../node/udemy-complete-nodejs/todo/server/models/user.js');

// remove({}) remove all documents that match your query
Todo.remove({}).then((result) => {
    console.log(result);
}, (err) => {
    console.log("Error", err);
}).catch((err) => console.log(err));

// // findOneAndRemove({key: value}) remove one document that matches your query and return the object
Todo.findOneAndRemove({_id: '59ac3a154adbf7adaf877f57'}).then((todo) => {
    console.log(todo);
}, (err) => {
    console.log("Error", err);
}).catch((err) => console.log(err));

// findByIdAndRemove('123asdf') remove one document that maches the id and return the object
Todo.findByIdAndRemove('59ac39e34adbf7adaf877f37').then((result) => {
    console.log(result);
}, (err) => {
    console.log("Error", err);
}).catch((err) => console.log(err));

mongoose.connection.close();