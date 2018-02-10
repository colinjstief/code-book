////
//// Create file via 'Filesystem' module
////

var file_system = require("fs");
// [1] path, name; [2] contents
file_system.writeFile(__dirname + "/index.html","<h1>Hello world!<h1>");

////
//// Pull down image file to hard drive
////
var https = require("https");

var img_url = "https://cicresources.blob.core.windows.net/images/CC-NMSF%20logo%20for%20storymap.png";
// [1] path, name
var img_file = file_system.createWriteStream(__dirname + "/node-img.png"); 
// [1] url; [2] action
var request = https.get(img_url, function(response){
    response.pipe(img_file);
});