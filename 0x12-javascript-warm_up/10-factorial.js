#!/usr/bin/node
const x = process.argv[2];

if (x === undefined || isNaN(x)) {
  console.log(parseInt('1'));
} else {
  function factorial (x) {
    if (x === 0 || x === 1) {
      return 1;
    } else { return (x * factorial(x - 1)); }
  }
  console.log(factorial(Number(x)));
}
