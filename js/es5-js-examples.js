"use strict"   // Forces the interpreter to use ES5 modifications

/**
 * Data Types in JS are as follows:
 * "number" for numbers, integers or floating point
 * "string" for strings
 * "boolean" for boolean values: true or false
 * "null" and "undefined" for unknown and undefined values - a standalone type like `None` in Python
 * "object" for complex data structures
 * "symbol" for unique identifiers, works like enum in C

 * The `typeof()` function returns the type of the argument as a string
 * Conversions can be found at: https://javascript.info/type-conversions
**/
let name = "Ritam";
// name = "Ritam";   // Strict mode prevents this kind of variable declarations

// The `` is similar to the f"" in Python. It allows for string interpolation
const GREETINGS = `Hello ${name}`  // This is the method to declare constants in ES5+
console.log(GREETINGS);

let y = 2;
console.log(`Setting y=${y}`);
let x = 1 + (y *= 2);  // One type of use of the assignment operator. Assignment operator always the returns the value that is assigned
console.log(`Value of x=${x} and y=${y}`);

console.log("02" == 2);  // This equates to true as JS does type juggling like PHP. Here "02" becomes 2
console.log("02" === 2);  // Strit equality operator prevents the above mentioned type juggling
