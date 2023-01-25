class ElectricTools{
    constructor (pwc, selectOn) {
    this.name = 'name',
    this.pwc = pwc,
    this.selectOn = true
}
}

class WlessLamp extends ElectricTools {
    constructor(name, pwc, selectOn) {
        super(pwc, selectOn);
        this.name = 'lamp'
        this.selectOn = true

}
}

class Comp extends ElectricTools {
    constructor(name, pwc, selectOn){
        super(pwc, selectOn);
    this.name = 'comp'
    this.selectOn = false

}
}



const lamp = new WlessLamp('lamp', selectOn = true, 50);
const comp = new Comp('comp', 350);


let a = comp.pwc;
let b = lamp.pwc

if (comp.selectOn === true) {
    a = 350
} else {
    a = 0
}

if (lamp.selectOn === true) {
    b = 50
} else {
    b = 0
}
const powCons = function(a, b) {
    return a + b;
}
console.log(`Total power consumption is going be ${powCons} watts`)


console.log(comp, lamp)
console.log(`Total power consumption if both device is \'ON'\ going be ${sumPwc} watts`)