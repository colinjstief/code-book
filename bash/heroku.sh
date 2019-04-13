## Help
heroku --Help

## Login
heroku login

## SSH keys
heroku keys:add
keroku keys # list them all
heroku keys:remove colin.stief@gmail.com
ssh -v git@heroku.com # check ssh connection

## Setup environments

#
## package.json
#
# "scripts": {
#     "start": "node server/server.js",
#     "test": "export NODE_ENV=test || \"SET NODE_ENV=test\" && mocha server/**/*.test.js",
#     "test-watch": "nodemon --exec \"npm test\""
# }
# "engines": {
#     "node": "8.2.1"
# }

#
## config/config.js
#
# let env = process.env.NODE_ENV || 'development';
# console.log('env ******', env);
#
# if (env === 'development') {
#     process.env.PORT = 3000;
#     process.env.MONGODB_URI = 'mongodb://localhost:27017/TodoApp'
# } else if (env == 'test') {
#     process.env.PORT = 3000;
#     process.env.MONGODB_URI = 'mongodb://localhost:27017/TodoApp'
# }

## Create App
heroku create # cwd is your web app

## Add mongodb service to Heroku app
heroku addons:create mongolab:sandbox
heroku config ## this is where the uri for our mongo db lives


## push to github
git push heroku master

## heroku configuration
heroku config
heroku config:set KEY=VALUE
heroku config:get KEY
heroku config:unset KEY

## heroku logs
heroku logs

## Connecting to MongoDB database from Robo3T
mongodb://heroku_62fkftnh:c3o5ii0ui1bp53b189aksh4mgr@ds121674.mlab.com:21674/heroku_62fkftnh
mongodb://  heroku_62fkftnh : c3o5ii0ui1bp53b189aksh4mgr @ ds121674.mlab.com  21674  heroku_62fkftnh

Address: ds121674.mlab.com
Port: 21674
Database: heroku_62fkftnh
Username: heroku_62fkftnh
Password: c3o5ii0ui1bp53b189aksh4mgr
