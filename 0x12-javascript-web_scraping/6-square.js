#!/usr/bin/node

const s = require('./5-square').Square;
exports.Square = function (size) {
  s.call(this, size);
};

exports.Square.prototype = Object.create(exports.Square.prototype);
exports.Square.constructor = exports.Square;

exports.Square.prototype.charPrint = function (c = 'X') {
  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};
