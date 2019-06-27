function sumAll() {
    let sum = 0;

    // for-of iterator yeilds all the values in a iterator
    for(let val of arguments) {
        //console.log(val, typeof val)
        sum += val;
    }

    return sum;
}


console.log(sumAll(2, 3));
console.log(sumAll(2, 3, 5));
console.log(sumAll(6, 8, 3, 2));

