#!/usr/bin/node
// Returns the number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (const item of list) {
    if (item === searchElement) {
      ++occur;
    }
  }
  return occur;
};
