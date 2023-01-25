
const someObj = {
    first: 1,
    second: 'bar'
};
const d = 'first'
const b = 'ban'
function oneFunc(a, someObj) {
    return a  in someObj;
}
console.log(oneFunc(d, someObj))
console.log(oneFunc(b, someObj))