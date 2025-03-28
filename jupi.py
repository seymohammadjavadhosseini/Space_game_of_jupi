import pgzrun
import random
import math
#______________________________________________طول و عرض صفحه بازی______________________________________________________________
WIDTH = 1200
HEIGHT = 700
#__________________________مشخصات سیاره مشتری شامل 1) موقعیت 2) شعاع های مداری 3) زاویه 4) سرعت _____________________________
jupiter = Actor("jupiter")

jupiter.pos = 1250,750

jupiter.radius_x = 450

jupiter.radius_y = 300

jupiter.angle = 0

jupiter.speed = 1
#__________________________مشخصات سیاره زحل شامل 1) موقعیت 2) شعاع های مداری 3) زاویه 4) سرعت _____________________________
saturn = Actor("saturn")

saturn.pos = 1250,750

saturn.radius_x = 150

saturn.radius_y = 100

saturn.angle = 0

saturn.speed = 0.75
#__________________________مشخصات سیاره نپتون شامل 1) موقعیت 2) شعاع های مداری 3) زاویه 4) سرعت _____________________________
neptune = Actor("neptune")

neptune.pos = 1250,750

neptune.radius_x = 350

neptune.radius_y = 200

neptune.angle = 0

neptune.speed = 1
#__________________________مشخصات سیاره پلوتون شامل 1) موقعیت 2) شعاع های مداری 3) زاویه 4) سرعت _____________________________
pluto = Actor("pluto")

pluto.pos = 1250,750

pluto.radius_x = 250

pluto.radius_y = 150

pluto.angle = 0

pluto.speed = 0.9
#__________________________موقعیت اولیه بازیکن 1 یا همان موجود فضایی شاخک دار__________________________
player_1 = Actor("player_1")
player_1.pos = 80,300
#________________________1موقعیت اولیه سفینه فضایی _________________________________
spaceship_1 = Actor("spaceship_1")
spaceship_1.pos = 400,200
#_________________________موقعیت آیکون فروشگاه در اولین صفحه بعد از خروج از بازی_________________________
shop_button = Actor("shop_button")
shop_button.pos = 600,500

sound_on_button = Actor("sound_on_button")
sound_on_button.pos = 70,60

sound_off_button = Actor("sound_off_button")
sound_off_button.pos = 70,60

background_game_over = Actor("background_game_over")
background_game_over.pos = 600,350

background_game = Actor("background_game")
background_game.pos = 600,350

background_menu = Actor("background_menu")
background_menu.pos = 600,350

background_shop = Actor("background_shop")
background_shop.pos = 600,350

start_game_button = Actor("start_game_button")
start_game_button.pos = 600,350

background_help = Actor("background_help")
background_help.pos = 600,350

diamond1 = Actor("diamond")
diamond1.pos = 495,40

diamond2 = Actor("diamond")
diamond2.pos = 565,40

diamond3 = Actor("diamond")
diamond3.pos = 635,40

alien_enemy = Actor("alien_enemy")
alien_enemy.pos = 1100,500

tir = Actor("tir")
tir.pos = 1060,500

home_button = Actor("home_button")
home_button.pos = 570,450

again_game_button = Actor("again_game_button")
again_game_button.pos = 640,450

player_2 = Actor("player_2")
player_2.pos = 300,200

player_3 = Actor("player_3")
player_3.pos = 300,400

player_4 = Actor("player_4")
player_4.pos = 300,600

spaceship_2 = Actor("spaceship_2")
spaceship_2.pos = 850,200

spaceship_3 = Actor("spaceship_3")
spaceship_3.pos = 850,400

spaceship_4 = Actor("spaceship_4")
spaceship_4.pos = 850,600

back_shop = Actor("back")
back_shop.pos = -80,-100

back_help = Actor("back")
back_help.pos = -50,-10

help_button = Actor("help_button")
help_button.pos = -20,-80

right_key = Actor("right")
right_key.pos = 900,550

left_key = Actor("left")
left_key.pos = 700,550

up_key = Actor("up")
up_key.pos = 800,450

down_key = Actor("down")
down_key.pos = 800,550

space_key = Actor("keyboard_space")
space_key.pos = 830,100

mark_space = Actor("mark_space")
mark_space.pos = 840,137

lock_shop_player2 = Actor("lock")
lock_shop_player2.pos = 250,250

unlock_shop_player2 = Actor("unlock")
unlock_shop_player2.pos = 250,250

lock_shop_player3 = Actor("lock")
lock_shop_player3.pos = 250,450

unlock_shop_player3 = Actor("unlock")
unlock_shop_player3.pos = 250,450

lock_shop_player4 = Actor("lock")
lock_shop_player4.pos = 250,650

unlock_shop_player4 = Actor("unlock")
unlock_shop_player4.pos = 250,650

lock_shop_spaceship2 = Actor("lock")
lock_shop_spaceship2.pos = 800,250

unlock_shop_spaceship2 = Actor("unlock")
unlock_shop_spaceship2.pos = 800,250

lock_shop_spaceship3 = Actor("lock")
lock_shop_spaceship3.pos = 800,450

unlock_shop_spaceship3 = Actor("unlock")
unlock_shop_spaceship3.pos = 800,450

lock_shop_spaceship4 = Actor("lock")
lock_shop_spaceship4.pos = 800,650

unlock_shop_spaceship4 = Actor("unlock")
unlock_shop_spaceship4.pos = 800,650
 
mark_shop_player2 = Actor("mark")
mark_shop_player2.pos = 380,250

mark_shop_player3 = Actor("mark")
mark_shop_player3.pos = 380,450

mark_shop_player4 = Actor("mark")
mark_shop_player4.pos = 380,650

mark_shop_spaceship2 = Actor("mark")
mark_shop_spaceship2.pos = 930,250

mark_shop_spaceship3 = Actor("mark")
mark_shop_spaceship3.pos = 930,450

