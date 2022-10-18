#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

function readData (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}

fs.readFile(file, 'utf-8', readData);
