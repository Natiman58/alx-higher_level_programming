#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const array = (process.argv).slice(2).map(Number);
  const sortedArray = array.sort(function (a, b) { return b - a; });
  console.log(sortedArray[1]);
}
