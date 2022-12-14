#!/usr/bin/node
// convert number to another base passed as argument

exports.converter = function (base) { return num => num.toString(base); };
