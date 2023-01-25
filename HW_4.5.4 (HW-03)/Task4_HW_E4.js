function ElectricTools(pwc, selectOn, sumPwc){
    this.name = 'name',
    this.pwc = pwc,
    this.selectOn = true
}
ElectricTools.prototype.switch = function(pwc,selectOn){
    console.log(`Power consumption is ${pwc} watts`)
}

function WlessLamp(name, pwc, selectOn){
    this.name = 'lamp'
    this.pwc = 50
    this.selectOn = true
}

WlessLamp.prototype = new ElectricTools()

function Comp(name, onwire, pwc, wireless){
    this.name = 'comp'
    this.selectOn = true

}

Comp.prototype = new ElectricTools()


const lamp = new WlessLamp('lamp', 50);
const comp = new Comp('comp', 350);

let a = comp.pwc
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
res = comp.pwc + lamp.pwc;

const sumPwc = res
console.log(`Total power consumption is going be ${powCons} watts`)