const path = require('path');

module.exports = {
  // Where is the input file?
  entry: './src/app.js',
  // What are the details of the output file?
  output: {
    // Where do we put it?
    path: path.join(__dirname, 'public'),
    // What should it be called?
    filename: 'bundle.js'
  },
  // What are we doing?
  module: {
    rules: [{
      test: /\.js$/,
      exclude: /node_modules/,
      loader: 'babel-loader'
    }]
  }
}