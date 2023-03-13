#!/usr/bin/node
const args = process.argv.slice(1);
const first = parseInt(args[0]);

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(first));