mark_shop_spaceship4 = Actor("mark")
mark_shop_spaceship4.pos = 930,650

laptop = Actor("laptop")
laptop.pos = 280,480

score = 0

time = 60

money = 99999999

buy_player2 = False

buy_player3 = False

buy_player4 = False

buy_spaceShip2 = False

buy_spaceShip3 = False

buy_spaceShip4 = False

mark_player2 = False

mark_player3 = False

mark_player4 = False

mark_spaceShip2 = False

mark_spaceShip3 = False

mark_spaceShip4 = False

time_start = False

menu_sound = False

num_collisions_tir_ba_player = 0

start_menu = True

game_over_menu = False

draw_diamond1 = True

draw_diamond2 = True

draw_diamond3 = True

madar_beyzi = False

game_start = False

shop_menu = False

help_menu = False

menu_sound = False

sound_score1_1 = False

sound_tir1_1 = False
#_____________دیکشنری شامل متغیرهای بولین کاراکترهای فروشگاه شامل سفینه ها و بازیکنان یا همان موجودات فضایی
dictShop = {
            "shop_player_1": False,

            "shop_player_2": False,

            "shop_player_3": False,

            "shop_player_4": False,

            "shop_spaceship_1": False,

            "shop_spaceship_2": False,

            "shop_spaceship_3": False,

            "shop_spaceship_4": False
           }
#______________دیکشنری شامل متغیر بالاترین امتیاز در بین افرادی که بازی می کنند که ابتدا صفر است___________________________
highest_scoreDict = {
                   "highest_score": 0
                  }
#_______________________________تابع بروزرسانی حرکت سیاره مشتری در مدار بیضوی____________________________________
def update_jupiter():

    jupiter.angle += jupiter.speed
    jupiter.x = WIDTH / 2 + jupiter.radius_x * math.cos(math.radians(jupiter.angle))
    jupiter.y = HEIGHT / 2 + jupiter.radius_y * math.sin(math.radians(jupiter.angle))
#_______________________________تابع بروزرسانی حرکت سیاره زحل در مدار بیضوی____________________________________
def update_saturn():

    saturn.angle += saturn.speed
    saturn.x = WIDTH / 2 + saturn.radius_x * math.cos(math.radians(saturn.angle))
    saturn.y = HEIGHT / 2 + saturn.radius_y * math.sin(math.radians(saturn.angle))
#_______________________________تابع بروزرسانی حرکت سیاره نپتون در مدار بیضوی____________________________________
def update_neptune():

    neptune.angle += neptune.speed
    neptune.x = WIDTH / 2 + neptune.radius_x * math.cos(math.radians(neptune.angle))
    neptune.y = HEIGHT / 2 + neptune.radius_y * math.sin(math.radians(neptune.angle))
#_______________________________تابع بروزرسانی حرکت سیاره پلوتون در مدار بیضوی____________________________________
def update_pluto():

    pluto.angle += pluto.speed
    pluto.x = WIDTH / 2 + pluto.radius_x * math.cos(math.radians(pluto.angle))
    pluto.y = HEIGHT / 2 + pluto.radius_y * math.sin(math.radians(pluto.angle))
#_______________________________تابع اصلی بروزرسانی کلیه حرکات مربوط به تمامی اشیا دارای حرکت در بازی______________________________
def update():
    global score , num_collisions_tir_ba_player , draw_diamond1 , draw_diamond2 , draw_diamond3 , tir , game_over_menu , saturn , sound_off_button , money , sound_tir1_1 , sound_score1_1
    
    if not game_over_menu and game_start == True:
#_______________________________فراخوانی توابع بروزرسانی سیارات________________________________       
        update_jupiter()

        update_saturn()

        update_neptune()

        update_pluto()

        tir.x -= 4

        if tir.x == 0:
           
           alien_enemy.y = random.randint(50,600)
           alien_enemy.x = 1100
           tir.x = alien_enemy.x
           tir.y = alien_enemy.y + 5
#__________________________کدهای مربوط به خطوط 340 تا 467 مربوط به حالتیست که موجود فضایی در بازی به هیچ وجه به بیرون صفحه بازی نمی تواند برود           
#___________________________فشردن کلید جهت راست و حرکت موجود فضایی انتخابی در بازی به راست_____________________________
        if keyboard.right:
            
            if dictShop["shop_player_1"] == True and player_1.x <= WIDTH - 35:
                player_1.x += 4

            if dictShop["shop_player_2"] == True and player_2.x <= WIDTH - 35:
                player_2.x += 4 

            if dictShop["shop_player_3"] == True and player_3.x <= WIDTH - 35:
                player_3.x += 4

            if dictShop["shop_player_4"] == True and player_4.x <= WIDTH - 30:
                player_4.x += 4 
#___________________________فشردن کلید جهت چپ و حرکت موجود فضایی انتخابی در بازی به چپ____________________________
        elif keyboard.left:

            if dictShop["shop_player_1"] == True and player_1.x >= 35:
                player_1.x -= 4

            if dictShop["shop_player_2"] == True and player_2.x >= 35:
                player_2.x -= 4

            if dictShop["shop_player_3"] == True and player_3.x >= 35:
                player_3.x -= 4

            if dictShop["shop_player_4"] == True and player_4.x >= 28:
                player_4.x -= 4
#___________________________فشردن کلید جهت بالا و حرکت موجود فضایی انتخابی در بازی به بالا____________________________
        elif keyboard.up:

            if dictShop["shop_player_1"] == True and player_1.y >= 37:
                player_1.y -= 4

            if dictShop["shop_player_2"] == True and player_2.y >= 35:
                player_2.y -= 4 

            if dictShop["shop_player_3"] == True and player_3.y >= 35:
                player_3.y -= 4

            if dictShop["shop_player_4"] == True and player_4.y >= 34:
                player_4.y -= 4 
