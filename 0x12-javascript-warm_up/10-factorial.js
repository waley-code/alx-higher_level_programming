#!/usr/bin/node
const args = process.argv.slice(2);
const first = parseInt(args[0]);

function add (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * add(a - 1);
  }
}

console.log(add(first));
