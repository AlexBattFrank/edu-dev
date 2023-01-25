

const obj2 = {
    prop2: "prop3",
    prop4: "prop5"
}
function selfKey(object){
    console.log(Object.keys(object))
    console.log(Object.values(object))
}
selfKey(obj2)
