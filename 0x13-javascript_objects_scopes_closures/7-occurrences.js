#!/usr/bin/node
/**
 * function to count number of occurrences in a list
 * @param {list} list - list to search in
 * @param {number} searchElement - element to search for
 * @returns {number} number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(element => {
    if (element === searchElement) {
      count++;
    }
  });
  return count;
};
