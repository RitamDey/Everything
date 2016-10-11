class Greeter {
    greeting: string = "Hello ";
    constructor(message: string) {
        this.greeting += message;
    }
    greet() {
        console.log(this.greeting);
    }
}

let obj = new Greeter("Joe")
obj.greet()
