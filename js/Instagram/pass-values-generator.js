/*    JS: Pass values into generator functions */


function* gen() {
    while(true) {
        console.log(value)
        let value = yield 'fixed';
        /**
         * This generator always returns a fixed value but you
         * can use passed value inside of the function.
         */
        console.log(value);
    }
}


const g = gen();

console.log(g.next('value1'));
console.log(g.next('value2'));