#___________________________فشردن کلید جهت پایین و حرکت موجود فضایی انتخابی در بازی به پایین____________________________
        elif keyboard.down:

            if dictShop["shop_player_1"] == True and player_1.y <= HEIGHT - 40:
                player_1.y += 4

            if dictShop["shop_player_2"] == True and player_2.y <= HEIGHT - 38:
                player_2.y += 4

            if dictShop["shop_player_3"] == True and player_3.y <= HEIGHT - 35:
                player_3.y += 4

            if dictShop["shop_player_4"] == True and player_4.y <= HEIGHT - 30:
                player_4.y += 4            
#___________________________فشردن کلید جهت راست و جهت بالا باهم و حرکت موجود فضایی انتخابی در بازی به بالا سمت راست_____________________________         
        if keyboard.right and keyboard.up:

            if dictShop["shop_player_1"] == True and player_1.x <= WIDTH - 35 and  player_1.y >= 35:
                player_1.x += 2
                player_1.y -= 2

            if dictShop["shop_player_2"] == True and player_2.x <= WIDTH - 35 and  player_2.y >= 35:
                player_2.x += 2
                player_2.y -= 2

            if dictShop["shop_player_3"] == True and player_3.x <= WIDTH - 35 and  player_3.y >= 35:
                player_3.x += 2
                player_3.y -= 2

            if dictShop["shop_player_4"] == True and player_4.x <= WIDTH - 30 and  player_4.y >= 30:
                player_4.x += 2
                player_4.y -= 2
#___________________________فشردن کلید جهت راست و جهت پایین باهم و حرکت موجود فضایی انتخابی در بازی به پایین سمت راست_____________________________
        elif keyboard.right and keyboard.down:

            if dictShop["shop_player_1"] == True and player_1.x <= WIDTH - 35 and  player_1.y <= HEIGHT - 35:
                player_1.x += 2
                player_1.y += 2

            if dictShop["shop_player_2"] == True and player_2.x <= WIDTH - 35 and  player_2.y <= HEIGHT - 35:
                player_2.x += 2
                player_2.y += 2

            if dictShop["shop_player_3"] == True and player_3.x <= WIDTH - 35 and  player_3.y <= HEIGHT - 35:
                player_3.x += 2
                player_3.y += 2

            if dictShop["shop_player_4"] == True and player_4.x <= WIDTH - 30 and  player_4.y <= HEIGHT - 30:
                player_4.x += 2
                player_4.y += 2 
#___________________________فشردن کلید جهت چپ و جهت بالا باهم و حرکت موجود فضایی انتخابی در بازی به بالا سمت چپ____________________________
        elif keyboard.left and keyboard.up:

            if dictShop["shop_player_1"] == True and player_1.x >= 35 and  player_1.y >= 35:
                player_1.x -= 2
                player_1.y -= 2

            if dictShop["shop_player_2"] == True and player_2.x >= 35 and  player_2.y >= 35:
                player_2.x -= 2
                player_2.y -= 2

            if dictShop["shop_player_3"] == True and player_3.x >= 35 and  player_3.y >= 35:
                player_3.x -= 2
                player_3.y -= 2

            if dictShop["shop_player_4"] == True and player_4.x >= 30 and  player_4.y >= 30:
                player_4.x -= 2
                player_4.y -= 2   
#___________________________فشردن کلید جهت چپ و جهت پایین باهم و حرکت موجود فضایی انتخابی در بازی به پایین سمت چپ____________________________
        elif keyboard.left and keyboard.down:

            if dictShop["shop_player_1"] == True and player_1.x >= 35 and  player_1.y <= HEIGHT - 35:
                player_1.x -= 2
                player_1.y += 2

            if dictShop["shop_player_2"] == True and player_2.x >= 35 and  player_2.y <= HEIGHT - 35:
                player_2.x -= 2
                player_2.y += 2

            if dictShop["shop_player_3"] == True and player_3.x >= 35 and  player_3.y <= HEIGHT - 35:
                player_3.x -= 2
                player_3.y += 2

            if dictShop["shop_player_4"] == True and player_4.x >= 30 and  player_4.y <= HEIGHT - 30:
                player_4.x -= 2
                player_4.y += 2   
#__________________________کدهای مربوط به خطوط 469 تا 595 مربوط به حالتیست که موجود فضایی در بازی به بیرون صفحه بازی می تواند برود 
        # if keyboard.right:

        #     if dictShop["shop_player_1"]:
        #         player_1.x += 4

        #     if dictShop["shop_player_2"]:
        #         player_2.x += 4 

        #     if dictShop["shop_player_3"]:
        #         player_3.x += 4

        #     if dictShop["shop_player_4"]:
        #         player_4.x += 4 

        # elif keyboard.left:

        #     if dictShop["shop_player_1"]:
        #         player_1.x -= 4

        #     if dictShop["shop_player_2"]:
        #         player_2.x -= 4

        #     if dictShop["shop_player_3"]:
        #         player_3.x -= 4

        #     if dictShop["shop_player_4"]:
        #         player_4.x -= 4

        # elif keyboard.up:

        #     if dictShop["shop_player_1"]:
        #         player_1.y -= 4

        #     if dictShop["shop_player_2"]:
        #         player_2.y -= 4 

        #     if dictShop["shop_player_3"]:
        #         player_3.y -= 4

        #     if dictShop["shop_player_4"]:
        #         player_4.y -= 4 

        # elif keyboard.down:

        #     if dictShop["shop_player_1"]:
        #         player_1.y += 4

        #     if dictShop["shop_player_2"]:
        #         player_2.y += 4

        #     if dictShop["shop_player_3"]:
        #         player_3.y += 4

        #     if dictShop["shop_player_4"]:
        #         player_4.y += 4            
         
        # if keyboard.right and keyboard.up:

        #     if dictShop["shop_player_1"]:
        #         player_1.x += 2
        #         player_1.y -= 2

        #     if dictShop["shop_player_2"]:
        #         player_2.x += 2
        #         player_2.y -= 2

        #     if dictShop["shop_player_3"]:
        #         player_3.x += 2
        #         player_3.y -= 2

        #     if dictShop["shop_player_4"]:
        #         player_4.x += 2
        #         player_4.y -= 2

        # elif keyboard.right and keyboard.down:

        #     if dictShop["shop_player_1"]:
        #         player_1.x += 2
        #         player_1.y += 2

        #     if dictShop["shop_player_2"]:
        #         player_2.x += 2
        #         player_2.y += 2

        #     if dictShop["shop_player_3"]:
        #         player_3.x += 2
        #         player_3.y += 2

        #     if dictShop["shop_player_4"]:
        #         player_4.x += 2
        #         player_4.y += 2 

        # elif keyboard.left and keyboard.up:

        #     if dictShop["shop_player_1"]:
        #         player_1.x -= 2
        #         player_1.y -= 2

        #     if dictShop["shop_player_2"]:
        #         player_2.x -= 2
        #         player_2.y -= 2

        #     if dictShop["shop_player_3"]:
        #         player_3.x -= 2
        #         player_3.y -= 2

        #     if dictShop["shop_player_4"]:
        #         player_4.x -= 2
        #         player_4.y -= 2   

        # elif keyboard.left and keyboard.down:

        #     if dictShop["shop_player_1"]:
        #         player_1.x -= 2
        #         player_1.y += 2

        #     if dictShop["shop_player_2"]:
        #         player_2.x -= 2
        #         player_2.y += 2

        #     if dictShop["shop_player_3"]:
        #         player_3.x -= 2
        #         player_3.y += 2

        #     if dictShop["shop_player_4"]:
        #         player_4.x -= 2
        #         player_4.y += 2 
