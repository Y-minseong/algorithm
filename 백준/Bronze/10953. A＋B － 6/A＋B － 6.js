const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().split('\n');

const T = parseInt(input);

for (i = 1; i <= T; i++) {
    let number = input[i].split(',');
    const A = parseInt(number[0]);
    const B = parseInt(number[1]);
    console.log(A + B);
}
