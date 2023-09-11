#!/usr/bin/node

const args = process.argv.slice(2);
const convertedArg = parseInt(args[0]);

if (isNaN(convertedArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convertedArg; i++) {
    console.log('C is fun');
  }
}
