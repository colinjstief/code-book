// node.js is a javascript runtime that uses the v8 engine
// v8 engine is an open source javascript engine written in c++ that takes js code and compiles it to machine code

global; // equivalent to window in browser
process; // equivalent to document in browser
process.env.PORT; // port property
process.env.NODE_ENV // current environment... in development, it's === undefined; Heroku sets this === 'production'
module;