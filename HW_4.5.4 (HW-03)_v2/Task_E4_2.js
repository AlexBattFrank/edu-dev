const someObj = {
    first: 1,
    second: 'bar'
};
const d = 'first'
const b = 'ban'

function checkProperty(string, someObj){
    for(let property in someObj){
        if(property === string){
            return true;
        }
    }
    return false;
}

// 4 Checking the results

console.log(checkProperty(d, someObj)) // true
console.log(checkProperty(b, someObj)) // false