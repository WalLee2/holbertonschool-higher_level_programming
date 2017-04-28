#!/usr/bin/node

function factorial (a) {
  if (a === 0 || isNaN(a) || a <= 1) {
   return (1);
  }
  return (a * factorial(a - 1));
}
console.log(factorial(Number(process.argv[2])));
