import time

import board
import busio
import digitalio

import adafruit_rfm69

RADIO_FREQ_MHZ = 868.0

CS = digitalio.DigitalInOut(board.CE0)
RESET = digitalio.DigitalInOut(board.D5)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, RADIO_FREQ_MHZ)

counter = 0

while True:
    message = bytes("This is a test message. NO: ", "utf-8")
    message += bytes(str(counter), "utf-8")
    rfm69.send(message)
    print("send message")
    counter += 1
