#!/usr/bin/node
// Prints all chars from a given movie from SW Api
const fs = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

fs(url, (a, response, body) => {
  const characters = JSON.parse(body).characters;
  console.log(characters)
  characters.forEach((index) => {
    fs(index, function (a, response, body) {
      const character = JSON.parse(body).name;
      console.log(character);
    });
  });
});
