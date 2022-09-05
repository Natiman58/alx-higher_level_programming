#!/usr/bin/node
const x = process.argv[2];

function factorial (x) {
  if (x === 0 || x === 1 || x === undefined || isNaN(x)) {
    return 1;
  } else { return (x * factorial(x - 1)); }
}

console.log(factorial(Number(x)));
