const {ObjectID} = require('mongodb');

const {mongoose} = require('./../../node/udemy-complete-nodejs/todo/server/db/mongoose.js');
const {Todo} = require('./../../node/udemy-complete-nodejs/todo/server/models/Todo.js');
const {User} = require('./../../node/udemy-complete-nodejs/todo/server/models/User.js');

const id = '59ac019f155c2d547c72f73b';
const userId = '59aabf1a8396cb0e6ad7fd17';

// ObjectID.isValid() validates the provided ID
if (!ObjectID.isValid(id)) {
    return console.log('ID is not valid');
}

// find() returns all documents that match your query
//                an array
// Note: Mongoose converts your id string to an ObjectID automatically
Todo.find({
    _id: id
}).then((todos) => {
    if (!todos.length) {
        return console.log('No IDs found');
    }
    console.log('find() Todos', todos);
}, (err) => {
    console.log('Error', err);
}).catch((e) => console.log(e));

// findOne() returns the first document that matches your query
//                   an object (if it's empty you get null)
Todo.findOne({
    _id: id
}).then((todo) => {
    if (!todo) {
        return console.log('Not found');
    }
    console.log('findOne() Todo', todo);
}, (err) => {
    console.log('Error', err);
}).catch((e) => console.log(e));

// findById() returns the document that matchs your id
//                   an object (if it's empty you get null)
// Note: Mongoose converts your id string to an ObjectID automatically
Todo.findById(id).then((todo) => {
    if (!todo) {
        return console.log('Id not found');
    }
    console.log('findById() Todo', todo);
}, (err) => {
    console.log('Error', err);
}).catch((e) => console.log(e));

// ObjectID.isValid() validates the provided ID
if (!ObjectID.isValid(userId)) {
    return console.log('User ID is not valid');
}

User.findById(userId).then((user) => {
    if (!user) {
        return console.log('Id not found');
    }
    console.log('findById() Users', user);
}, (err) => {
    console.log('Error', err);
}).catch((e) => console.log(e));

mongoose.connection.close();