#!/usr/bin/node
// Creates a class Square that inherits from Square

const Square = require('./5-square');
const Parent = Square;
module.exports = class Square extends Parent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
