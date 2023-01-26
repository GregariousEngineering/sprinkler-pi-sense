Sprinkler Pi Sense
========================================
Demo Raspberry Pi Qwiic "Smart" Sprinkler
----------------

[![SparkFun Qwiic Kit for Raspberry Pi](https://cdn.sparkfun.com//assets/parts/1/5/7/6/5/16841-SparkFun_Qwiic_Starter_Kit_for_Raspberry_Pi-02.jpg)](https://www.sparkfun.com/products/16841)

*This is demo code to go with* [*"Smart" Sprinkler*](https://www.gregariousengineering.com/2022/12/smart-sprinkler.html)

Program Function
---------------
Read data from DarkSky API and Rain Sensor (GPIO2), decide if sprinklers should be disabled, 
actuate a Qwiic relay to simulate Rain Sensor disabling sprinklers, and display status on Qwiic OLED

Acknowledgements
----------------
* **Based on these SparkFun demos
    * ** [Sparkfun Qwiic Relay Demo](https://github.com/sparkfun/Qwiic_Relay_Py)
    * ** [Sparkfun Qwiic Qwiic Kit for Pi Demo](https://github.com/sparkfun/Qwiic-Kit-for-Pi)

Repository Contents
-------------------
* **/sprinkler_pi_sense_demo.py** - Example code 

Requirements
--------------
* **Raspberry Pi** - Any will do
* **Qwiic Connection** - 
   * ** e.g. [SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://www.sparkfun.com/products/15945)
* **Qwiic Relay** - To simulate Rain Sensor
   * ** e.g. [SparkFun Qwiic Single Relay ](https://www.sparkfun.com/products/15093)
* **Qwiic OLED** - For quick status
   * ** e.g. [SparkFun Micro OLED Breakout](https://www.sparkfun.com/products/14532)
* **Python Modules (i.e. Libraries)** - Python library for the Qwiic Kit for Raspberry Pi.
   * ** [Qwiic Python Library](https://github.com/sparkfun/qwiic_py)
   * ** Qwiic Relay Python Library
* **DarkSky Developer Account** - Account is required to pull current weather data (no longer accepting signups since bought by Apple; moving to Apple Developer in March)
   * ** [Dark Sky API](https://darksky.net/dev)

Documentation
--------------
* **Python Modules (i.e. Libraries)** - Python library for the Qwiic Kit for Raspberry Pi.
   * **[Qwiic_I2C_Py](https://github.com/sparkfun/Qwiic_I2C_Py)**
   * **[Qwiic_Micro_OLED_Py](https://github.com/sparkfun/Qwiic_Micro_OLED_Py)**
   * **[Qwiic_Py](https://github.com/sparkfun/Qwiic_Py)**
* **[Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-kit-for-raspberry-pi-hookup-guide)** - Basic hookup guide for the Qwiic Kit.
  

License Information
-------------------

This product is _**open source**_! 

Please review the LICENSE.md file for license information. 

Distributed as-is, with flaws; no warranty or guarantee.

- GregariousEngineer

