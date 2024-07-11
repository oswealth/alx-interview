#!/usr/bin/node
/**
  * prints all characters of a Star Wars movie
  */

const args = process.argv;
const request = require('request');
const API = `https://swapi-api.hbtn.io/api/films/${args[2]}`;

// Call the Star Wars API
request.get(API, async (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
  } else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      await getCharacterName(characters[i]);
    }
  }
});

/** Calls the API to get the character info */
function getCharacterName (character) {
  return new Promise((resolve, reject) => {
    request.get(character, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.error('Error:', error || `Status code: ${response.statusCode}`);
        reject(error);
      } else {
        const characterInfo = JSON.parse(body);
        console.log(characterInfo.name);
        resolve(true);
      }
    });
  });
}
