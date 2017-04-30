#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, res, body) {
  if (body) {
    let parsed = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < parsed.results.length; i++) {
      if (parsed.results[i].characters) {
        let string = parsed.results[i].characters;
        for (let a = 0; a < string.length; a++) {
          if (string[a].includes('/18/')) {
            count++;
          }
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
