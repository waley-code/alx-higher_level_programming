#!/usr/bin/node

const { dict } = require('./101-data');

const x = {};

for (const key in dict) {
  const arr = [];
  arr.push(key);
  x[dict[key]] = arr;
}
console.log(x);
