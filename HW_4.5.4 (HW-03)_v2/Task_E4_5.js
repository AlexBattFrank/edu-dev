
class ElectricalAppliance {
    constructor() {
        this.isOn = false;
    }

    plugIn() {
        this.isOn = true;
        console.log("Appliance is plugged in and switched on");
    }

    unplug() {
        this.isOn = false;
        console.log("Appliance is unplugged and switched off");
    }
}

class TableLamp extends ElectricalAppliance {
    constructor() {
        super();
        this.wattage = 40;
        this.isLit = false;
    }

    lit() {
        this.isLit = true;
        console.log("Table lamp is lit");
    }

    unlit() {
        this.isLit = false;
        console.log("Table lamp is unlit");
    }
}

class Computer extends ElectricalAppliance {
    constructor() {
        super();
        this.wattage = 350;
        this.isRunning = false;
    }

    start() {
        this.isRunning = true;
        console.log("Computer is started");
    }

    shutDown() {
        this.isRunning = false;
        console.log("Computer is shut down");
    }
}


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