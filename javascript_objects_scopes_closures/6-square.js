#!/usr/bin/node
// Creates a class Square that inherits from Square

const Square = require('./5-square')

modules.exports = class S1 extends Square {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let block = 'C'
    if (typeof(c) === 'undefined') {
      block = 'X'
    }
    for (let y = 0; y < this.size; y++) {
      console.log(block.repeat(this.size));
    }
  }
};
