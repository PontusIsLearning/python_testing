from ppadb.client import Client
from time import sleep
import cv2 as cv
import numpy as np
from PIL import Image

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('No device connected')
    quit()

device = devices[0]

def countdown(t, p=10):
    '''
    Set timer, t = seconds to countdown, p = interval to print default is every 10s.
    '''
    for i in range(t):
        sleep(1)
        if i % p == 0:
            print(f"{t - i}")

def check_for_exit():

    image = device.screencap()

    with open("screen.png", "wb") as f:
        f.write(image)

    image = Image.open("screen.png")
    image = np.array(image, dtype=np.uint8)

    # print(len(image[:,1]))
    # print(image[:,400])

    # röd knapp @ x 200, y 1450

    pxl = [list(i[:3]) for i in image[1450]]
    return pxl[250:350]

n = 1

while True:
    print(f"Starting race nr{n}")
    sleep(2)
    # Start race
    device.shell('input touchscreen tap 450 2100')
    sleep(4)
    device.shell('input touchscreen tap 450 2350')
    # Wait for race
    print("waiting for race to finnish")
    countdown(45)
    device.shell('input touchscreen tap 450 2350')
    sleep(4)
    device.shell('input touchscreen tap 450 2350')
    print("waiting 10s then pressing back")
    countdown(10, 1)
    device.shell('input keyevent 4')
    sleep(5)
    # check for quit screen
    pxl = check_for_exit()
    for j in pxl:
        if j[0] > 200:
            print("found quit screen")
            # voulez vous quitter? Non
            device.shell('input touchscreen tap 300 1450')
            sleep(2)
            break
        else:
            continue
    device.shell('input keyevent 4')
    sleep(5)
    # check for quit screen
    pxl = check_for_exit()
    for j in pxl:
        if j[0] > 200:
            print("found quit screen")
            # voulez vous quitter? Non
            device.shell('input touchscreen tap 300 1450')
            sleep(2)
            break
        else:
            continue
    n += 1