#!/usr/bin/node
// script that checks ifther is arguments

if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
