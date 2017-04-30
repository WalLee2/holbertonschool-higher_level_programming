#!/usr/bin/node

var request = require('request');
request('http://swapi.co/api/films/' + process.argv[2], function (err, res) {
  if (res) {
    let parsed = JSON.parse(res.body);
    console.log(parsed.title);
  } else {
    console.log(err);
  }
});
