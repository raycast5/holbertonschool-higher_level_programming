#!/usr/bin/node
// Added a funcion that increments the integer value

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
myObject.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
