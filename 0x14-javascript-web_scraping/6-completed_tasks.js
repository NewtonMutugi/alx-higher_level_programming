#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    for (const task of json) {
      if (task.completed === true) {
        if (task.userId in dict) {
          dict[task.userId] += 1;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
}
);
