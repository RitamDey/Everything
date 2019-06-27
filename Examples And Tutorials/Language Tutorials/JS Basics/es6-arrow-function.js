// Arrow function are used in JS6 to create inline functions


// Old way
let magic = function () {
	"use strict"

	return new Date();
}

// With arrow function
let magicInline = () => {
	"use strict"

	return new Date();
}


console.log(magic());
console.log(magicInline());
