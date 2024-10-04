// 문자형으로 변환
let value = true;
console.log(value, typeof value)
value = String(value)
console.log(value, typeof value)

// 숫자형으로 변환
let str = "9291913"
let str2 = "23a4"
let str3 = true
console.log(str, typeof str)
str = Number(str)
str2 = Number(str2)
str3 = Number(str3)
console.log(str, typeof str)
console.log(str2, typeof str2) // 문자열이 있으면 결과는 NaN
console.log(str3, typeof str3) // true = 1, false = 0

// 불린형으로 변환
let b = "hello"
let b2 = ""
let b3 = "0"
let b4 = 0
b = Boolean(b)
b2 = Boolean(b2)
b3 = Boolean(b3)
b4 = Boolean(b4)
console.log(b, typeof b)
console.log(b2, typeof b2) // 빈 문자열, NaN, null, nudefined, 0은 false
console.log(b3, typeof b3) // 문자 0은 true
console.log(b4, typeof b4) // 숫자 0은 false