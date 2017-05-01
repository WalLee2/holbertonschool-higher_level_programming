#!/usr/bin/node

var request = require('request');
request(process.argv[2], function (error, response) {
  if (error) {
    console.log('code:', error.statusCode);
  } else {
    console.log('code:', response.statusCode);
  }
});
