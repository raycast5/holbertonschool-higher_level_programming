#!/usr/bin/node
// script that concats 2 arguments using is

const arg1 = process.argv[2];
const joiner = 'is';
const arg2 = process.argv[3];
const Cstring = arg1 + ' ' + joiner + ' ' + arg2;

console.log(Cstring);
