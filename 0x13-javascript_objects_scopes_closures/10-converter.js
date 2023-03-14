#!/usr/bin/node
/**
 * function to convert a number from base 10 to another base passed as argument
 * @param {number} base - base to convert to
 * @returns {function} function that converts a number
 */
exports.converter = function (base) {
  function convert (number) {
    return number.toString(base);
  }
  return convert;
};

