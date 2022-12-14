#!/usr/bin/node
// reverses list

exports.esrever = function (list) {
  const total = [];
  for (let i = list.length - 1; i >= 0; i--) {
    total.push(list[i]);
  }
  return total;
};
