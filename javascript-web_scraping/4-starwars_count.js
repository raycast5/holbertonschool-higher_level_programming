#!/usr/bin/node
// Retreives count of SW appearances for char id 18

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const chars = films[film].characters;
      for (const char in chars) {
        if (chars[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
