#!/usr/bin/node

const Rectangle = require('./4-rectangle').Rectangle;
function Square (size) {
  Rectangle.call(this, size, size);
}
exports.Rectangle = Rectangle;
exports.Square = Square;
