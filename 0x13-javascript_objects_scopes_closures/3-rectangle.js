#!/usr/bin/node

class Rectangle {
  // an empty class Rectangle that defines a rectangle:
  constructor (w, h) {
    if (w && h) {
      if (!(h <= 0 || w <= 0)) {
        this.width = w;
        this.height = h;
      }
    }
    this.print = function () {
      for (let index = 0; index < h; index++) {
        let x = '';
        for (let ind = 0; ind < w; ind++) {
          x += 'X';
        }
        console.log(x);
      }
    };
  }
}

module.exports = Rectangle;
