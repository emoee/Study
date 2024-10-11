let data_list = [
    {type: 'number'},
    false, 
    // x => Math.pow(x, 3) // 오류 타입을 명시하지 않아서.
    (x: number) => Math.pow(x,3)
];

console.log(data_list)

let olimpic_newgame = [
    {
        'name' : '쇼트트랙',
        'type' : '혼성 계주'
    },
    true
];

console.log(olimpic_newgame);

// 타입 가드 예시
if (typeof olimpic_newgame[0] === 'object' && olimpic_newgame[0] != null){
    console.log(olimpic_newgame[0].name);
}

// 타입 단언
console.log((olimpic_newgame[0] as {name: string; type: string;}).name)

export {};