#_____________________برخورد موجود فضایی شاخک دار با هر سفینه انتخابی و سیارات و تیر دشمن فضایی بیگانه در بازی و شرایط مربوطه به وجود آمده تحت تاثیر آن________________________
        if dictShop["shop_player_1"]:

            # if player_1.x < -50:
            #     player_1.x = WIDTH + 50

            # elif player_1.x > WIDTH + 50:
            #     player_1.x = -50

            # elif player_1.y < -50:
            #     player_1.y = HEIGHT + 50

            # elif player_1.y > HEIGHT + 50:
            #     player_1.y = -50

            if dictShop["shop_spaceship_1"]:  

                if player_1.colliderect(spaceship_1):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_1.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200) 

            if dictShop["shop_spaceship_2"]:

                if player_1.colliderect(spaceship_2):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_2.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_3"]:

                if player_1.colliderect(spaceship_3):
                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_3.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_4"]:

                if player_1.colliderect(spaceship_4):
                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_4.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)                          

            if player_1.colliderect(jupiter):
                game_over_menu = True

            if player_1.colliderect(saturn):
                game_over_menu = True

            if player_1.colliderect(neptune):
                game_over_menu = True       

            if player_1.colliderect(pluto):
                game_over_menu = True     

            if player_1.colliderect(tir):

                num_collisions_tir_ba_player += 1
                alien_enemy.y = random.randint(50,600)
                alien_enemy.x = 1100
                tir.x = alien_enemy.x
                tir.y = alien_enemy.y + 5

                if num_collisions_tir_ba_player == 1:

                    draw_diamond1 = True
                    draw_diamond2 = True
                    draw_diamond3 = False

                elif num_collisions_tir_ba_player == 2:

                    draw_diamond1 = True
                    draw_diamond2 = False
                    draw_diamond3 = False
                    
                elif num_collisions_tir_ba_player == 3:

                    draw_diamond1 = False
                    draw_diamond2 = False
                    draw_diamond3 = False 
                    game_over_menu = True  
#_____________________برخورد موجود فضایی کله سبز با هر سفینه انتخابی و سیارات و تیر دشمن فضایی بیگانه در بازی و شرایط مربوطه به وجود آمده تحت تاثیر آن________________________
        if dictShop["shop_player_2"]:

            # if player_2.x < -50:
            #     player_2.x = WIDTH + 50

            # elif player_2.x > WIDTH + 50:
            #     player_2.x = -50

            # elif player_2.y < -50:
            #     player_2.y = HEIGHT + 50

            # elif player_2.y > HEIGHT + 50:
            #     player_2.y = -50

            if dictShop["shop_spaceship_1"]:

                if player_2.colliderect(spaceship_1):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_1.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_2"]:

                if player_2.colliderect(spaceship_2):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_2.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_3"]:

                if player_2.colliderect(spaceship_3):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_3.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_4"]:

                if player_2.colliderect(spaceship_4):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_4.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if player_2.colliderect(jupiter):
                game_over_menu = True
                 
            if player_2.colliderect(saturn):
                game_over_menu = True

            if player_2.colliderect(neptune):
                game_over_menu = True

            if player_2.colliderect(pluto):
                game_over_menu = True 

            if player_2.colliderect(tir):

                num_collisions_tir_ba_player += 1
                alien_enemy.y = random.randint(50,600)
                alien_enemy.x = 1100
                tir.x = alien_enemy.x
                tir.y = alien_enemy.y + 5
                
                if num_collisions_tir_ba_player == 1:

                    draw_diamond1 = True
                    draw_diamond2 = True
                    draw_diamond3 = False

                elif num_collisions_tir_ba_player == 2:

                    draw_diamond1 = True
                    draw_diamond2 = False
                    draw_diamond3 = False
                    
                elif num_collisions_tir_ba_player == 3:

                    draw_diamond1 = False
                    draw_diamond2 = False
                    draw_diamond3 = False 
                    game_over_menu = True
