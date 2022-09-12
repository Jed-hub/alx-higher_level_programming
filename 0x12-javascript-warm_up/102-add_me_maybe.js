#!/usr/bin/node
// execute x times a function

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
