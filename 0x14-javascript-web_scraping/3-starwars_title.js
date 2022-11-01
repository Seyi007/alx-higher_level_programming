#!/usr/bin/node
const argv = process.argv;
const id = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const title = JSON.parse(body);
    console.log(title.title);
  }
});
