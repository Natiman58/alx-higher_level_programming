#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let element;
  for (element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
