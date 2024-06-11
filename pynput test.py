import pynput
from pynput.mouse import Button, Controller
import time
import keyboard
import csv

mouse = Controller()
mouseX = 1330

# fp = open("def_list.csv", "r")

with open("def_list.csv", newline='') as csvfile:
    data = list(csv.reader(csvfile))

# print(data[0][3]) # 2D array

for item in data: # item is a row

    mouse.position = (mouseX, -300) # Add task
    # time.sleep(0.5)
    mouse.click(Button.left, 1) # click
    time.sleep(2)

    # select deficiency
    mouse.move(0, 50) # change relative position
    time.sleep(1)
    mouse.click(Button.left, 1) # click

    mouse.move(0, 45)
    time.sleep(1.5)
    mouse.click(Button.left, 1)

    # click on text box
    time.sleep(1)
    mouse.move(0, 30)
    time.sleep(0.5)
    mouse.click(Button.left, 1)

    desc = item[3]
    keyboard.write(desc)

    # selecting location CC (can change later)
    mouse.move(0, 115)
    time.sleep(0.25)
    mouse.click(Button.left, 1)
    mouse.move(0, 120)
    mouse.click(Button.left, 1)

    time.sleep(0.25)
    mouse.move(0, 200)
    mouse.click(Button.left, 1)

    break

