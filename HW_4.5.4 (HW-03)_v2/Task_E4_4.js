
function ElectricalAppliance() {
    this.isOn = false;
}

ElectricalAppliance.prototype.plugIn = function () {
    this.isOn = true;
    console.log("Appliance is plugged in and switched on");
};

ElectricalAppliance.prototype.unplug = function () {
    this.isOn = false;
    console.log("Appliance is unplugged and switched off");
};


function TableLamp() {
    ElectricalAppliance.call(this);
    this.wattage = 40;
    this.isLit = false;
}

TableLamp.prototype = Object.create(ElectricalAppliance.prototype);

TableLamp.prototype.lit = function () {
    this.isLit = true;
    console.log("Table lamp is lit");
};

TableLamp.prototype.unlit = function () {
    this.isLit = false;
    console.log("Table lamp is unlit");
};


function Computer() {
    ElectricalAppliance.call(this);
    this.wattage = 350;
    this.isRunning = false;
}

Computer.prototype = Object.create(ElectricalAppliance.prototype);

Computer.prototype.start = function () {
    this.isRunning = true;
    console.log("Computer is started");
};

Computer.prototype.shutDown = function () {
    this.isRunning = false;
    console.log("Computer is shut down");
};


let myTableLamp = new TableLamp();
let myComputer = new Computer();

// 4 Checking the results

myTableLamp.plugIn();
myTableLamp.lit();

myComputer.plugIn();
myComputer.start();


console.log(`My table lamp is consuming ${myTableLamp.wattage} Watts`);
console.log(`My computer is consuming ${myComputer.wattage} Watts`);


myComputer.unplug();
myTableLamp.unplug();