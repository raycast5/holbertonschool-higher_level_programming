#!/usr/bin/node
// Prints the numberof arguments already printed

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
