#!/usr/bin/node
const args = process.argv.slice(1);
let num = 0;
let prev = 0;

if (args.length <= 1) {
  console.log(prev);
} else {
  args.forEach(el => {
    if (el > num) {
      prev = num;
      num = el;
    }
  });
  console.log(prev);
}