#_____________________برخورد موجود فضایی بنفش با هر سفینه انتخابی و سیارات و تیر دشمن فضایی بیگانه در بازی و شرایط مربوطه به وجود آمده تحت تاثیر آن________________________
        if dictShop["shop_player_3"]:

            # if player_3.x < -50:
            #     player_3.x = WIDTH + 50

            # elif player_3.x > WIDTH + 50:
            #     player_3.x = -50

            # elif player_3.y < -50:
            #     player_3.y = HEIGHT + 50

            # elif player_3.y > HEIGHT + 50:
            #     player_3.y = -50

            if dictShop["shop_spaceship_1"]:

                if player_3.colliderect(spaceship_1):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_1.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_2"]:

                if player_3.colliderect(spaceship_2):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_2.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_3"]:

                if player_3.colliderect(spaceship_3):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_3.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_4"]:

                if player_3.colliderect(spaceship_4):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_4.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if player_3.colliderect(jupiter):
                game_over_menu = True

            if player_3.colliderect(saturn):
                game_over_menu = True

            if player_3.colliderect(neptune):
                game_over_menu = True

            if player_3.colliderect(pluto):
                game_over_menu = True

            if player_3.colliderect(tir):

                num_collisions_tir_ba_player += 1
                alien_enemy.y = random.randint(50,600)
                alien_enemy.x = 1100
                tir.x = alien_enemy.x
                tir.y = alien_enemy.y + 5
                
                if num_collisions_tir_ba_player == 1:

                    draw_diamond1 = True
                    draw_diamond2 = True
                    draw_diamond3 = False

                elif num_collisions_tir_ba_player == 2:

                    draw_diamond1 = True
                    draw_diamond2 = False
                    draw_diamond3 = False
                    
                elif num_collisions_tir_ba_player == 3:

                    draw_diamond1 = False
                    draw_diamond2 = False
                    draw_diamond3 = False 
                    game_over_menu = True 
#_____________________برخورد موجود فضایی کله کوچک با هر سفینه انتخابی و سیارات و تیر دشمن فضایی بیگانه در بازی و شرایط مربوطه به وجود آمده تحت تاثیر آن________________________
        if dictShop["shop_player_4"]:

            # if player_4.x < -50:
            #     player_4.x = WIDTH + 50

            # elif player_4.x > WIDTH + 50:
            #     player_4.x = -50

            # elif player_4.y < -50:
            #     player_4.y = HEIGHT + 50

            # elif player_4.y > HEIGHT + 50:
            #     player_4.y = -50

            if dictShop["shop_spaceship_1"]:

                if player_4.colliderect(spaceship_1):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_1.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_2"]:

                if player_4.colliderect(spaceship_2):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_2.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_3"]:

                if player_4.colliderect(spaceship_3):
                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_3.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)

            if dictShop["shop_spaceship_4"]:

                if player_4.colliderect(spaceship_4):

                    score += 10
                    money += 10
                    if highest_scoreDict["highest_score"] < score:
                        highest_scoreDict["highest_score"] = score
                    spaceship_4.pos = random.randint(100,WIDTH-200),random.randint(100,HEIGHT-200)       

            if player_4.colliderect(jupiter):
                game_over_menu = True 

            if player_4.colliderect(neptune):
                game_over_menu = True 

            if player_4.colliderect(saturn):
                game_over_menu = True

            if player_4.colliderect(pluto):
                game_over_menu = True 

            if player_4.colliderect(tir):

                num_collisions_tir_ba_player += 1
                alien_enemy.y = random.randint(50,600)
                alien_enemy.x = 1100
                tir.x = alien_enemy.x
                tir.y = alien_enemy.y + 5
                
                if num_collisions_tir_ba_player == 1:

                    draw_diamond1 = True
                    draw_diamond2 = True
                    draw_diamond3 = False

                elif num_collisions_tir_ba_player == 2:

                    draw_diamond1 = True
                    draw_diamond2 = False
                    draw_diamond3 = False
                    
                elif num_collisions_tir_ba_player == 3:

                    draw_diamond1 = False
                    draw_diamond2 = False
                    draw_diamond3 = False 
                    game_over_menu = True                            
#_________________________________________تابع نوشتن متن و کشیدن تمامی اشیا درون بازی______________________________________________
def draw():
    global time_start , menu_sound

    if start_menu:

        screen.clear()
        background_menu.draw()
        start_game_button.draw()
        shop_button.draw()
        help_button.draw()
        shop_button.pos = 600,500
        help_button.pos = 70,620
        back_shop.pos = -30,-50
        back_help.pos = -50,-70

        if not menu_sound: 

            sound_on_button.draw()
            sounds.x.play()

        elif menu_sound:

            sound_off_button.draw()
            sounds.x.stop()
