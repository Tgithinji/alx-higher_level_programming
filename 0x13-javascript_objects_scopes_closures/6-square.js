#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c = 'X') {
    let rect = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rect += c;
      }
      if ((i + 1) === this.height) {
        break;
      }
      rect += '\n';
    }
    console.log(rect);
  }
}

module.exports = Square;
