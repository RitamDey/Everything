'use strcit';


process.stdin.resume();
process.stdin.setEncoding('utf-8');


let inputString = '';
let currentLine = 0;


process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}


function rev(s) {
    let x;
    
    try {
        x = s.split("").reverse().join("");
    }
    catch(e) {
        console.log(e.message);
    }
    finally {
        console.log(x);
    }

}


function main() {
    const s = eval(readLine());

    rev(s);
}
