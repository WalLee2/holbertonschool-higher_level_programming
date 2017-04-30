#!/usr/bin/node

const Rectangle = require('./4-rectangle').Rectangle;
exports.Square = function (size) {
  Rectangle.call(this, size, size);
  this.size = size;
};
exports.Square.prototype = Object.create(exports.Rectangle.prototype);
exports.Square.prototype.constructor = exports.Square;
