import random
import pyautogui
import time
import keyword
from enum import Enum
#import subprocess
from PIL import ImageGrab
import cv2
import easyocr
import matplotlib.pyplot as plt


class Energy:
    # create box from screen and grab a screenshot
    pic = ImageGrab.grab(bbox=(850, 135, 950, 150))
    #pic.show()
    pic.save("C:/Users/vlade/Downloads/scrcpy-win64-v2.0/scrcpy-win64-v2.0/screen.png")

    # read image
    image_path = 'C:/Users/vlade/Downloads/scrcpy-win64-v2.0/scrcpy-win64-v2.0/screen.png'
    img = cv2.imread(image_path)

    # inctance text detector
    reader = easyocr.Reader(['en'], gpu=False)

    # detect text on image
    text_ = reader.readtext(img)

    col = [row[1] for row in text_]
    energy_bar = (col[0].split('/'))
    energy = int(energy_bar[0])
    print(energy)


class Season(Enum):
    SEASON1 = 1
    SEASON2 = 2
    SEASON3 = 3
    SEASON4 = 4
    SEASON5 = 5


class Province(Enum):
    PROVINCE1 = 1
    PROVINCE2 = 2
    PROVINCE3 = 3
    PROVINCE4 = 4
    PROVINCE5 = 5
    PROVINCE6 = 6
    PROVINCE7 = 7
    PROVINCE8 = 8
    PROVINCE9 = 9
    PROVINCE10 = 10
    PROVINCE11 = 11
    PROVINCE12 = 12
    PROVINCE13 = 13
    PROVINCE14 = 14
    PROVINCE15 = 15
    PROVINCE16 = 16
    PROVINCE17 = 17
    PROVINCE18 = 18
    PROVINCE19 = 19
    PROVINCE20 = 20
    PROVINCE21 = 21
    PROVINCE22 = 22
    PROVINCE23 = 23
    PROVINCE24 = 24
    PROVINCE25 = 25
    PROVINCE26 = 26
    PROVINCE27 = 27
    PROVINCE28 = 28
    PROVINCE29 = 29
    PROVINCE30 = 30
    PROVINCE31 = 31
    PROVINCE32 = 32
    PROVINCE33 = 33
    PROVINCE34 = 34
    PROVINCE35 = 35


class Stage(Enum):
    STAGE1 = 1
    STAGE2 = 2
    STAGE3 = 3
    STAGE4 = 4
    STAGE5 = 5
    STAGE6 = 6
    STAGE7 = 7
    STAGE8 = 8
    STAGE9 = 9
    STAGE10 = 10

#seasons = [Season.SEASON1, Season.SEASON2, Season.SEASON3, Season.SEASON4, Season.SEASON5]
#seasons[0] = (940, 240)
#print(seasons[0])


#pyautogui.moveTo(seasons[0])
#seasons[0] = (1000,300)
#pyautogui.moveTo(seasons[0])
season_choice = Season.SEASON1
random_x = random.uniform(0.8, 1.5)

seasons = {Season.SEASON1.value: (940, 240), Season.SEASON2.value: (990, 240), Season.SEASON3.value: (1040, 240),
           Season.SEASON4.value: (1090, 240), Season.SEASON5.value: (1140, 240)}

mission_menu = (920, 920)
go_button_menu = (1100, 270)
back_button_menu = (780, 920)


