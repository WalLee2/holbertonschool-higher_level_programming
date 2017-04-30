#!/usr/bin/node

exports.Rectangle = function (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  this.rotate = function () {
    let temp = w;
    w = h;
    h = temp;
  };
  this.double = function () {
    w = w * 2;
    h = h * 2;
  };
  this.print = function () {
    for (let i = 0; i < h; i++) {
      console.log('X'.repeat(w));
    }
  };
};
