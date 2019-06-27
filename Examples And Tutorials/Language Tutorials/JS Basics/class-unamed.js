let Rectangle = class {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }

    area() {
        return this.height*this.width;
    }
}


console.log(Rectangle);
const rec = new Rectangle(5, 15);
console.log(rec.area());
