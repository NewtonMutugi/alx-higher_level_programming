#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  arr.sort(function (a, b) { return a - b; });
  console.log(arr[arr.length - 2]);
}
