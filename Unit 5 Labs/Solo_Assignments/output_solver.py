from math import *
from tkinter import Tk
while True:
    r = Tk()
    r.withdraw()
    risk = 0
    sex = input("sex")
    if sex == "stop":
        break
    age = int(input("age"))
    cho = int(input("cho"))
    smo = input("smo")
    hdl = int(input("hdl"))
    sbp = int(input("sbp"))
    med = input("med")

    if sex == "F":
        if age <= 34:
            risk += -7
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 4
            elif cho <= 239:
                risk += 8
            elif cho <= 279:
                risk += 11
            elif cho >= 280:
                risk += 13
            if smo == "Y":
                risk += 9
        elif age <= 39:
            risk += -3
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 4
            elif cho <= 239:
                risk += 8
            elif cho <= 279:
                risk += 11
            elif cho >= 280:
                risk += 13
            if smo == "Y":
                risk += 9
        elif age <= 44:
            risk += 0
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 3
            elif cho <= 239:
                risk += 6
            elif cho <= 279:
                risk += 8
            elif cho >= 280:
                risk += 10
            if smo == "Y":
                risk += 7
        elif age <= 49:
            risk += 3
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 3
            elif cho <= 239:
                risk += 6
            elif cho <= 279:
                risk += 8
            elif cho >= 280:
                risk += 10
            if smo == "Y":
                risk += 7
        elif age <= 54:
            risk += 6
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 2
            elif cho <= 239:
                risk += 4
            elif cho <= 279:
                risk += 5
            elif cho >= 280:
                risk += 7
            if smo == "Y":
                risk += 4
        elif age <= 59:
            risk += 8
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 2
            elif cho <= 239:
                risk += 4
            elif cho <= 279:
                risk += 5
            elif cho >= 280:
                risk += 7
            if smo == "Y":
                risk += 4
        elif age <= 64:
            risk += 10
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 1
            elif cho <= 239:
                risk += 2
            elif cho <= 279:
                risk += 3
            elif cho >= 280:
                risk += 4
            if smo == "Y":
                risk += 2
        elif age <= 69:
            risk += 12
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 1
            elif cho <= 239:
                risk += 2
            elif cho <= 279:
                risk += 3
            elif cho >= 280:
                risk += 4
            if smo == "Y":
                risk += 2
        elif age <= 74:
            risk += 14
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 1
            elif cho <= 239:
                risk += 1
            elif cho <= 279:
                risk += 2
            elif cho >= 280:
                risk += 2
            if smo == "Y":
                risk += 1
        elif age <= 79:
            risk += 16
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 1
            elif cho <= 239:
                risk += 1
            elif cho <= 279:
                risk += 2
            elif cho >= 280:
                risk += 2
            if smo == "Y":
                risk += 1
        if hdl >= 60:
            risk += -1
        elif hdl < 60:
            risk += 0
        elif hdl < 50:
            risk += 1
        elif hdl < 40:
            risk += 2
        if med == "T":
            if sbp < 120:
                risk += 0
            elif sbp < 130:
                risk += 3
            elif sbp < 140:
                risk += 4
            elif sbp < 160:
                risk += 5
            elif sbp >= 160:
                risk += 6
        else:
            if sbp < 120:
                risk += 0
            elif sbp < 130:
                risk += 1
            elif sbp < 140:
                risk += 2
            elif sbp < 160:
                risk += 3
            elif sbp >= 160:
                risk += 4
        if risk < 9:
            r.clipboard_append("<1")
        elif risk == 9:
            r.clipboard_append("1")
        elif risk == 10:
            r.clipboard_append("1")
        elif risk == 11:
            r.clipboard_append ("1")
        elif risk == 12:
            r.clipboard_append("1")
        elif risk == 13:
            r.clipboard_append("2")
        elif risk == 14:
            r.clipboard_append("2")
        elif risk == 15:
            r.clipboard_append ("3")
        elif risk == 16:
            r.clipboard_append("4")
        elif risk == 17:
            r.clipboard_append("5")
        elif risk == 18:
            r.clipboard_append("6")
        elif risk == 19:
            r.clipboard_append("8")
        elif risk == 20:
            r.clipboard_append("11")
        elif risk == 21:
            r.clipboard_append("14")
        elif risk == 22:
            r.clipboard_append("17")
        elif risk == 23:
            r.clipboard_append("22")
        elif risk == 24:
            r.clipboard_append("27")
        elif risk >= 25:
            r.clipboard_append(">=30")
    if sex == "M":
        if age <= 34:
            risk += -9
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 4
            elif cho <= 239:
                risk += 7
            elif cho <= 279:
                risk += 9
            elif cho >= 280:
                risk += 11
            if smo == "Y":
                risk += 8
        elif age <= 39:
            risk += -4
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 4
            elif cho <= 239:
                risk += 7
            elif cho <= 279:
                risk += 9
            elif cho >= 280:
                risk += 11
            if smo == "Y":
                risk += 8
        elif age <= 44:
            risk += 0
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 3
            elif cho <= 239:
                risk += 5
            elif cho <= 279:
                risk += 6
            elif cho >= 280:
                risk += 8
            if smo == "Y":
                risk += 5
        elif age <= 49:
            risk += 3
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 3
            elif cho <= 239:
                risk += 5
            elif cho <= 279:
                risk += 6
            elif cho >= 280:
                risk += 8
            if smo == "Y":
                risk += 5
        elif age <= 54:
            risk += 6
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 2
            elif cho <= 239:
                risk += 3
            elif cho <= 279:
                risk += 4
            elif cho >= 280:
                risk += 5
            if smo == "Y":
                risk += 3
        elif age <= 59:
            risk += 8
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 2
            elif cho <= 239:
                risk += 3
            elif cho <= 279:
                risk += 4
            elif cho >= 280:
                risk += 5
            if smo == "Y":
                risk += 3
        elif age <= 64:
            risk += 10
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 1
            elif cho <= 239:
                risk += 1
            elif cho <= 279:
                risk += 2
            elif cho >= 280:
                risk += 3
            if smo == "Y":
                risk += 1
        elif age <= 69:
            risk += 11
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 1
            elif cho <= 239:
                risk += 1
            elif cho <= 279:
                risk += 2
            elif cho >= 280:
                risk += 3
            if smo == "Y":
                risk += 1
        elif age <= 74:
            risk += 12
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 0
            elif cho <= 239:
                risk += 0
            elif cho <= 279:
                risk += 1
            elif cho >= 280:
                risk += 1
            if smo == "Y":
                risk += 1
        elif age <= 79:
            risk += 13
            if cho < 160:
                risk += 0
            elif cho <= 199:
                risk += 0
            elif cho <= 239:
                risk += 0
            elif cho <= 279:
                risk += 1
            elif cho >= 280:
                risk += 1
            if smo == "Y":
                risk += 1
        if hdl >= 60:
            risk += -1
        elif hdl < 60:
            risk += 0
        elif hdl < 50:
            risk += 1
        elif hdl < 40:
            risk += 2
        if med == "T":
            if sbp < 120:
                risk += 0
            elif sbp < 130:
                risk += 1
            elif sbp < 140:
                risk += 2
            elif sbp < 160:
                risk += 2
            elif sbp >= 160:
                risk += 3
        else:
            if sbp < 120:
                risk += 0
            elif sbp < 130:
                risk += 0
            elif sbp < 140:
                risk += 1
            elif sbp < 160:
                risk += 1
            elif sbp >= 160:
                risk += 2
        if risk < 0:
            r.clipboard_append("<1")
        elif risk == 0:
            r.clipboard_append("1")
        elif risk == 1:
            r.clipboard_append("1")
        elif risk == 2:
            r.clipboard_append ("1")
        elif risk == 3:
            r.clipboard_append("1")
        elif risk == 4:
            r.clipboard_append("1")
        elif risk == 5:
            r.clipboard_append("2")
        elif risk == 6:
            r.clipboard_append ("2")
        elif risk == 7:
            r.clipboard_append("3")
        elif risk == 8:
            r.clipboard_append("4")
        elif risk == 9:
            r.clipboard_append("5")
        elif risk == 10:
            r.clipboard_append("6")
        elif risk == 11:
            r.clipboard_append("8")
        elif risk == 12:
            r.clipboard_append("10")
        elif risk == 13:
            r.clipboard_append("12")
        elif risk == 14:
            r.clipboard_append("16")
        elif risk == 15:
            r.clipboard_append("20")
        elif risk == 16:
            r.clipboard_append("25")
        elif risk >= 17:
            r.clipboard_append(">=30")