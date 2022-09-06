#!/usr/bin/node

const array = require('./100-data').list;
const map1 = array.map((element, index) => element * index);

console.log(array);
console.log(map1);
