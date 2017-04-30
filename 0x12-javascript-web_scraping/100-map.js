#!/usr/bin/node

const data = require('./100-data').list;
console.log(data);
var multiply = data.map(function(num) {
  num = num - 1;
  return (num * data[num])
});
console.log(multiply);
