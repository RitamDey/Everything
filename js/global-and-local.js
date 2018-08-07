/**
    Variables in JS are declared in global scope without the `var` keyword
 */

var thisIsGlobal = "Global variable";


function declareGlobal() {
    // Without the `var` ketword this variable is in global scope
    newGlobal = "New global variable";
}


function print() {
    declareGlobal();

    console.log(thisIsGlobal);
    console.log(newGlobal);
}


print();