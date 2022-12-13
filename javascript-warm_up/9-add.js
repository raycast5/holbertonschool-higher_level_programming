#!/usr/bin/node
// script that adds a and b

const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(a, b));
