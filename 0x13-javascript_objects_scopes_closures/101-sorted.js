#!/usr/bin/node
const list = require('./101-data.js').list;
const newList = {};
for (const key in list) {
  if (newList[list[key]] === undefined) {
    newList[list[key]] = [];
  }
  newList[list[key]].push(key);
}
