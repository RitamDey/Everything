const str = "<div id=\"my-id\" class=\"my-class\">"

// Using regex substitute < or > or " with "" and split by " "
const arr = str.replace(/[<>"]/g, "").split(' ');
console.log(arr);

const tag = arr[0];


const attrs = arr.slice(1).reduce(
        (res, v) => {
            const keyValue = v.split("=");
            res[keyValue[0]] = keyValue[1];
            return res;
        }, {}
)


console.log({tag, attrs});
