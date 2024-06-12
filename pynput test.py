import pynput
from pynput.mouse import Button, Controller
import time
import keyboard
import csv

# Converts subtrade to expected 'Package' by FieldView
def convert_trade(name):
    match name:
        case "Benmar":
            return "drywall"
        # case "Branch A/V":
        #     return "" ### not in FV
        case "CCL":
            return "chandos"
        # case "EN3":
        #     return  ### not in FV
        case "JDA":
            return "miscellaneous"
        case "Lab Flooring":
            return "flooring"
        case "Ladson":
            return "millwork"
        case "PPG":
            return "electrical"
        # case "SDR Seating":
        #     return "" ### not in FV
        case "Swift":
            return "mechanical"
        case "Tuygun":
            return "painting"
        case "Upper Canada":
            return "doors"
        case "Westmount":
            return "glazing"
        case default:
            return "nothing"
        
def location(item):
    if item[2].startswith('B'):
        mouse.click(Button.left, 1)
    elif item[2].startswith('1'):
        mouse.move(0, 35)
        mouse.click(Button.left)
        mouse.move(0, -35)
    elif item[2].startswith('2'):
        mouse.move(0, 70)
        mouse.click(Button.left, 1)
        mouse.move(0, -70)
    else:
        mouse.move(0, 105)
        mouse.click(Button.left, 1)
        mouse.move(0, -105)


mouse = Controller()
mouseX = 1330


with open("def_list_2.csv", newline='') as csvfile:
    data = list(csv.reader(csvfile))

# print(data[0][3]) # 2D array
counter = 0

for i in range(215, len(data)): # item is a row
    counter += 1

    mouse.position = (mouseX, -300) # Add task
    time.sleep(1)
    mouse.click(Button.left, 1) # click
    time.sleep(1)

    # select deficiency
    mouse.move(0, 50) # change relative position
    time.sleep(1)
    mouse.click(Button.left, 1) # click
    time.sleep(1)


    mouse.move(0, 45)
    time.sleep(1)
    mouse.click(Button.left, 1)

    # click on text box
    time.sleep(1)
    mouse.move(0, 30)
    time.sleep(1)
    mouse.click(Button.left, 1)

    desc = data[i][3]
    keyboard.write(desc + ": " + data[i][2])

    # selecting location CC (can change later)
    mouse.move(0, 115)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    mouse.move(155, 120)
    mouse.click(Button.left, 1)

    # Selecting architectural
    mouse.move(0, 40)
    mouse.click(Button.left, 1)

    location(data[i]) # selects location

    mouse.move(-155, -40)

    time.sleep(1)
    mouse.move(0, 200)
    mouse.click(Button.left, 1)

    # Positioning over search bar (trade type) and type value
    time.sleep(1)
    mouse.move(0, 30)
    mouse.click(Button.left, 1)
    keyboard.write(convert_trade(data[i][4]))


    # Select Package
    time.sleep(1)
    mouse.move(0, 40)
    time.sleep(1)
    mouse.click(Button.left, 1)

    # Scroll down
    time.sleep(1)
    for k in range(10):
        keyboard.send("down")

    # Click on Priority
    time.sleep(0.75)
    mouse.move(0, -20)
    time.sleep(0.75)
    mouse.click(Button.left, 1)

    # Select medium priority (can be changed)
    time.sleep(0.75)
    mouse.move(0, 100)
    time.sleep(1)
    mouse.click(Button.left, 1)

    time.sleep(0.75)
    mouse.move(0, 80)
    mouse.click(Button.left, 1)

    time.sleep(5 + (counter / 100))
