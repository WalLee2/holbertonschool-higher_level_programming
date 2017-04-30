#!/usr/bin/node

const Rectangle = require('./4-rectangle').Rectangle;
exports.Square = function (size) {
  Rectangle.call(this, size, size);
  this.size = size;
  this.charPrint = function (c) {
    if (c === undefined || c === null) {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  };
};
exports.Square.prototype = Object.create(Rectangle.prototype);
exports.Square.prototype.constructor = exports.Square;
