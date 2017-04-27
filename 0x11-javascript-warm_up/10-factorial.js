#!/usr/bin/node

if (Number(process.argv[2])) {
  let usrIn = Number(process.argv[2]);
  let count = 1
  for (let i = usrIn; i > 0; i--) {
    count = usrIn * count;
    usrIn--;
  }
  console.log(count);
} else {
  console.log("1");
}
