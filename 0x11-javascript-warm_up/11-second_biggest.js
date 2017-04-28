#!/usr/bin/node

let length = process.argv.length;
let myArr = [];
for (let a = 2; a < length; a++) {
  myArr.push(Number(process.argv[a]));
}
if (myArr.length > 1) {
  let hiLow = myArr.sort(function (a, b) { return b - a; });
  console.log(hiLow[1]);
} else {
  console.log('0');
}
