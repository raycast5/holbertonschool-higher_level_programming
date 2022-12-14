#!/usr/bin/node
// Creates a class Square that inherits from Square

const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }
};
