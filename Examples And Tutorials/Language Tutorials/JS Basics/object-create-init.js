/**
 * Creating an object using the Object create method.
 * This method uses pre-existing objects
**/


// Creating a object
var square = {
    side: 5,
    area: function() {
        return this.side*this.side;
    }
}


// Creating another object based on the pre-existing object
var sq = Object.create(square);
sq.side = 10;


console.log("Original object: ", square);
console.log("Area is: ", square.area());


console.log("New object: ", sq);
console.log("Area is: ", sq.area());


// Adding a property on the fly
sq.perimeter = function() {
    return 4*this.side;
}

console.log("Perimeter is: ", sq.perimeter());
