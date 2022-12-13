#!/usr/bin/node
// Script to factorialize and print a number

const num = process.argv[2];

function factorial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(parseInt(num)));
