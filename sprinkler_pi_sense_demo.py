#!/usr/bin/env python3

# -----------------------------------------------------------------------------
#            Example Code for Raspberry Pi Sprinkler "Rain Sensor"
# -----------------------------------------------------------------------------
# Read data from DarkSky API and Rain Sensor (GPIO2), decide if sprinklers should
# be disabled, actuate a Qwiic relay to simulate rain sensor to control spinklers
# and update Qwiic Micro OLED
# By: GregariousEngineer @ GregariousEngineering
# Created: 12/12/2021
# Last Update: 12/25/2022
#
# Distributed for fun, as-is, with flaws; no warranty or guarantee
# -----------------------------------------------------------------------------
from __future__ import print_function, division
import requests
import qwiic #Must download Qwiic Python Library - https://github.com/sparkfun/qwiic_py
import qwiic_relay
import time
import sys
from gpiozero import Button

is_sprinkler_disabled = False

#DarkSky API Setup - you will need an account and lat/long
darkSkyApiToken="YOUR DARKSKY TOKEN HERE"
location="42.1456,-100.1555" # Your garden coordinates here
weatherURL="https://api.darksky.net/forecast/"+darkSkyApiToken+"/"+location

rain_sensor_relay = qwiic_relay.QwiicRelay()
if rain_sensor_relay.begin() == False:
    print("The Qwiic Relay isn't connected to the system. Please check your connection", file=sys.stderr)
    is_rain_sensor_relay = False

#Qwiic OLED
oled = qwiic.QwiicMicroOled()
if oled.begin() == False:
    print("The Qwiic OLED isn't connected to the system. Please check your connection", file=sys.stderr)
    is_oled = False
else:
    oled.clear(oled.ALL)
    oled.display()
    oled.set_font_type(1) 

#Rain Bird Rain Sensor (or similar) wired to GPIO 2 to allow physical sensor passthrough
rain_sensor = Button(2) 

#Loop runs until we force an exit or something breaks
while True:
    try:
        is_sprinkler_disabled = False

        # Pull data from DarkSky
        weather = requests.get(weatherURL).json()
        print("New weather from "+time.strftime("%a %b %d %Y %H:%M:%S", time.localtime()))

        # If low < 45F
        if weather['daily']['data']['0']['apparentTemperatureLow'] < 45: 
            print("Disabled for low temp below 45F")
            is_for_low_temp = True
            is_sprinkler_disabled = True

        # If high < 75F
        if weather['daily']['data']['0']['apparentTemperatureHigh'] < 75: 
            print("Disabled for high temp above 75F") 
            is_for_high_temp = True
            is_sprinkler_disabled = True

        # If precipitation accumulation > 0.25
        if weather['daily']['data']['0']['precipAccumulation'] > 0.25: 
            print("Disabled for precip accumulation more than 1/4in") 
            is_for_acc_precip = True
            is_sprinkler_disabled = True

        # If moderate intensity precip is likely
        if weather['daily']['data']['0']['precipProbability'] > 0.5 and weather['daily']['data']['0']['precipIntensityMax'] > 0.025: 
            print("Disabled for expected precip") 
            is_for_exp_precip = True
            is_sprinkler_disabled = True

        # Check the rain sensor and skip spinkler if it's rained
        if rain_sensor.is_pressed: 
            print("Disabled for rain rensor active") 
            is_for_sensor = True
            is_sprinkler_disabled = True

        # Set the relay
        if is_rain_sensor_relay and is_sprinkler_disabled: 
            # Set the relay
            rain_sensor_relay.set_relay_off(1)

        print("Sprinklers Disabled? "+is_sprinkler_disabled)
        print(" ") #blank line for easier readability

        if is_oled:
            oled.clear(oled.PAGE)

            oled.set_cursor(0,0)
            oled.print(int(weather['daily']['data']['0']['apparentTemperatureLow']))
            oled.print("-")
            oled.print(int(weather['daily']['data']['0']['apparentTemperatureHigh']))
            oled.print("F")
            if is_for_low_temp or is_for_high_temp:
                oled.print("*")
            
            oled.set_cursor(0,16)
            oled.print(int(weather['daily']['data']['0']['precipProbability'])*10)
            oled.print("%")
            oled.print("{0:.2f}".format(weather['daily']['data']['0']['precipIntensityMax']))
            oled.print("in/hr")
            if is_for_acc_precip or is_for_exp_precip:
                oled.print("*")
            
            oled.set_cursor(0,32)
            if is_sprinkler_disabled:
                oled.print("Disabled!")
                if is_for_sensor:
                    oled.print("*")
            
            oled.display()
        
        time.sleep(120)
        
        
    #if we break things or exit then exit cleanly
    except (EOFError, SystemExit, KeyboardInterrupt):
        mqttc.disconnect()
        sys.exit()
