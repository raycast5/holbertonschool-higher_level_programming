#!/usr/bin/node
// Script that returns the second biggest number

const argc = process.argv.length;
const arr = [];
let res;

if (argc < 4) {
  console.log(0);
} else {
  for (let i = 2; i < argc; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  arr.sort(function compareNumbers (a, b) { return a - b; });
  res = arr[arr.length - 2];
  console.log(res);
}