#________________________________________کد نمایش صفحه فروشگاه بازی___________________________________________        
    elif shop_menu:

        screen.clear()

        background_shop.draw()

        screen.draw.text(f"your money : {money}$",color= "white",topleft=(30,20),fontsize=30)

        screen.draw.text("Alien",color= "white",topleft=(230,50),fontsize=80)

        player_2.draw()

        text_box_rect = Rect(270, 240, 80, 37)
        screen.draw.filled_rect(text_box_rect,"black") 

        screen.draw.text("100$",color= "white",topleft=(270,240),fontsize=50)

        if buy_player2:
            unlock_shop_player2.draw()

        if not buy_player2:
            lock_shop_player2.draw()

        if mark_player2:
            mark_shop_player2.draw()    

        player_3.draw()

        text_box_rect = Rect(270, 440, 80, 37)
        screen.draw.filled_rect(text_box_rect,"black")

        screen.draw.text("200$",color= "white",topleft=(270,440),fontsize=50)

        if buy_player3:
            unlock_shop_player3.draw()

        if not buy_player3:    
            lock_shop_player3.draw()
        
        if mark_player3:
            mark_shop_player3.draw()

        player_4.draw()

        text_box_rect = Rect(270, 640, 80, 37)
        screen.draw.filled_rect(text_box_rect,"black")

        screen.draw.text("300$",color= "white",topleft=(270,640),fontsize=50)

        if buy_player4:
            unlock_shop_player4.draw()

        if not buy_player4:    
            lock_shop_player4.draw()

        if mark_player4:
            mark_shop_player4.draw()    

        screen.draw.text("Spaceship",color= "white",topleft=(710,50),fontsize=80)

        spaceship_2.draw()

        text_box_rect = Rect(820, 240, 80, 37)
        screen.draw.filled_rect(text_box_rect,"black")

        screen.draw.text("400$",color= "white",topleft=(820,240),fontsize=50)

        if buy_spaceShip2:
            unlock_shop_spaceship2.draw()

        if not buy_spaceShip2:    
            lock_shop_spaceship2.draw()

        if mark_spaceShip2:
            mark_shop_spaceship2.draw()    


        spaceship_3.draw()

        text_box_rect = Rect(820, 440, 80, 37)
        screen.draw.filled_rect(text_box_rect,"black")

        screen.draw.text("500$",color= "white",topleft=(820,440),fontsize=50)

        if buy_spaceShip3:
            unlock_shop_spaceship3.draw()

        if not buy_spaceShip3:    
            lock_shop_spaceship3.draw()

        if mark_spaceShip3:
            mark_shop_spaceship3.draw()    

        spaceship_4.draw()

        text_box_rect = Rect(820, 640, 80, 37)
        screen.draw.filled_rect(text_box_rect,"black")

        screen.draw.text("600$",color= "white",topleft=(820,640),fontsize=50)

        if buy_spaceShip4:
            unlock_shop_spaceship4.draw()

        if not buy_spaceShip4:
            lock_shop_spaceship4.draw()

        if mark_spaceShip4:
            mark_shop_spaceship4.draw()    

        back_shop.draw()
#___________________________________کد نمایش صفحه راهنمای بازی_____________________________________
    elif help_menu:

        screen.clear()
        background_help.draw()

        right_key.draw()
        screen.draw.text("Move to Right",color= "light grey",topleft=(960,540),fontsize=40)

        left_key.draw()
        screen.draw.text("Move to Left",color= "light grey",topleft=(470,540),fontsize=40)

        up_key.draw()
        screen.draw.text("Move to Up",color= "white",topleft=(720,360),fontsize=40)

        down_key.draw()
        screen.draw.text("Move to Down",color= "white",topleft=(720,620),fontsize=40)

        space_key.draw()
        screen.draw.text("start game",color= "white",topleft=(760,170),fontsize=40)
        mark_space.draw()

        laptop.draw()
        text_box_rect = Rect(210, 330, 138, 31)
        screen.draw.filled_rect(text_box_rect,"black")
        screen.draw.text("Producers",color= "white",topleft=(210,330),fontsize=40)
        screen.draw.text("Mr Tafazoli",color= "black",topleft=(210,400),fontsize=30)
        screen.draw.text("Mr Hosseini",color= "black",topleft=(210,430),fontsize=30)
        screen.draw.text("Miss Jamshidi",color= "black",topleft=(210,460),fontsize=30)

        back_help.draw()
        back_shop.pos = -50,-50
        help_button.pos = -20,-20
        back_help.pos = 70,620
#________________________________________کد اصلی برای شروع بازی و شروع و گذران زمان بازی_________________________________________
    else:
      
        background_game.draw()
        player_1.draw()

        if dictShop["shop_spaceship_1"]:
            spaceship_1.draw()

        if dictShop["shop_spaceship_2"]:
            spaceship_2.draw()

        if dictShop["shop_spaceship_3"]:
            spaceship_3.draw() 

        if dictShop["shop_spaceship_4"]:

            spaceship_4.draw()

        jupiter.draw()
        neptune.draw()
        pluto.draw()
        saturn.draw()
        alien_enemy.draw()
        tir.draw()

        screen.draw.text(f"SCORE : {score}",color= "white",topleft=(30,20),fontsize=60)

        screen.draw.text(f"TIME : {time}",color= "white",topleft=(30,60),fontsize=60)
        
        if draw_diamond1:
            diamond1.draw()

        if draw_diamond2:    
            diamond2.draw()

        if draw_diamond3:    
            diamond3.draw()

        if dictShop["shop_player_2"]:

            screen.clear()
            sounds.x.stop()
            background_game.draw()

            if dictShop["shop_spaceship_1"]:
                spaceship_1.draw()

            if dictShop["shop_spaceship_2"]:
                spaceship_2.draw()

            if dictShop["shop_spaceship_3"]:
                spaceship_3.draw()

            if dictShop["shop_spaceship_4"]:
                spaceship_4.draw() 

            player_2.draw()

            jupiter.draw()

            neptune.draw()

            pluto.draw()

            saturn.draw()

            alien_enemy.draw()

            tir.draw()

            screen.draw.text(f"SCORE : {score}",color= "white",topleft=(30,20),fontsize=60)

            screen.draw.text(f"TIME : {time}",color= "white",topleft=(30,60),fontsize=60)

            if draw_diamond1:
                diamond1.draw()

            if draw_diamond2:    
                diamond2.draw()

            if draw_diamond3:    
                diamond3.draw() 

        if dictShop["shop_player_3"]:

            screen.clear()
            sounds.x.stop()
            background_game.draw()

            if dictShop["shop_spaceship_1"]:
                spaceship_1.draw()

            if dictShop["shop_spaceship_2"]:
                spaceship_2.draw()

            if dictShop["shop_spaceship_3"]:
                spaceship_3.draw() 

            if dictShop["shop_spaceship_4"]:
                spaceship_4.draw()

            player_3.draw()

            jupiter.draw()

            neptune.draw()

            pluto.draw()

            saturn.draw()

            alien_enemy.draw()

            tir.draw()

            screen.draw.text(f"SCORE : {score}",color= "white",topleft=(30,20),fontsize=60)

            screen.draw.text(f"TIME : {time}",color= "white",topleft=(30,60),fontsize=60)

            if draw_diamond1:
                diamond1.draw()

            if draw_diamond2:    
                diamond2.draw()

            if draw_diamond3:    
                diamond3.draw()

        if dictShop["shop_player_4"]:

            screen.clear()
            sounds.x.stop()
            background_game.draw()

            if dictShop["shop_spaceship_1"]:
                spaceship_1.draw()

            if dictShop["shop_spaceship_2"]:
                spaceship_2.draw()

            if dictShop["shop_spaceship_3"]:
                spaceship_3.draw()

            if dictShop["shop_spaceship_4"]:
                spaceship_4.draw()

            player_4.draw()

            jupiter.draw()

            neptune.draw()

            pluto.draw()

            saturn.draw()

            alien_enemy.draw()

            tir.draw()

            screen.draw.text(f"SCORE : {score}",color= "white",topleft=(30,20),fontsize=60)

            screen.draw.text(f"TIME : {time}",color= "white",topleft=(30,60),fontsize=60)

            if draw_diamond1:
                diamond1.draw()

            if draw_diamond2:    
                diamond2.draw()

            if draw_diamond3:    
                diamond3.draw()        
