#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function (a) {
  return (myObject.value++);
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
