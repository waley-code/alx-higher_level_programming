#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    let result = '';
    let quotient = number;

    while (quotient > 0) {
      const remainder = quotient % base;
      quotient = Math.floor(quotient / base);
      if (remainder < 10) {
        result = remainder.toString() + result;
      } else {
        result = String.fromCharCode(remainder + 87) + result;
      }
    }

    return result || '0';
  };
};
