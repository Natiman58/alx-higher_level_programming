#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    this.print(c);
  }
}
module.exports = Square;
