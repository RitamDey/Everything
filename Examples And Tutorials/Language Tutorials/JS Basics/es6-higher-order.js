// Example of usage of arrow functions on higher order function like map(), reduce(), filter()

const realNumberArray = [4, 5.6, -9.8, 3.14, 42, 6, 8.34];


const squareList = (arr) => {
	"use strict";

	const squaredIntger = arr.filter( (num) => (num % parseInt(num) === 0) && (num > 0)).map((num) => Math.pow(num, 2))

	return squaredInteger;
}

const squaredIntegers = squareList(realNumberArray);
console.log(squaredIntegers);
