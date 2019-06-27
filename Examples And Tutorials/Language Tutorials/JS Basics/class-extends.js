'use strict';

class Animal {
    constructor(name) {
        this.name = name;
    }
}


class Dog extends Animal {
    function bark() {
        console.log(this.name+" Barked!!\n");
    }
}


var dash = new Animal("Tommy");
console.log(dash.name);
dash.bark();
