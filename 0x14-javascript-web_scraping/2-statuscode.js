#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const  request = require("request");
request(url, function(err, response) {
  console.log('code:', response && response.statusCode);
  if (err) {
    console.log(err);
  }
});
