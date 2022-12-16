#!/usr/bin/node
// Retreives data from given url and stores it in given filepath

const request = require('request');
const url = process.argv[2];
const filepath = process.argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filepath, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
