#!/usr/bin/node
// script that converts 1st arg to number

const res = parseInt(process.argv[2]);

if (isNaN(res)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + res);
}
