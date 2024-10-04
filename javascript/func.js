function showCount(count){
    console.log("--", count ,"--")
    console.log(count ?? "unknown") // ?? 연산자로 falsy값 처리 가능
    count = count || "no given" // 0도 처리
    console.log(count)
}

showCount(0);
showCount(null);
showCount();

// 함수표현식은 변수안에 할당되기 때문에 세미콜론이 필요하다.
function sayHi(){
    // 함수 선언문
    // 함수를 선언하기 전에 사용해도 가능하다.
}
let sayHi = function(){
    // 함수 표현식
};

