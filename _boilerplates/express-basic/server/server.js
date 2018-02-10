require('./config/config');

const _ = require('lodash');
const path = require('path');
const express = require('express');

const port = process.env.PORT;
const app = express();

const publicPath = path.join(__dirname, './../public');
app.use(express.static(publicPath));

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});