#__________________________________game overکد برای حالت اتمام بازی تحت شرایط مختلف و نمایش صفحه ___________________________________
    if game_over_menu:

        screen.clear()

        background_game_over.draw()

        screen.draw.text("FINISH GAME",color= "red",topleft=(300,180),fontsize=130)

        screen.draw.text(f"HIGHEST SCORE IS : {highest_scoreDict['highest_score']}",color= "black",topleft=(380,300),fontsize=60)

        screen.draw.text(f"YOUR SCORE IS : {score}",color= "black",topleft=(400,350),fontsize=60)

        shop_button.pos = -200,-200

        home_button.draw()

        again_game_button.draw()
#_________________________________تابع کلیک چپ کردن روی آیکون های مختلف تحت شرایط خاص____________________________________
def on_mouse_down(pos):
    global start_menu , num_collisions_tir_ba_player , draw_diamond1 , draw_diamond2 , draw_diamond3 , time_start , game_over_menu , madar_beyzi , game_start , score , time , shop_menu , menu_sound , shop_player_2 , shop_player_1 , shop_player_3 , shop_player_4 , money , shop_spaceship_1 , shop_spaceship_2 , shop_spaceship_3 , shop_spaceship_4 , help_menu , buy_player2 , buy_player3 , buy_player4 , buy_spaceShip2 , buy_spaceShip3 , buy_spaceShip4 , mark_player2 , mark_player3 , mark_player4 , mark_spaceShip2 , mark_spaceShip3 , mark_spaceShip4

    if start_game_button.collidepoint(pos):

        start_menu = False
        dictShop["shop_player_1"] = True
        dictShop["shop_spaceship_1"] = True

        if dictShop["shop_spaceship_2"]:

            dictShop["shop_spaceship_1"] = False
            dictShop["shop_spaceship_3"] = False
            dictShop["shop_spaceship_4"] = False

        if dictShop["shop_spaceship_3"]:

            dictShop["shop_spaceship_1"] = False
            dictShop["shop_spaceship_2"] = False 
            dictShop["shop_spaceship_4"] = False

        if dictShop["shop_spaceship_4"]:

            dictShop["shop_spaceship_1"] = False
            dictShop["shop_spaceship_2"] = False 
            dictShop["shop_spaceship_3"] = False

        player_2.pos = 80,300

        player_3.pos = 80,300

        player_4.pos = 80,300

        spaceship_2.pos = 400,200

        spaceship_3.pos = 400,200

        spaceship_4.pos = 400,200
#____________________________________________کد برای بازگشت به صفحه اصلی بازی_______________________________________________
    if home_button.collidepoint(pos):

        start_menu = True

        game_over_menu = False

        time_start = False

        game_start = False

        num_collisions_tir_ba_player = 0

        score = 0

        time = 60

        spaceship_1.pos = 400,200

        player_1.pos = 80,300

        alien_enemy.pos = 1100,500

        tir.pos = 1060,500
