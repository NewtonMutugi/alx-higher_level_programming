#!/usr/bin/node
// script that prints all characters of a Star Wars movie:
// Display one character name by line in the same order of the list “characters” in the /films/ response
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body).characters;
    for (const character of json) {
      request(character, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const json = JSON.parse(body);
          console.log(json.name);
        }
      });
    }
  }
}
);
