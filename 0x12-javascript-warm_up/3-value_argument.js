#!/usr/bin/node
const args = process.argv.slice(2);

if (args) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
