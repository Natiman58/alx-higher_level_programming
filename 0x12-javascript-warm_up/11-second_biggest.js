#!/usr/bin/node
const num = process.argv[2];
const array = (process.argv).slice(2).map(Number);
const sortedArray = array.sort(function (a, b) { return a - b; });

if (num === undefined || num === '1') {
  console.log('0');
} else {
  console.log(sortedArray[4]);
}
