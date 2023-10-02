# !/usr/bin/python
# import RPi.GPIO as GPIO
import time
import sys
# import paho.mqtt.publish as publish

from gpiozero import Button

FLOW_SENSOR_GPIO = 23
BUTTON_COULD_WATER = 22
# MQTT_SERVER = "192.168.1.220"

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

botton_despacho = Button(BUTTON_COULD_WATER)


def countPulse(channel):
    global count
    if botton_despacho.is_pressed:  # start_counter == 1:
        count = count + 1


flujometro = Button(FLOW_SENSOR_GPIO)
flujometro.when_pressed = countPulse

global count
count = 0

# GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)


try:
    # start_counter = 1
    # segundos = 0
    # if botton_despacho.
    # while botton_despacho.is_pressed:
    #     time.sleep(1)
    #     segundos += 1
    # start_counter = 0
    sec = 0
    botton_despacho.wait_for_press()
    botton_despacho.when_released = lambda: sec = botton_despacho.active_time
    # sec = botton_despacho.active_time
    print(sec)
    time.sleep(1)
    # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
    flow = (count / 137) / sec
    print(count)
    print("The flow is: %.3f Liter/min" % (flow))
    # publish.single("/Garden.Pi/WaterFlow", flow, hostname=MQTT_SERVER)
    count = 0
    # time.sleep(5)
except KeyboardInterrupt:
    print('\nkeyboard interrupt!')
    sys.exit()