def go_to_mission():
    pyautogui.moveTo(mission_menu, None, random_x, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(1)
    go_button()


def go_button():
    pyautogui.moveTo(go_button_menu, None, random_x, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(1)
    button_back()


def button_back():
    pyautogui.moveTo(back_button_menu, None, random_x, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(1)


def empty_click_before_back():
    return pyautogui.moveTo(780, 920, random_x, pyautogui.easeOutQuad)


def button_x():
    return pyautogui.moveTo(1140, 140, random_x, pyautogui.easeOutQuad)


def button_next():
    return pyautogui.moveTo(960, 920, random_x, pyautogui.easeOutQuad)


def button_next_stop():
    return pyautogui.moveTo(1040, 850, random_x, pyautogui.easeOutQuad)


def button_fight():
    return pyautogui.moveTo(1050, 950, random_x, pyautogui.easeOutQuad)


def button_auto():
    return pyautogui.moveTo(1090, 135, random_x, pyautogui.easeOutQuad)


def button_replay():
    return pyautogui.moveTo(830, 850, random_x, pyautogui.easeOutQuad)

def update_energy():
    ## update energy
    # create box from screen and grab a screenshot
    pic = ImageGrab.grab(bbox=(780, 130, 860, 160))
    # pic.show()
    pic.save("C:/Users/vlade/Downloads/scrcpy-win64-v2.0/scrcpy-win64-v2.0/screen.png")

    # read image
    image_path = 'C:/Users/vlade/Downloads/scrcpy-win64-v2.0/scrcpy-win64-v2.0/screen.png'
    img = cv2.imread(image_path)

    # inctance text detector
    reader = easyocr.Reader(['en'], gpu=False)

    # detect text on image
    text_update = reader.readtext(img)

    col = [row[1] for row in text_update]
    energy_bar_update = (col[0].split('/'))
    Energy.energy = int(energy_bar_update[0])
    print(Energy.energy)
    ## update energy block


def stop():
    button_x()
    pyautogui.click()
    time.sleep(1)
    button_next_stop()
    pyautogui.click()
    time.sleep(1)
    empty_click_before_back()
    pyautogui.click()
    time.sleep(1)
    button_back()
    pyautogui.click()
    time.sleep(1)
    #subprocess.call([r'C:/Users/vlade/Downloads/scrcpy-win64-v2.0/scrcpy-win64-v2.0/exit.bat'])
    exit()


def replay():
    #Energy.energy = Energy.energy - 3
    print (Energy.energy)
    button_replay()
    pyautogui.click()
    time.sleep(1)
    update_energy()
    if Energy.energy < 3:
        stop()
    button_fight()
    pyautogui.click()
    while not (pyautogui.pixel(1090, 135)[0] == 251 and pyautogui.pixel(1090, 135)[1] == 251 and pyautogui.pixel(1090,
                                135)[2] == 251):
        pass
    button_auto()
    pyautogui.click()
    time.sleep(1)
    while not (pyautogui.pixel(830, 850)[0] == 46 and pyautogui.pixel(830, 850)[1] == 127 and pyautogui.pixel(830, 850)[
        2] == 177):
        pass

    replay()




go_to_mission()

# Go to Season1 (8-7) only by default
if season_choice == Season.SEASON1:
    print(seasons[Season.SEASON1.value])
    pyautogui.moveTo(seasons[Season.SEASON1.value], None, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(None, 500, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.dragTo(1100, 500, 1, button='left')
    pyautogui.moveTo(940, None, random_x, pyautogui.easeOutQuad)
    pyautogui.dragTo(1100, 500, 1, button='left')
    pyautogui.moveTo(940, None, random_x, pyautogui.easeOutQuad)
    pyautogui.dragTo(1100, 500, 1, button='left')
    time.sleep(1)
    pyautogui.moveTo(800, 600, random_x, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(890, 450, random_x, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(1)
    button_next()
    pyautogui.click()
    time.sleep(1)
    update_energy()
    if Energy.energy < 3:
        stop()
    button_fight()
    #pyautogui.moveTo(1050, 950, random_x, pyautogui.easeOutQuad)
    pyautogui.click()
    while not (pyautogui.pixel(1090, 135)[0] == 251 and pyautogui.pixel(1090, 135)[1] == 251 and pyautogui.pixel(1090,
                                135)[2] == 251):
        pass
    button_auto()
    #pyautogui.moveTo(1090, 140, random_x, pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(1)
    while not (pyautogui.pixel(830, 850)[0] == 46 and pyautogui.pixel(830, 850)[1] == 127 and pyautogui.pixel(830, 850)[
        2] == 177):
        pass
    replay()


elif season_choice == Season.SEASON2:
    print(seasons[Season.SEASON2.value])
    pyautogui.moveTo(seasons[Season.SEASON2.value], None, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(None, 500, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.dragTo(990, 300, 1, button='left')
    pyautogui.moveTo(990, 850, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.dragTo(1100, 850, 1, button='left')
    pyautogui.moveTo(850, 850, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.dragTo(1100, 850, 1, button='left')
    time.sleep(2)
    pyautogui.moveTo(950, 780, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1000, 760, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.click()
    button_next()
    pyautogui.click()
    button_fight()
    pyautogui.click()
    while not (pyautogui.pixel(1090, 135)[0] == 251 and pyautogui.pixel(1090, 135)[1] == 251 and pyautogui.pixel(1090,
                                                                                                                 135)[
        2] == 251):
        pass
    button_auto()
    pyautogui.click()
    time.sleep(1)
    while not (pyautogui.pixel(830, 850)[0] == 46 and pyautogui.pixel(830, 850)[1] == 127 and pyautogui.pixel(830, 850)[
        2] == 177):
        pass

    replay()

elif season_choice == Season.SEASON3:
    print(seasons[Season.SEASON3.value])
    pyautogui.moveTo(seasons[Season.SEASON3.value], None, random_x, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.click()

elif season_choice == Season.SEASON4:
    print(seasons[Season.SEASON4.value])
    pyautogui.moveTo(seasons[Season.SEASON4.value], None, random_x, pyautogui.easeOutQuad)
    pyautogui.click()

elif season_choice == Season.SEASON5:
    print(seasons[Season.SEASON5.value])
    pyautogui.moveTo(seasons[Season.SEASON5.value], None, random_x, pyautogui.easeOutQuad)
    pyautogui.click()













#print (Season.SEASON1.value, Province.PROVINCE10.value)










