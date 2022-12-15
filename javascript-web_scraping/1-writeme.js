#!/usr/bin/node
// Writes a given string to given file

const fs = require('fs');
const fname = process.argv[2];
const content = process.argv[3];

fs.writeFile(fname, content, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
