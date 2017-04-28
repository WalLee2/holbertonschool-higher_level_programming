#!/usr/bin/node

function factorial (a) {
  if (a) {
    let usrIn = Number(process.argv[2]);
    let count = 1;
    for (let i = usrIn; i > 0; i--) {
      count = usrIn * count;
      usrIn--;
    }
    return (count);
  } else {
    return (1);
  }
}

console.log(factorial(process.argv[0]));
