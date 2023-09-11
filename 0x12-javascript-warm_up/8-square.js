#!/usr/bin/node

const args = process.argv.slice(2);
const convertedArg = parseInt(args[0]);

if (isNaN(convertedArg)) {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = 0; i < convertedArg; i++) {
    for (let j = 0; j < convertedArg; j++) {
      square += 'X';
    }
    if ((i + 1) === convertedArg) {
      break;
    } else {
      square += '\n';
    }
  }
  console.log(square);
}
