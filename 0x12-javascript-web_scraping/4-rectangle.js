#!/usr/bin/node

exports.Rectangle = function (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  this.rotate = function () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  };
  this.double = function () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  };
  this.print = function () {
    for (let i = 0; i < h; i++) {
      console.log('X'.repeat(w));
    }
  };
};
