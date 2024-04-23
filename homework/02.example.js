// Devloper: Angel Smythe   

let n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log({size: n.length})

// Procedural
for(let i = 0; i < n.length; i++){
    console.log({i});
}

// Functional
n.forEach( e=>console.log({e:e * 2}));
n.forEach( booboo=>console.log({booboo}));

n.filter( e => e > 2).forEach( x => console.log ({x}));

let m = n.filter( e => e > 5);
console.log({m});