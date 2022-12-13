#!/usr/bin/node
// Calls a function x amount of times

module.exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