#_____________________________________________کد برای بازی مجدد______________________________________________
    if again_game_button.collidepoint(pos):

        start_menu = False

        game_over_menu = False

        time_start = False

        draw_diamond1 = True

        draw_diamond2 = True

        draw_diamond3 = True

        madar_beyzi = False

        game_start = False

        num_collisions_tir_ba_player = 0

        score = 0

        time = 60

        spaceship_1.pos = 400,200

        spaceship_2.pos = 400,200

        spaceship_3.pos = 400,200

        spaceship_4.pos = 400,200 

        player_1.pos = 80,300

        player_2.pos = 80,300

        player_3.pos = 80,300

        player_4.pos = 80,300

        alien_enemy.pos = 1100,500

        tir.pos = 1060,500

    if player_2.collidepoint(pos):

        if not dictShop["shop_player_2"] and buy_player2 == False:

            if money >= 100:

                money -= 100 
                buy_player2 = True
                dictShop["shop_player_2"] = True
                dictShop["shop_player_1"] = False
                dictShop["shop_player_3"] = False
                dictShop["shop_player_4"] = False
            else:

                dictShop["shop_player_2"] = False
                dictShop["shop_player_1"] = True
                dictShop["shop_player_3"] = False
                dictShop["shop_player_4"] = False
        if buy_player2:

            dictShop["shop_player_2"] = True
            dictShop["shop_player_1"] = False
            dictShop["shop_player_3"] = False
            dictShop["shop_player_4"] = False
            mark_player2 = True
            mark_player3 = False
            mark_player4 = False
                     


    if player_3.collidepoint(pos):

        if not dictShop["shop_player_3"] and buy_player3 == False:

            if money >= 200:

                money -= 200 
                buy_player3 = True
                dictShop["shop_player_2"] = False
                dictShop["shop_player_1"] = False 
                dictShop["shop_player_3"] = True 
                dictShop["shop_player_4"] = False

            else:

                dictShop["shop_player_2"] = False
                dictShop["shop_player_1"] = True
                dictShop["shop_player_3"] = False
                dictShop["shop_player_4"] = False 

        if buy_player3:
            dictShop["shop_player_2"] = False
            dictShop["shop_player_1"] = False 
            dictShop["shop_player_3"] = True 
            dictShop["shop_player_4"] = False
            mark_player2 = False
            mark_player3 = True
            mark_player4 = False         

    if player_4.collidepoint(pos):

        if not dictShop["shop_player_4"] and buy_player4 == False:

            if money >= 300:
                
                money -= 300
                buy_player4 = True
                dictShop["shop_player_2"] = False
                dictShop["shop_player_1"] = False 
                dictShop["shop_player_3"] = False
                dictShop["shop_player_4"] = True

            else:

                dictShop["shop_player_2"] = False
                dictShop["shop_player_1"] = True
                dictShop["shop_player_3"] = False
                dictShop["shop_player_4"] = False
  
        if buy_player4:
            dictShop["shop_player_2"] = False
            dictShop["shop_player_1"] = False 
            dictShop["shop_player_3"] = False
            dictShop["shop_player_4"] = True
            mark_player2 = False
            mark_player3 = False
            mark_player4 = True
    

    if spaceship_2.collidepoint(pos):

        if not dictShop["shop_spaceship_2"] and buy_spaceShip2 == False:

            if money >= 400:

                money -= 400
                buy_spaceShip2 = True
                dictShop["shop_spaceship_1"] = False
                dictShop["shop_spaceship_2"] = True
                dictShop["shop_spaceship_3"] = False
                dictShop["shop_spaceship_4"] = False

            else:

                dictShop["shop_spaceship_1"] = True
                dictShop["shop_spaceship_2"] = False
                dictShop["shop_spaceship_3"] = False
                dictShop["shop_spaceship_4"] = False

        if buy_spaceShip2:
            dictShop["shop_spaceship_1"] = False
            dictShop["shop_spaceship_2"] = True
            dictShop["shop_spaceship_3"] = False
            dictShop["shop_spaceship_4"] = False
            mark_spaceShip2 = True
            mark_spaceShip3 = False
            mark_spaceShip4 = False


    if spaceship_3.collidepoint(pos):

        if not dictShop["shop_spaceship_3"] and buy_spaceShip3 == False:

            if money >= 500:
            
                money -= 500
                buy_spaceShip3 = True
                dictShop["shop_spaceship_1"] = False
                dictShop["shop_spaceship_2"] = False
                dictShop["shop_spaceship_3"] = True
                dictShop["shop_spaceship_4"] = False

            else:

                dictShop["shop_spaceship_1"] = True
                dictShop["shop_spaceship_2"] = False
                dictShop["shop_spaceship_3"] = False
                dictShop["shop_spaceship_4"] = False

        if buy_spaceShip3:
            dictShop["shop_spaceship_1"] = False
            dictShop["shop_spaceship_2"] = False
            dictShop["shop_spaceship_3"] = True
            dictShop["shop_spaceship_4"] = False
            mark_spaceShip2 = False
            mark_spaceShip3 = True
            mark_spaceShip4 = False        

    if spaceship_4.collidepoint(pos):

        if not dictShop["shop_spaceship_4"] and buy_spaceShip4 == False:

            if money >= 600:

                money -= 600
                buy_spaceShip4 = True
                dictShop["shop_spaceship_1"] = False
                dictShop["shop_spaceship_2"] = False
                dictShop["shop_spaceship_3"] = False
                dictShop["shop_spaceship_4"] = True 

            else:

                dictShop["shop_spaceship_1"] = True
                dictShop["shop_spaceship_2"] = False
                dictShop["shop_spaceship_3"] = False
                dictShop["shop_spaceship_4"] = False

        if buy_spaceShip4:
            dictShop["shop_spaceship_1"] = False
            dictShop["shop_spaceship_2"] = False
            dictShop["shop_spaceship_3"] = False
            dictShop["shop_spaceship_4"] = True
            mark_spaceShip2 = False
            mark_spaceShip3 = False
            mark_spaceShip4 = True        

    if shop_button.collidepoint(pos):

        shop_menu = True  
        start_menu = False 
        player_2.pos = 300,200 
        player_3.pos = 300,400
        player_4.pos = 300,600
        spaceship_2.pos = 850,200
        spaceship_3.pos = 850,400
        spaceship_4.pos = 850,600
        back_shop.pos = 70,620
        back_help.pos = -50,-50
        help_button.pos = -50,-90

    if back_shop.collidepoint(pos):

        shop_menu = False
        help_menu = False
        start_menu = True 

    if sound_on_button.collidepoint(pos):

        menu_sound = True
        sound_off_button.pos = 70,60
        sound_on_button.pos = -50,-50

    elif sound_off_button.collidepoint(pos):

        menu_sound = False
        sound_off_button.pos = -50,-50
        sound_on_button.pos = 70,60
        
    if help_button.collidepoint(pos):\

        help_menu = True
        start_menu = False
        shop_menu = False

    if back_help.collidepoint(pos):
        
        shop_menu = False
        help_menu = False
        start_menu = True  
        back_shop.pos = -50,-50
        back_help.pos = -10,-50
        help_button.pos = 70,620   
#_______________________________________space تابع برای شروع بازی با فشردن کلید _______________________________________
def on_key_down(key):
    global game_start , time_start

    if key == keys.SPACE:
        game_start = True
        time_start = True  
#_______________________________________تابع برای گذران زمان بازی_________________________________________  
def time_left():
    global time, game_over_menu , time_start 

    if time_start:
        if time:
            time -= 1   
        else:
            game_over_menu = True
#___________________________________کد برای کنترل سرعت گذران زمان بازی______________________________________
clock.schedule_interval(time_left, 1)

pgzrun.go()