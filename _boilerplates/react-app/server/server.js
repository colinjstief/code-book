require('./config/config');

const _ = require('lodash');
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');

// Setup
const port = process.env.PORT;
const app = express();
const publicPath = path.join(__dirname, './../public');

// Middleware
app.use(express.static(publicPath));
app.use(bodyParser.json());

// Routes
app.get('*', (req, res) => {
  res.sendFile(path.join(publicPath, 'index.html'));
});

// Start listening...
app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});