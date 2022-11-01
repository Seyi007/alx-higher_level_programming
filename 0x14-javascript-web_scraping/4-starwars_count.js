#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let i = 0;
    const results = JSON.parse(body).results;
    for (let j = 0; j < results.length; j++) {
      const chars = results[j].characters;
      for (let k = 0; k < chars.length; k++) {
        if (chars[k].includes('/18/')) {
          i++;
      }
     }
    }
    console.log(i);
  }
});
