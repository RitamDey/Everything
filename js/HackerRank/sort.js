var arr = ['c', 'a', 'd', 'b', 'aa'];


arr.sort(
    function (x, y) { 
        return x<y;
    }
);

// arr.sort((x, y) => x<y);  // Using lambdas


console.log(arr);
