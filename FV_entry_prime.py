# Modified Python script for automation of adding deficiencies to Field View V2.0

# V1.0 read Excel data from a .csv file and required more logic in order to convert a task to its subtrade,
# and for correctly identifying and selecting the location of the deficiency within the building based on its description.

# This version reads from a .txt file (which I had already converted from a pdf using different Python code),
# and assigns all deficiencies to Chandos, due to the absence of the correct subtrade in the Field View list.

# This is not a plug and play solution, it was designed to work with my specific computer setup. However it can be adapted 
# quite easily to be much more broadly applicable.

# Talha Malik, June 12, 2024
# Last Updated: July 15, 2024

import pynput
from pynput.mouse import Button, Controller
import time
import keyboard
import csv

mouse = Controller()

# Helper function to convert subtrade to expected 'Package' by Field View
def convert_trade(name):
    match name:
        case "Benmar":
            return "drywall"
        case "CCL":
            return "chandos"
        case "JDA":
            return "miscellaneous"
        case "Lab Flooring":
            return "flooring"
        case "Ladson":
            return "millwork"
        case "PPG":
            return "electrical"
        case "Swift":
            return "mechanical"
        case "NexLevel":
            return "fireproofing"
        case "Flynn":
            return "roofing siding"
        case "Bramalea":
            return "structural steel"
        case "Historic":
            return "restoration"
        case "Tuygun":
            return "painting"
        case "Upper Canada":
            return "doors"
        case "Westmount":
            return "glazing"
        case "Troy":
            return "fire proection"
        case "Outspan":
            return "formwork"
        case "Pink":
            return "precast"
        case "Thyssenkrupp":
            return "elevator"
        case "Novum":
            return "structural glass"
        case "Verdi":
            return "hardscape"
        case "Custom Ice":
            return "ice rink"
        case "Forest":
            return "paving"
        case default:
            return "chando"
        
# Helper function to check if a trade is in the database
def trade_exists(name):
    if convert_trade(name) == "chando":
        return False
    else:
        return True
        
# Helper function to automatically select correct floor of CC (only my format)
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

def run(filename): # currently set to read CSV, can adjust to detect file type

    mouseX = 1330

    with open(filename, newline='', encoding='utf-8') as csvfile:
        data = list(csv.reader(csvfile))

    location = data[0][0]

    cc = 100
    lib = 140
    br = 75
    sq = 165

    match location:
        case "CC":
            location = cc
        case "LIB":
            location = lib
        case "BR":
            location = br
        case "SQ":
            location = sq

    counter = 0

    # Main loop to iterate through all entries in file
    for i in range(1, len(data)): # item is a row
        counter += 1

        mouse.position = (mouseX, -300) # Add task
        time.sleep(0.5)
        mouse.click(Button.left, 1) # click
        time.sleep(0.5)

        # select deficiency
        mouse.move(0, 50) # change relative position
        time.sleep(0.25)
        mouse.click(Button.left, 1) # click
        time.sleep(0.25)


        mouse.move(0, 70)
        time.sleep(0.5)
        mouse.click(Button.left, 1)

        # click on text box
        time.sleep(0.5)
        mouse.move(0, 30)
        time.sleep(0.25)
        mouse.click(Button.left, 1)

        # Checking if subtrade is in FV or not, then writes description of task
        if trade_exists(data[i][0]):
            keyboard.write(data[i][1])
        else:
            keyboard.write(f"{data[i][1]} ({data[i][0]})")

        # selecting location CC (can change later)
        mouse.move(0, 115)

        time.sleep(0.25)
        mouse.click(Button.left, 1)

        # location variable can be interchanged
        mouse.move(0, location)
        mouse.click(Button.left, 1)
        mouse.move(0, (-1 * location))

        time.sleep(0.25)
        mouse.move(0, 120)


        time.sleep(0.25)
        mouse.move(0, 150)
        mouse.click(Button.left, 1)

        
        # Positioning over search bar (trade type) and type value
        time.sleep(0.25)
        mouse.move(0, 40)
        mouse.click(Button.left, 1)

        # Type package name into search bar
        keyboard.write(convert_trade(data[i][0]))

        # Select Package
        time.sleep(0.25)
        mouse.move(0, 50)
        time.sleep(0.25)
        mouse.click(Button.left, 1)


        # Scroll down
        time.sleep(0.25)
        for k in range(10):
            keyboard.send("down")

        # Click on Priority
        time.sleep(0.25)
        mouse.move(0, -20)
        time.sleep(0.25)
        mouse.click(Button.left, 1)

        # Select medium priority (can be changed)
        time.sleep(0.25)
        mouse.move(0, 120)
        time.sleep(0.25)
        mouse.click(Button.left, 1)


        time.sleep(0.25)
        mouse.move(0, 80)

        mouse.click(Button.left, 1)

        # This delay may need to be lengthened on systems with a slow internet connection. If the page does not reload within 2.5s the program behaves unexpectedly.
        time.sleep(3)


# declaring files/locations
locations = ["br", "lib", "cc"]
filenames = ["RAW_BR_2.csv", "RAW_LIB_2.csv", "RAW_CC_2.csv"]

# running for each file
# for i in range(2):
#     run(filenames[i])

run("TPP_51.csv")