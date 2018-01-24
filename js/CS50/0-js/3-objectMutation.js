const o = {
    a: 'a',
    b: 'b',
    obj: {
        key: 'key',
    }
}


// Shallow copying of Objects
const o2 = Object.assign({}, o)  // Create a new object and set it same to o

o2.obj.key = "new key";


// Since its a shallow copy the internal object is copied rather created
// from the original with the original values
console.log(o.obj.key);


// Deep copying of objects
function deepCopy(obj) {
    // check if vals are objects
    // if so, copy that object (deep copy)
    // else return the value
    const keys = Object.keys(obj);

    const newObj = {}
    for(let i=0; i < keys.length; ++i) {
        if (typeof obj[keys[i]] === 'object')
            newObj[keys[i]] = deepCopy(obj[keys[i]]);
        else
            newObj[keys[i]] = obj[keys[i]];
    }
    return newObj;
}


const o3 = deepCopy(o);

o3.obj.key = "very new key";


console.log(o3);
console.log(o);
