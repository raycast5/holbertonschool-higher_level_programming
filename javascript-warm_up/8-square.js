#!/usr/bin/node
// script that prints a square of x size

const size = parseInt(process.argv[2]);
let row = 'X';

if (isNaN(size)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 1; j < size; j++) {
    row += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
