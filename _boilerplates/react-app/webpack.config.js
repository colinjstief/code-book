// For creating proper paths
const path = require('path');

// For extracting css and scss files from our build so we can place one file in our html head
const ExtractTextPlugin = require('extract-text-webpack-plugin');

// What's our current running environment?
// Heroku assigns 'production'; test assigns 'test'; development is undefined
process.env.NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = (env) => {

  // env is set to 'production' in the package.json build:prod script; 
  // if that's true, we're going to load a different source map below
  const isProduction = env === 'production';

  // What should we call our style build?
  const CSSExtract = new ExtractTextPlugin('styles.css');

  return {
    // Where is the input file? (Note we define an array with babel-polyfill as the first item)
    entry: [
      'babel-polyfill',
      './src/app.js'
    ],
    // What are the details of the output file?
    output: {
      // Where do we put it?
      path: path.join(__dirname, 'public', 'dist'),
      // What should it be called?
      filename: 'bundle.js'
    },
    // What are we doing?
    module: {
      rules: [
        // Transpile JS using .babelrc file
        // $ makes sure the file ends right there (and doesn't include jsx)
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel-loader'
        },
        // Build styles.css file using CSSExtract object from 'extract-text-webpack-plugin'
        // ? says maybe
        {
          test: /\.s?css$/,
          use: CSSExtract.extract({
            use: [{
                loader: 'css-loader',
                options: {
                  importLoaders: 1,
                  sourceMap: true
                }
              },
              'postcss-loader',
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          })
        },
        // This requires 'file-loder' and 'url-loader'; let's us use urls and font types
        {
          test: /\.(png|woff|woff2|eot|ttf|svg)$/,
          loader: 'url-loader?limit=100000'
        }
      ]
    },
    // Any other plugins?
    plugins: [
      // Build styles.css
      CSSExtract
    ],
    // Any sourcemaps for tracking down bugs?
    //devtool: isProduction ? 'source-map' : 'cheap-module-eval-source-map'
    devtool: isProduction ? 'source-map' : 'inline-source-map'
  }
}