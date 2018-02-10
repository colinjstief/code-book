// Manual

// const {SHA256} = require('crypto-js');

// let message = 'I am user number 3';
// let message_hash = SHA256(message).toString();

// console.log(`Message: ${message}`);
// console.log(`Hash: ${message_hash}`);

// let data = {
//     id: 4
// }

// let token = {
//     data,
//     hash: SHA256(JSON.stringify(data) + 'salt').toString()
// }

// token.data.id = 5;
// token.hash = SHA256(JSON.stringify(token.data).toString());

// let result_hash = SHA256(JSON.stringify(token.data) + 'salt').toString();

// if (result_hash === token.hash) {
//     console.log('Data was not changed');
// } else {
//     console.log('Changed!!');
// }

// // JWT

// const jwt = require('jsonwebtoken');

// let data = {
//     id: 10
// };

// let token = jwt.sign(data, 'salting');
// console.log(`Token: ${token}`);

// let decoded = jwt.verify(token, 'salting');
// console.log('Decoded:', decoded);


// Bcrypt

const bcrypt = require('bcryptjs');

let password = '123abc!';

bcrypt.genSalt(10, (err, salt) => {
    bcrypt.hash(password, salt, (err, hash) => {
        console.log(hash);
    })
});

let hashedPassword = '$2a$10$fi7J6GfIFMLuTszd55z2zeRk79t1cTo39hjlAGonAP7WEEERkXfFu';
bcrypt.compare(password, hashedPassword, (err, res) => {
    console.log(res);
});
