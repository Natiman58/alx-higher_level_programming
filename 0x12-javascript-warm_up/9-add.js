#!/usr/bin/node

if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log('NaN');
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
