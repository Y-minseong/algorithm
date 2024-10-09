const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 첫 번째 줄은 숫자의 개수 N, 두 번째 줄은 숫자들이 주어짐
const N = parseInt(input[0]);
const numbers = input[1];

// 숫자들을 하나씩 더하는 과정
let sum = 0;
for (let i = 0; i < N; i++) {
    sum += parseInt(numbers[i]);
}

// 결과 출력
console.log(sum);