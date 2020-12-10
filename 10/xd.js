// --- Day 10: Adapter Array ---

let memo = []
const fs = require('fs');
fs.readFile("input", 'utf8', (err, data) => {
    if (err) throw err;
    data = data.trim().split('\n').map(item => parseInt(item));
    data.sort((a, b) => a-b);
    data.push(data[data.length - 1] + 3)
    console.log(data)
    initialize(data);
    let res = adapterCalc(data, 0)
    console.log(res)
}); 


const initialize = data => {
    for(let i = 0; i < data[data.length - 1]; i++) {
        memo.push(null);
    }
}

const adapterCalc = (arr, start) => {
    let current = start
    let counter = 0

    if (current === arr[arr.length - 1]) {
        return 1;
    }
    if (memo[current] !== null) {
        return memo[current];
    }

    for (let j = 1; j < 4; j++) {
        let joltj = current + j; 
        if (arr.includes(joltj)) {
            let resj = adapterCalc(arr, joltj);
            memo[joltj] = resj;
            counter += resj;
        }

    }
    return counter
}
