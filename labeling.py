from turtle import *

location_ids = {
    "A1BE": (-253.0, 376.0),
    "A1FE": (246.0, 377.0),
    "A12D-1": (184.0, 400.0),
    "A2BE": (-253.0, 272.0),
    "A2FE": (245.0, 277.0),
    "A22D-1": (184.0, 348.0),
    "A22D-2": (183.0, 301.0),
    "A3BE": (-252.0, 174.0),
    "A3FE": (252.0, 173.0),
    "A32D-1": (183.0, 250.0),
    "A32D-2": (184.0, 200.0),
    "A4FE": (252.0, 70.0),
    "A4BE": (-250.0, 75.0),
    "A42D-1": (182.0, 148.0),
    "A42D-2": (184.0, 100.0),
    "A5FE": (248.0, -27.0),
    "A5BE": (-251.0, -23.0),
    "A52D-1": (182.0, 46.0),
    "A52D-2": (184.0, -0.0),
    "A6FE": (255.0, -124.0),
    "A6BE": (-254.0, -127.0),
    "A62D-1": (187.0, -56.0),
    "A62D-2": (185.0, -98.0),
    "A7FE": (254.0, -220.0),
    "A7BE": (-257.0, -230.0),
    "A72D-1": (184.0, -151.0),
    "A72D-2": (187.0, -198.0),
    "A8FE": (254.0, -325.0),
    "A8BE": (-255.0, -322.0),
    "A82D-1": (182.0, -254.0),
    "A82D-2": (184.0, -301.0),
    "A9FE": (253.0, -427.0),
    "A9BE": (-253.0, -423.0),
    "D1": (449.0, 329.0),
    "D2": (477.0, 329.0),
    "D3": (509.0, 329.0),
    "D4": (541.0, 329.0),
    "Le1": (465.0, 354.0),
    "Le2": (512.0, 353.0),
    "Le3": (453.0, 307.0),
    "Le4": (476.0, 307.0),
    "Le5": (501.0, 306.0),
    "Le6": (526.0, 305.0),
    "4x41": (392.0, 171.0),
    "4x42": (431.0, 201.0),
    "4x43": (432.0, 143.0),
    "4x44": (391.0, -29.0),
    "4x45": (471.0, -25.0),

}
location_ids2 = {
    "A10FE": (291.0, 316.0),
    "A12BE": (-246.0, 175.0),
    "A12-2D": (184.0, 101.0),
    "A12FE": (247.0, 173.0),
    "A13BE": (-246.0, 82.0),
    "A132D-1": (182.0, 51.0),
    "A132D-2": (184.0, 2.0),
    "A13FE": (244.0, 77.0),
}

def secondary_labels_1_9():
    penup()
    goto(location_ids["A1BE"])
    write("1", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A12D-1"])
    write("2", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A22D-1"])
    write("5", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A1FE"])
    write("3", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A2BE"])
    write("4", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A22D-2"])
    write("6", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A2FE"])
    write("7", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A3BE"])
    write("8", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A32D-1"])
    write("9", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A32D-2"])
    write("10", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A3FE"])
    write("11", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A4BE"])
    write("12", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A42D-1"])
    write("13", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A42D-2"])
    write("14", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A4FE"])
    write("15", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A5BE"])
    write("16", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A52D-1"])
    write("17", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A52D-2"])
    write("18", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A5FE"])
    write("19", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A6BE"])
    write("20", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A62D-1"])
    write("21", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A62D-2"])
    write("22", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A6FE"])
    write("23", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A7BE"])
    write("24", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A7FE"])
    write("27", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A72D-1"])
    write("25", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A72D-2"])
    write("26", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A8BE"])
    write("28", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A82D-1"])
    write("29", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A82D-2"])
    write("30", align="center", font=("Arial", 12, "bold"))
    goto(location_ids["A8FE"])
    write("31", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A9BE"])
    write("32", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["A9FE"])
    write("33", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["D1"])
    write("1", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["D2"])
    write("2", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["D3"])
    write("3", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["D4"])
    write("4", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["Le1"])
    write("5", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["Le2"])
    write("6", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["Le3"])
    write("7", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["Le4"])
    write("8", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["Le5"])
    write("9", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["Le6"])
    write("10", align="center", font=("Arial", 10, "bold"))
    goto(location_ids["4x41"])
    write("1", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["4x42"])
    write("2", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["4x43"])
    write("3", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["4x44"])
    write("4", align="center", font=("Arial", 16, "bold"))
    goto(location_ids["4x45"])
    write("5", align="center", font=("Arial", 16, "bold"))
    hideturtle()

def secondary_labels_10_16():
    penup()
    goto(location_ids2["A10FE"])
    write("34", align="center", font=("Arial", 16, "bold"))
    goto(location_ids2["A12BE"])
    write("35", align="center", font=("Arial", 16, "bold"))
    goto(location_ids2["A12-2D"])
    write("36", align="center", font=("Arial", 16, "bold"))
    goto(location_ids2["A12FE"])
    write("37", align="center", font=("Arial", 16, "bold"))
    goto(location_ids2["A13BE"])
    write("38", align="center", font=("Arial", 16, "bold"))
    goto(location_ids2["A132D-1"])
    write("39", align="center", font=("Arial", 16, "bold"))
    goto(location_ids2["A132D-2"])
    write("40", align="center", font=("Arial", 16, "bold"))
    goto(location_ids2["A13FE"])
    write("41", align="center", font=("Arial", 16, "bold"))

def aisle_labels():
    penup()
    # goto(0.0, 382.0)
    # write("Aisle 1", align="center", font=("Arial", 18, "bold"))
    # goto(0.0, 284.0)
    # write("Aisle 2", align="center", font=("Arial", 18, "bold"))
    # goto(0.0, 183.0)
    # write("Aisle 3", align="center", font=("Arial", 18, "bold"))
    # goto(0.0, 82.0)
    # write("Aisle 4", align="center", font=("Arial", 18, "bold"))
    # goto(0.0, -16.0)
    # write("Aisle 5", align="center", font=("Arial", 18, "bold"))
    # goto(0.0, -117.0)
    # write("Aisle 6", align="center", font=("Arial", 18, "bold"))
    goto(495.0, 373.0)
    write("Dump-ins", align="center", font=("Arial", 18, "bold"))
    goto(575.0, 168.0)
    write("Front Lobby 1", align="center", font=("Arial", 16, "bold"))
    goto(575.0, -26.0)
    write("Front Lobby 2", align="center", font=("Arial", 16, "bold"))
