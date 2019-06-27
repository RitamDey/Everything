// Use destructuring to obtain the length of the input string str, and assign the length to len in line.


function getLength(str) {
    const { length: len } = str;

    return len;
}


console.log(getLength("Hello"));
console.log(getLength("FreeCodeCamp") === "FreeCodeCamp".length);
