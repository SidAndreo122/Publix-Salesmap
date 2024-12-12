from turtle import *
import time
from aisles import Aisle
from tkinter import *
from pandas import *
from labeling import location_ids, secondary_labels_1_9, aisle_labels

ON = True
# ---------------------------- PANDA DATA SETUP ------------------------------ #
data = read_csv("exceldata/testing_publix_salesv2.csv")

# ---------------------------- MAP SETUP ------------------------------------- #
# TODO-1: Import Turtle, and create aisles class to create aisles on the screen
screen = Screen()
screen.setup(width=1320, height=1020)
screen.title("Aisles 1-9 Publix Salesmap") # creates name on the top of the window
screen.tracer(0)

aisle = Aisle(0, 382.5)
Aisle(x=0, y=282.5)
Aisle(x=0, y=182.5)
Aisle(x=0, y=82.5)
Aisle(x=0, y=-17.5)
Aisle(x=0, y=-117.5)
Aisle(x=0, y=-217.5)
Aisle(x=0, y=-317.5)
Aisle(x=0, y=-417.5)
# TODO-2: Use a grid or eyeball it to perfect positioning of pixels on page. Make the page look good by thickening lines
# TODO-3: Create Dump-Ins, lobby 1 and 2 on the screen
secondary_labels_1_9()
aisle_labels()
aisle.create_dump_ins()
aisle.create_lobby_display_2()
aisle.create_lobby_display_1()
# print(data['Location ID']["Nabisco - Aisle 3 Front Endcap"])
# if data.iloc[6, 3] == "A3FE":
#     goto(location_ids["A3FE"])
#     write(f"{data[data.Item == "NAB VRTY MINI CKIE 12PK1"]}")
def get_mouse_click_coor(x, y):
    print(f"{x}, {y}")

onscreenclick(get_mouse_click_coor) # will listen to keyboard press for a click from mouse and call the function
while ON:
    time.sleep(0.1)
    screen.update()

# ts = turtle.getscreen()
# ts.getcanvas().postscript(file="test.ps")
screen.exitonclick()


