const o = new Object();  // Create a new generic object

o.firstName = "Jordan"
o.lastName = "Hayashi"
o.isTeaching = true
o.greet = function() {
    console.log("Hi!");
}


console.log(o);


const o2 = {}  // New way of creating objects
o2.firstName = "Jordan";
o2["lastName"] = "Hayashi";  // Another way

console.log(o2);


const o3 = {
    firstName: "Jordan",
    lastName: "Hayashi",
    isTeaching: true,
    greet: function() {
        console.log("Hi!");
    },
    address: {
        street: "Main St",
        number: 123,
    }
}  // In-line style of object declaration

console.log(o3)
