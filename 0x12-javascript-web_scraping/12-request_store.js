#!/usr/bin/node

const fs = require('fs');
const request = require('request');
request(process.argv[2], function (error, pass, body) {
  fs.writeFile(process.argv[3], body, 'utf-8', function (fail) {
    if (error) {
      return (console.log(error));
    }
  });
});
