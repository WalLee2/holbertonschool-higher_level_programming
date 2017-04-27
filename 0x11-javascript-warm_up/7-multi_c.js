#!/usr/bin/node

if (Number(process.argv[2])) {
  let usrIn = Number(process.argv[2]);
  for (let i = 0; i < usrIn; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
