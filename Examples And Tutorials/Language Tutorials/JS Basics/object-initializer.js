/**
 * Example of Object Initialization using Java like notation
**/


var obj = new Object();  // Create a blank object

// Adding properties on the fly
obj.len = 4;
obj.width = 5;
obj.area = function(x, y) {
    return x*y;
}

// Testing the properties added
console.log(obj.area(obj.len, obj.width))
console.log(obj);
