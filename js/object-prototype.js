/**
 * The Prototype Property
 * The drawback of internally defining the getInformation function is that
 * it recreates that function every time we create a new Fruit object.
 * Fortunately, every function in JavaScript has something called a
 * prototype property, which is empty by default. We can think of a
 * function's prototype as an object blueprint or paradigm; when we add
 * methods and properties to the prototype, they are accessible to all
 * instances of that function. This is especially useful for inheritance
 * (discussed below).
 *
 * We can add a function to our constructor function's prototype like so:
**/


'use strict';


function Square(side) {
    this.side = side;
}

Square.prototype.area = function() {
    return this.side * this.side;
}

Square.prototype.perimeter = function() {
    return 4 * this.side;
}


const sq = new Square(5);
console.log(sq);
console.log(sq.area());
console.log(sq.perimeter());
