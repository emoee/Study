let a = Infinity;
let b = -Infinity;
let c = NaN;

console.log(c === c);
console.log(NaN === NaN); // 결과값은 false NaN은 어떤 값과도 같지않다. 

console.log(isFinite(a)); // Infinity는 그냥 Infinity
console.log(isFinite('9')); // 숫자로 변환 가능하면 true

// parseInt parseFloat
// 맨 앞부터 숫자로 변환. 만약 맨 앞이 문자라면 NaN
console.log(parseInt('100px')); // 숫자까지만 출력
console.log(parseInt('12.64')); // 정수만 출력
console.log(parseFloat('12.345.6')) // 2번째 점 전까지 출력
console.log(parseFloat('a12.356')) // NaN
console.log(parseInt('0xff', 16)) // 16진수로 읽어들여서 255 출력

