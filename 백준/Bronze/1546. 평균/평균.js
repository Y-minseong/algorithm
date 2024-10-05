const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

// 첫 번째 줄은 시험 본 과목 수 N, 두 번째 줄은 점수 배열
const N = parseInt(input[0]);
const scores = input[1].split(' ').map(Number);

// 최대 점수를 찾음
const maxScore = Math.max(...scores);

// 각 점수를 변환하고 합계를 구함
const newScores = scores.map(score => (score / maxScore) * 100);

// 변환된 점수들의 평균 계산
const average = newScores.reduce((a, b) => a + b, 0) / N;

console.log(average);
