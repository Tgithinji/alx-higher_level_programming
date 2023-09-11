#!/usr/bin/node

const argv = process.argv.slice(2);
const converted = parseInt(argv[0]);

if (isNaN(converted)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${converted}`);
}
