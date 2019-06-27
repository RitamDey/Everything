/**
 * Initialization and Creation of object using constructor function.
**/


// Creating a constructor function
function Square(side) {
    this.side = side;
    this.area = side*side;
}


var sq = new Square(5);  // New object

console.log(sq, sq.area);


// Adding properties on the fly
sq.perimeter = 4*sq.side;
console.log(sq.perimeter);
