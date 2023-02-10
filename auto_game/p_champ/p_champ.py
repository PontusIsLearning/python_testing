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
image = device.screencap()

with open('screen.png', 'wb') as _f:
    _f.write(image)

img_to_search = cv.imread('screen.png', cv.IMREAD_GRAYSCALE)
play_btn = cv.imread('play.png', cv.IMREAD_GRAYSCALE)
race_btn = cv.imread('race.png', cv.IMREAD_GRAYSCALE)

play_loc = cv.matchTemplate(img_to_search, play_btn, cv.TM_CCOEFF_NORMED)
race_loc = cv.matchTemplate(img_to_search, race_btn, cv.TM_CCOEFF_NORMED)

cv.imshow('Result', play_loc)
cv.waitKey()