# 4x4x4 3D LED Cube

## Requirements

* Led (Blue looks good)
* Resistors (resistance changes with the LED choosen / Transistor Base)
* 4 - BC547 Transistors (For Layer Selection)
* 2 - 74HC595 Shift Registors (For holding the led output)

* Jumper wires (Male-Male , Male-Female) 
* Solid Core Hookup wires (Most of the wiring)
* German silver wire (Cube Structure)

* Soldering equipment

* 2 Breadboards
* Thermocol sheet

* Any Controller of choise to code

## Manufacturing

### 1. LEDs and Wires

* Check the working of LEDs by attaching resistor to led the to power supply (3.3V or 5V).
* Straighten the German silver wire and cut to length of the Grid Size.


### 2. Setup for Layer

* Print out a square grid of 4x4 on a piece of paper and secure it to thermocol sheet.
* Make holes in the sheet where the grid lines intersect.

### 3. Layer Manufacturing

* Place the LEDs in the holes secuely in a proper pattern.
* Bend the cathode of all the LEDs to one direction.
* Place a German silver wire on a Horizontal Line of cathodes and solder to all of them.
* Do it to all the Horizontal Lines.
* Connect Side Vertically to connect all Horizontal Lines using two German silver wires.
* Manufacture such 4 layers.

![Layers](https://github.com/turrentrock/4x4x4-3D-LED-Cube/master/res/Layers.jpeg)

### 4. Stacking Layers

* Using again the same Thermocol sheet , at the intersection points pierce the wires vertically.
* Now slip down each layer and solder the Anods to the vertial wires.
* For the first layer its simple to do.
* For the next layer take aid of some support to hold it at height and solder the Anods to the Vertical wires.
* Do it for the next layers as well.

![Layers_stacking](https://github.com/turrentrock/4x4x4-3D-LED-Cube/master/res/Layers_assembled.jpeg)

### 5. Circute layout

* Mount the LED cube somwhhere sturdy
* Use breadboads for the circutis
* Referred the design from the references mentioned.
* 6 inputs (3 each for the shift register).
* The shift register (2*8) outputs will be joined to the anodes vertical lines of the cube.
* 4 cathode layers go into a transistor for the layer selection logic.
* Resistors to be placed where the current needs to be limited for the LEDs and transistors.

![CircutieLayout](https://github.com/turrentrock/4x4x4-3D-LED-Cube/master/res/Cube_Connections.jpeg)

### THE END

![LedsGlowing](https://github.com/turrentrock/4x4x4-3D-LED-Cube/master/res/Leds_Glowing.jpeg)

### References

* https://www.instructables.com/id/Raspberry-Pi-4x4x4-LED-Cube/
* https://create.arduino.cc/projecthub/MissionCritical/how-to-make-a-4x4x4-led-cube-with-leftover-leds-a4082f
* https://www.electronicshub.org/8x8x8-led-cube/
