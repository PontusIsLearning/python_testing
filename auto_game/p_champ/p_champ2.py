from ppadb.client import Client
from time import sleep
import cv2 as cv
import numpy as np


adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('No device connected')
    quit()

device = devices[0]

for i in range(10):
    device.shell('input touchscreen tap 350 2100')
    sleep(5)
    device.shell('input touchscreen tap 400 2350')
    # Wait for race
    sleep(40)
    device.shell('input touchscreen tap 400 2350')
    sleep(5)
    device.shell('input touchscreen tap 400 2350')
    if i % 2 == 0:
        # Wait for add
        sleep(40)
        device.shell('input keyevent 4')   
    sleep(5)