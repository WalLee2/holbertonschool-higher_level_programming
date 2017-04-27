#!/usr/bin/node

if (Number(process.argv[2])) {
    let usrIn = Number(process.argv[2]);
    let myStr = 'X';
    for (let i = 1; i < usrIn; i++) {
      myStr = myStr + 'X';
    }
    for (let a = 0; a < usrIn; a++) {
      console.log(myStr);
    }
} else {
    console.log('Missing size');
}
