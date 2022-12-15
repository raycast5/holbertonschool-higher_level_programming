#!/usr/bin/node
// Reads a file and writes its contents to stdout

const fs = require('fs');
const fname = process.argv[2];

fs.readFile(fname, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
