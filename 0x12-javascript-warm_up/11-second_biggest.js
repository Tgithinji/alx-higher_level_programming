#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort(function (a, b) {
    return a - b;
  });
  console.log(sortedArgs[sortedArgs.length - 2]);
}
