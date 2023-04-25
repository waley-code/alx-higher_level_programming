#!/usr/bin/node
// dfddfdgdgi
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach((film) => {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });
  console.log(`${count}`);
});
