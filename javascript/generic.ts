function keysOf<T extends Object>(obj:T):Array<keyof T>{
    return Array.from(Object.keys(obj)) as Array<keyof T>
}

const example = {
    name: 'Alice',
    age: 25,
    isStudent: true,
};

// keysOf 함수를 사용하여 키 배열을 가져옵니다.
const keys = keysOf(example); // keys는 ('name' | 'age' | 'isStudent')[]
console.log(keys); // ['name', 'age', 'isStudent']

Object.keys(example).map((key) => {
    const value = example[key as keyof typeof example];
    return value;
});

const values = Object.keys(example).map((key) => {
    const value = example[key as keyof typeof example];
    return value;
});

// values는 ['Alice', 25, true]가 됩니다.
console.log(values); // ['Alice', 25, true]
