// 0 대신 사용하는 e
let billion = 1000000000;
let billionE = 1e9;
console.log(billion, billionE);

let a = 1e3;
let aa = 1*1000;
let b = 0.001;
let bb = 1e-3;
console.log(b, bb);

// 16진수 색상, 문자인코딩 시 사용
let c = 0xff;
let cc = 0xFF;

// 2진수
let t = 0b11111111;
let e = 0o377;
console.log(t==e);

// 문자형, 진법 사용
let num = 255;
console.log(num.toString(16));
console.log(num.toString(2))
console.log(255..toString(2)) // 숫자에 메소드 사용은 점 2개




