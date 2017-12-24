'use strict';


process.stdin.resume();
process.stdin.setEncoding('utf-8');

let currentLine = 0;
let inputString = '';

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split("\n").map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/**
  * Modify and return the array so that all even numbers are doubled
  * And all odd numbers are tripled

  * Parameter(s):
  * nums: An array of numbers.
**/
function modifyArray(nums) {
    return nums.map((n) => { if(n%2) return n*3; else return n*2; });
}


function main() {
    const n = +(readLine());
    const a = readLine().split(' ').map(Number);

    console.log(modifyArray(a).toString().split(",").join(' '));
}
