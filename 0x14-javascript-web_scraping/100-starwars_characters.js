#!/usr/bin/node

const request = require('request');

function getCharacters(movieId) {
    return new Promise((resolve, reject) => {
        const url = `https://swapi.dev/api/films/${movieId}/`;
        request.get(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode !== 200) {
                reject(`Failed to fetch movie details. Status code: ${response.statusCode}`);
            } else {
                const movieData = JSON.parse(body);
                resolve(movieData.characters);
            }
        });
    });
}

async function printCharacters(movieId) {
    try {
        const characters = await getCharacters(movieId);
        for (const characterUrl of characters) {
            const characterData = await fetchCharacterData(characterUrl);
            console.log(characterData.name);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function fetchCharacterData(url) {
    return new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode !== 200) {
                reject(`Failed to fetch character details. Status code: ${response.statusCode}`);
            } else {
                const characterData = JSON.parse(body);
                resolve(characterData);
            }
        });
    });
}

const movieId = process.argv[2];

if (movieId) {
   printCharacters(movieId);
} else {
  console.error('Please provide a movie ID as an argument.');
}
