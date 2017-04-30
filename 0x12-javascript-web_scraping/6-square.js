#!/usr/bin/node

const s = require('./5-square').Square;
exports.Square = function (size) {
  s.call(this, size);
};
exports.Square.prototype = Object.create(exports.Square.prototype);
exports.Square.prototype.constructor = exports.Square;

exports.Square.prototype.charPrint = function (c) {
  if (c === undefined || c === null) {
    for (let i = 0; i < this.size; i++) {
      console.log('X'.repeat(this.size));
    }
  } else {
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
