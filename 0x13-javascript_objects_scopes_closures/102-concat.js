#!/usr/bin/node
const fs = require('fs');
const argv = process.argv.slice(2);

let data = '';
fs.readFile(argv[0], (err, fileData) => {
  if (err) {
    return;
  }
  data = fileData.toString();

  fs.readFile(argv[1], (err, fileData2) => {
    if (err) {
      return;
    }
    data += fileData2.toString();

    fs.writeFile(argv[2], data, () => {
    });
  });
});
