#!/usr/bin/node
// kefaslungu
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
