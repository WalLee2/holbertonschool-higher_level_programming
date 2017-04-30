#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, pass, body) {
  if (error) {
    return (console.log(error));
  }
  let parsed = JSON.parse(body);
  let myDict = {};
  for (let i = 0; i < parsed.length; i++) {
    if (parsed[i].completed === true) {
      if (myDict[parsed[i].userId]) {
        myDict[parsed[i].userId]++;
      } else {
        myDict[parsed[i].userId] = 1;
      }
    }
  }
  console.log(myDict);
});
