#!/usr/bin/node
// Creates a class Square that inherits from Square

const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.height));
    }
  }
};
