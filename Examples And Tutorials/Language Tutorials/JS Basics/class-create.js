class Rectangle {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }

    perimeter() {
        return 2*(this.height + this.width);
    }

    area() {
        return this.height * this.width;
    }
}


let rec = new Rectangle(5, 10)
console.log(rec)
console.log(rec.area());
console.log(rec.perimeter());

