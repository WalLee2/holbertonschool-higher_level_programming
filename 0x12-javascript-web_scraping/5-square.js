#!/usr/bin/node

const Rectangle = require('./4-rectangle').Rectangle;
const Square = function (size) {
  Rectangle.call(this, size, size);
  this.size = size;
};
Square.prototype = Object.create(Rectangle.prototype);
Square.constructor = Square;

exports.Square = Square;
