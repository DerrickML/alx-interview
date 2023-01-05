#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + filmId + '/';

function printMovieCharacters (url) {
  request(url, async function (error, response, body) {
    if (error) return console.log('An error occurred');

    const characters = JSON.parse(body).characters;
    if (!characters) return;

    const promises = [];

    for (const ch of characters) {
      let promise = null;

      promise = new Promise(function (resolve, reject) {
        request(ch, function (error, response, body) {
          if (error) return console.log('Error fetching character');
          resolve(JSON.parse(body).name);
        });
      });
      promises.push(promise);
    }

    const data = await Promise.all(promises);
    for (const item of data) {
      console.log(item);
    }
  });
}

printMovieCharacters(url);
