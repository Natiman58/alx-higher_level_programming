#!/usr/bin/node
let array = (process.argv).slice(2).map(Number);
let sortedArray = array.sort(function (a, b) { return a - b; });

if (array.length <= 3) {
  console.log('0');
} else { console.log(sortedArray[4]); }
