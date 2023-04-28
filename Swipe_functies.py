##################
#Alles importeren#
##################

import numpy as np
import pygame as pg
import random as r
import time as t
import pdb

pg.init()
pg.font.init()
#lucidaconsole
titelfont = pg.font.Font('papyrus',72)
menufont = pg.font.Font('papyrus',36)
menufont_klein = pg.font.Font('papyrus',25)
tekstfont = pg.font.Font('papyrus',15)
tekst_groot_font = pg.font.Font('papyrus',23)
settings_font = pg.font.Font('papyrus',20)

#level_load = np.genfromtxt('Assets/level.txt',dtype='str',delimiter=' ')

#####################
#Importeren - Foto's#
#####################

def import_foto(name,sizex=50,sizey=50):
    foto_rauw = pg.image.load(name)
    foto_af = pg.transform.scale(foto_rauw,(sizex,sizey))
    return foto_af

finish_foto = import_foto("Assets/Finish.png")

stekels_foto = import_foto("Assets/Stekels.png",50,25)
stekels2_foto = import_foto("Assets/Stekels2.png",50,25)
stekels3_foto = import_foto("Assets/Stekels3.png",50,25)

munt_klein_foto = import_foto("Assets/coin-1.png",30,30)
munt_cut_foto = import_foto("Assets/coinCut.png",30,30)
munt_foto = import_foto("Assets/coin-1.png",40,40)
munt1_foto = import_foto("Assets/coin-1.png",40,40)
munt2_foto = import_foto("Assets/coin-2.png",40,40)
munt3_foto = import_foto("Assets/coin-3.png",40,40)
munt4_foto = import_foto("Assets/coin-4.png",40,40)
munt5_foto = import_foto("Assets/coin-5.png",40,40)
munt6_foto = import_foto("Assets/coin-4.png",40,40)
munt7_foto = import_foto("Assets/coin-3.png",40,40)
munt8_foto = import_foto("Assets/coin-2.png",40,40)

muntx2_foto = import_foto("Assets/coinx2-1.png",40,40)
muntx21_foto = import_foto("Assets/coinx2-1.png",40,40)
muntx22_foto = import_foto("Assets/coinx2-2.png",40,40)
muntx23_foto = import_foto("Assets/coinx2-3.png",40,40)
muntx24_foto = import_foto("Assets/coinx2-4.png",40,40)
muntx25_foto = import_foto("Assets/coinx2-5.png",40,40)
muntx26_foto = import_foto("Assets/coinx2-4.png",40,40)
muntx27_foto = import_foto("Assets/coinx2-3.png",40,40)
muntx28_foto = import_foto("Assets/coinx2-2.png",40,40)

hartje_klein_foto = import_foto("Assets/heart1.png",30,30)
hartje_foto = import_foto("Assets/heart1.png",40,40)
hartje1_foto = import_foto("Assets/heart1.png",40,40)
hartje2_foto = import_foto("Assets/heart2.png",40,40)
hartje3_foto = import_foto("Assets/heart3.png",40,40)
hartje4_foto = import_foto("Assets/heart2.png",40,40)

kogel_foto = import_foto("Assets/kogel-1.png",40,40)
kogel1_foto = import_foto("Assets/kogel-1.png",40,40)
kogel2_foto = import_foto("Assets/kogel-2.png",40,40)
kogel3_foto = import_foto("Assets/kogel-3.png",40,40)
kogel4_foto = import_foto("Assets/kogel-2.png",40,40)

kogel_klein_foto = import_foto("Assets/kogel-klein.png",25,50)
kogel_middel_foto = import_foto("Assets/kogel-1.png",15,30)
kogel_groot_foto = import_foto("Assets/kogel-1.png")

versnelling_foto = import_foto("Assets/Speed-1.png",40,40)
versnelling1_foto = import_foto("Assets/Speed-1.png",40,40)
versnelling2_foto = import_foto("Assets/Speed-2.png",40,40)
versnelling3_foto = import_foto("Assets/Speed-3.png",40,40)
versnelling4_foto = import_foto("Assets/Speed-4.png",40,40)
versnelling5_foto = import_foto("Assets/Speed-5.png",40,40)
versnelling6_foto = import_foto("Assets/Speed-6.png",40,40)
versnelling7_foto = import_foto("Assets/Speed-7.png",40,40)

schild_foto = import_foto("Assets/Shield-1.png",40,40)
schild1_foto = import_foto("Assets/Shield-1.png",40,40)
schild2_foto = import_foto("Assets/Shield-2.png",40,40)
schild3_foto = import_foto("Assets/Shield-3.png",40,40)
schild4_foto = import_foto("Assets/Shield-4.png",40,40)
schild5_foto = import_foto("Assets/Shield-5.png",40,40)
schild6_foto = import_foto("Assets/Shield-4.png",40,40)
schild7_foto = import_foto("Assets/Shield-3.png",40,40)
schild8_foto = import_foto("Assets/Shield-2.png",40,40)

plant1_foto = import_foto("Assets/Plant-1.png")
plant2_foto = import_foto("Assets/Plant-2.png")
plant3_foto = import_foto("Assets/Plant-3.png")
plant4_foto = import_foto("Assets/Plant-2.png")

Dec11 = import_foto("Assets/Dec1-1.png",100,100)
Dec12 = import_foto("Assets/Dec1-2.png",100,100)
Dec13 = import_foto("Assets/Dec1-3.png",100,100)

Dec21 = import_foto("Assets/Dec2-1.png",100,100)
Dec22 = import_foto("Assets/Dec2-2.png",100,100)
Dec23 = import_foto("Assets/Dec2-3.png",100,100)

Dec31 = import_foto("Assets/Dec3-1.png",100,100)
Dec32 = import_foto("Assets/Dec3-2.png",100,100)
Dec33 = import_foto("Assets/Dec3-3.png",100,100)

checkpoint1_foto = import_foto("Assets/Checkpoint-1.png")
checkpoint2_foto = import_foto("Assets/Checkpoint-2.png")
checkpoint3_foto = import_foto("Assets/Checkpoint-3.png")
checkpoint4_foto = import_foto("Assets/Checkpoint-4.png")
checkpoint5_foto = import_foto("Assets/Checkpoint-5.png")
checkpoint6_foto = import_foto("Assets/Checkpoint-6.png")
checkpoint7_foto = import_foto("Assets/Checkpoint-7.png")
checkpoint8_foto = import_foto("Assets/Checkpoint-8.png")
checkpoint9_foto = import_foto("Assets/Checkpoint-9.png")
checkpoint10_foto = import_foto("Assets/Checkpoint-10.png")
checkpoint11_foto = import_foto("Assets/Checkpoint-11.png")

whirl1_foto = import_foto("Assets/Whirl-1.png")
whirl2_foto = import_foto("Assets/Whirl-2.png")
whirl3_foto = import_foto("Assets/Whirl-3.png")
whirl4_foto = import_foto("Assets/Whirl-4.png")
whirl5_foto = import_foto("Assets/Whirl-5.png")
whirl6_foto = import_foto("Assets/Whirl-6.png")
whirl7_foto = import_foto("Assets/Whirl-7.png")
whirl8_foto = import_foto("Assets/Whirl-8.png")
whirl9_foto = import_foto("Assets/Whirl-9.png")
whirl10_foto = import_foto("Assets/Whirl-10.png")
whirl11_foto = import_foto("Assets/Whirl-11.png")
whirl12_foto = import_foto("Assets/Whirl-12.png")

blob1_foto = import_foto("Assets/Blob-1.png")
blob2_foto = import_foto("Assets/Blob-2.png")
blob3_foto = import_foto("Assets/Blob-3.png")
blob4_foto = import_foto("Assets/Blob-4.png")
blob5_foto = import_foto("Assets/Blob-5.png")

geest_neutraal_rauw = pg.image.load("Assets/geest_neutraal.png")
geest_neutraal_foto = pg.transform.scale(geest_neutraal_rauw,(50,50))

geest_boos_rauw = pg.image.load("Assets/geest_boos.png")
geest_boos_foto = pg.transform.scale(geest_boos_rauw,(50,50))

geest_dood_rauw = pg.image.load("Assets/geest_dood.png")
geest_dood_foto = pg.transform.scale(geest_dood_rauw,(50,50))

boss_foto = import_foto("Assets/Boss.png",128,128)


####################
#Importeren - Audio#
####################

Nimbus = pg.mixer.Sound("Assets/ScreenNimbus.wav")

Boze_Geest = pg.mixer.Sound("Assets/BozeGeest.wav")

Coin = pg.mixer.Sound("Assets/coin.wav")

Versnel_geluid = pg.mixer.Sound("Assets/Versnelling_Geluid.wav")

Hartje_geluid = pg.mixer.Sound("Assets/Boop.wav")

Kogel_geluid = pg.mixer.Sound("Assets/Boop.wav")

Schild_geluid = pg.mixer.Sound("Assets/Swoosh.wav")

Game_Over = pg.mixer.Sound("Assets/GameOver.wav")

Level_Up = pg.mixer.Sound("Assets/LevelUp.wav")

Click_Geluid = pg.mixer.Sound("Assets/Click.wav")

Kogel_Schiet_Geluid = pg.mixer.Sound("Assets/Boom.wav")

ost1 = pg.mixer.Sound("Assets/Chicken.wav")

ost2 = pg.mixer.Sound("Assets/Wonderful-Life.wav")

ost3 = pg.mixer.Sound("Assets/BitFun.wav")

ost4 = pg.mixer.Sound("Assets/BitPower.wav")

ost5 = pg.mixer.Sound("Assets/BitSummer.wav")

channel_sound = pg.mixer.Channel(1)
channel_sound.set_volume(0.1)

#############
#Achtergrond#
#############

def achtergrond(scherm):
    scherm.fill((50,50,50))

########
#Volume#
########

def set_volume(volume):
    if volume:
        channel_sound.set_volume(0.1)
    else:
        channel_sound.set_volume(0.0)
############
#Get Colour#
############

def get_color(level):
    if level == 21:#boss
        kleur = (222, 61, 24)
    elif level < 11: #pyramid
        kleur = (248, 243, 61)
    elif level < 16: #jungle
        kleur = (24, 163, 33)
    elif level < 21: #underwater
        kleur = (32, 113, 245)
    return kleur
        
#######
#Menus#
#######

def tekenknop(scherm,radius,knopy,text,textx,texty,knopx=530):
    pg.draw.rect(scherm,(122,122,122),((knopx,knopy),(140,60)))
    pg.draw.rect(scherm,(50,50,50),((knopx,knopy),(radius,radius)))
    pg.draw.circle(scherm,(122,122,122),(knopx+radius,knopy+radius),radius)
    pg.draw.rect(scherm,(50,50,50),((knopx+140-radius,knopy),(radius,radius)))
    pg.draw.circle(scherm,(122,122,122),(knopx+140-radius,knopy+radius),radius)
    pg.draw.rect(scherm,(50,50,50),((knopx,knopy+60-radius),(radius,radius)))
    pg.draw.circle(scherm,(122,122,122),(knopx+radius,knopy+60-radius),radius)
    pg.draw.rect(scherm,(50,50,50),((knopx+140-radius,knopy+60-radius),(radius,radius)))
    pg.draw.circle(scherm,(122,122,122),(knopx+140-radius,knopy+60-radius),radius)

    menu_text = text
    if knopx == 530:#normale knop
        font_text = menufont.render(menu_text,True,(0,0,0))
    else:#setting knop
        font_text = settings_font.render(menu_text,True,(0,0,0))
    scherm.blit(font_text,(textx,texty))
    
def menu(scherm,level_nummer,geselecteerd_level,scrollx,particles,showtime,autoplay,volume):
    achtergrond(scherm)
    #knoppen voor menu:
    radius = 10
    tekenknop(scherm,radius,375,'Play',560,385)
    tekenknop(scherm,radius,475,'Help',560,485)
    tekenknop(scherm,radius,575,'Exit',560,585)

    titel_text = 'Swipe!'
    font_titel = titelfont.render(titel_text,True,(248,243,61))
    scherm.blit(font_titel,(490,0))
    #settings:
    if particles:
        particles = 'on'
    else:
        particles = 'off'
    if showtime:
        showtime = 'on'
    else:
        showtime = 'off'
    if autoplay:
        autoplay = 'on'
    else:
        autoplay = 'off'
    if volume:
        volume = 'on'
    else:
        volume = 'off'
        
    tekst(scherm,'Settings:',220,380,'tekst_groot')
    tekenknop(scherm,radius,445,'Particles: ' + particles,115,460,100)
    tekenknop(scherm,radius,445,'Show time: ' + showtime,290,460,280)
    tekenknop(scherm,radius,545,'Autoplay: ' + autoplay,115,560,100)
    tekenknop(scherm,radius,545,'Volume: ' + volume,295,560,280)
    #level selecteren:
    teller = 0
    for x in range(15):
        if x%2 == 0:
            ystart = 0
            yeind = 2
            ystap = 1
        else:
            ystart = 1
            yeind = -1
            ystap = -1
        for y in range(ystart,yeind,ystap):
            teller += 1
            if teller == geselecteerd_level:
                pg.draw.rect(scherm,(122,0,200),((x*125+95+scrollx,y*125+155),(75,75)))
            if teller == 21: #boss level
                pg.draw.rect(scherm,(222, 61, 24),((x*125+100+scrollx,y*125+160),(65,65)))
            elif teller < 11: #pyramid levels
                pg.draw.rect(scherm,(248,243,61),((x*125+100+scrollx,y*125+160),(65,65)))
            elif teller < 16: #jungle levels
                pg.draw.rect(scherm,(24, 163, 33),((x*125+100+scrollx,y*125+160),(65,65)))
            elif teller < 21: #underwater levels
                pg.draw.rect(scherm,(32, 113, 245),((x*125+100+scrollx,y*125+160),(65,65)))
            
            scherm.blit(menufont.render(str(teller),True,(0,0,0)),(x*125+120+scrollx-10*(len(str(teller))-1),y*125+165))
            
            if (x+1)%2 == y and teller < level_nummer:
                pg.draw.line(scherm,(248,243,61),(x*125+100+65+scrollx,y*125+160+int(65/2)),(x*125+100+65+60+scrollx,y*125+160+int(65/2)),5)
            if (y == 1 and teller < level_nummer) or (y == 1 and teller == level_nummer and x%2 == 0):
                pg.draw.line(scherm,(248,243,61),(x*125+130+scrollx,y*125+100),(x*125+130+scrollx,y*125+160),5)
            if teller == level_nummer:
                break
        if teller == level_nummer:
            break
        
def tekst(scherm, tekst, x, y, type_tekst):
    if type_tekst == 'tekst':
        font_tekst = tekstfont.render(tekst,True,(0,0,0))
    elif type_tekst == 'titel':
        font_tekst = titelfont.render(tekst,True,(248,243,61))
    elif type_tekst == 'tekst_groot':
        font_tekst = tekst_groot_font.render(tekst,True,(248,243,61))
    else:
        font_tekst = menufont.render(tekst,True,(248,243,61))
    scherm.blit(font_tekst,(x,y))
    
def help_menu(scherm):
    pg.draw.rect(scherm,(140,140,140),((50,50),(1100,550)))
    pg.draw.rect(scherm,(122,122,122),((530,475),(140,60)))
    #knop Ok!
    radius = 10
    pg.draw.rect(scherm,(140,140,140),((530,475),(radius,radius)))
    pg.draw.circle(scherm,(122,122,122),(530+radius,475+radius),radius)
    pg.draw.rect(scherm,(140,140,140),((530+140-radius,475),(radius,radius)))
    pg.draw.circle(scherm,(122,122,122),(530+140-radius,475+radius),radius)
    pg.draw.rect(scherm,(140,140,140),((530,475+60-radius),(radius,radius)))
    pg.draw.circle(scherm,(122,122,122),(530+radius,475+60-radius),radius)
    pg.draw.rect(scherm,(140,140,140),((530+140-radius,475+60-radius),(radius,radius)))
    pg.draw.circle(scherm,(122,122,122),(530+140-radius,475+60-radius),radius)
    help_text = 'Ok!'
    font_help = menufont.render(help_text,True,(0,0,0))
    scherm.blit(font_help,(560,485))
    tekst(scherm,'Welcome to Swipe!', 460,90,'titel_klein')
    tekst(scherm,'Instructions:',550,140,'tekst_groot')
    tekst(scherm,'Move with arrow keys and puzzle your way to the end of the level. Also make sure to grab these power-ups:',270,170,'tekst')
    tekst(scherm,'Coin (Increases score with 1), Coin Doubler (Doubles coins for next 15 seconds), Heart (increases health by 1),',237,190,'tekst')
    tekst(scherm,'Shield (immune for 7 seconds), Speed (Double speed woosh...), Bullet (collect these, shoot them with spacebar. Use it to shoot ghosts or the boss)',140,210,'tekst')
    foto_lijst = [munt_foto,muntx2_foto,hartje_foto,schild_foto,versnelling_foto,kogel_foto]
    for keer in range(len(foto_lijst)):
        scherm.blit(foto_lijst[keer],((keer*70)+400,240))
    tekst(scherm,'Avoid these spikes! If you touch one, you lose a life (the rectangle spikes have a suprise when touching them). Beware of ghosts! ',200,300,'tekst')
    foto_lijst = [stekels_foto, stekels2_foto, stekels3_foto,geest_boos_foto,plant1_foto,whirl5_foto]
    for keer in range(len(foto_lijst)):
        scherm.blit(foto_lijst[keer],(keer*70+400,340))
    tekst(scherm,'Keep your bullets, you will need them for the end fight in level 21. The boss summons ghosts, so avoid them too!',220,400,'tekst')
    tekst(scherm,'Oh and, if you have no lives left, you will lose a bit of progress...',420,420,'tekst')
    tekst(scherm,'Music by: HealthyBros, see his YouTube channel too! Art is by me. Menu music and Chicken theme is in the YouTube video library.',220,440,'tekst')
    
def gebruiker_input_menu(event_rij, menu_aan, spelen, geselecteerd_level, level, maximum_level, menu_help, schermblit, schermheightx, schermheighty, scrollx, showtime, particles,autoplay,volume):
    muis_x,muis_y = pg.mouse.get_pos()
    muis_x = (muis_x)*(1200/schermheightx)-scrollx
    muis_y = muis_y*(650/schermheighty)
    for e in event_rij:
        if e.type == pg.QUIT:
            spelen = False
        if e.type == pg.VIDEORESIZE:
            schermblit = pg.display.set_mode(e.size,pg.RESIZABLE|pg.DOUBLEBUF|pg.SCALED, vsync=1)
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                pg.event.pump()
                spelen = False
                
                    
        #scroll movement
        if e.type == pg.MOUSEMOTION:
            muis_x,muis_y = pg.mouse.get_pos()
            muis_x = (muis_x)*(1200/schermheightx)
            if muis_x < 100:
                if scrollx < -1:
                    scrollx += 3
                    
            if muis_x > 1100:
                if scrollx > -235:
                    scrollx -= 3
                
            muis_x,muis_y = pg.mouse.get_pos()
            muis_x = (muis_x)*(1200/schermheightx)-scrollx
            muis_y = muis_y*(650/schermheighty)

        #knoppen
        if e.type == pg.MOUSEBUTTONDOWN:
            muis_x,muis_y = pg.mouse.get_pos()
            muis_x = (muis_x)*(1200/schermheightx)
            muis_y = muis_y*(650/schermheighty)#menu
            if muis_y > 375 and muis_y < 435 and muis_x > 1200/2-70 and muis_x < 1200/2+70:
                level = 1
                menu_aan = False
            elif muis_y > 475 and muis_y < 535 and muis_x > 1200/2-70 and muis_x < 1200/2+70:
                if menu_help:
                    menu_help = False
                else:
                    menu_help = True
            elif muis_y > 575 and muis_y < 635 and muis_x > 1200/2-70 and muis_x < 1200/2+70:
                spelen = False

            elif muis_y > 445 and muis_y < 445+60 and muis_x > 100 and muis_x < 100+140:#settings
                if particles:
                    particles = False
                else:
                    particles = True
            
            elif muis_y > 445 and muis_y < 445+60 and muis_x > 280 and muis_x < 280+140:
                if showtime:
                    showtime = False
                else:
                    showtime = True
            
            elif muis_y > 545 and muis_y < 545+60 and muis_x > 100 and muis_x < 100+140:
                if autoplay:
                    autoplay = False
                else:
                    autoplay = True

            elif muis_y > 545 and muis_y < 545+60 and muis_x > 280 and muis_x < 280+140:
                if volume:
                    volume = False
                else:
                    volume = True
            
            else:#levels
                muis_x,muis_y = pg.mouse.get_pos()
                muis_x = (muis_x)*(1200/schermheightx)-scrollx
                muis_y = muis_y*(650/schermheighty)
                for level_nummer in range(maximum_level):
                    x = int(level_nummer/2)
                    y = (abs(3/2-level_nummer%4)+0.5)%2
                    if muis_x > x*125+100 and muis_x < x*125+100 + 65:
                        if muis_y > y*125+160 and muis_y < y*125+160 + 65:
                            geselecteerd_level = level_nummer + 1
                            channel_sound.play(Click_Geluid)
                            break
                        
    muis_type = normaal_cursor
    
    muis_x,muis_y = pg.mouse.get_pos()
    muis_x = (muis_x)*(1200/schermheightx)
    muis_y = muis_y*(650/schermheighty)
    if ((muis_y > 375) and muis_y < 435 or (muis_y > 475 and muis_y < 535) or (muis_y > 575 and muis_y < 635)) and (muis_x > 1200/2-70 and muis_x < 1200/2+70):
        muis_type = klik_cursor

    muis_x,muis_y = pg.mouse.get_pos()
    muis_x = (muis_x)*(1200/schermheightx)-scrollx
    muis_y = muis_y*(650/schermheighty)
    for level_nummer in range(maximum_level):
        x = int(level_nummer/2)
        y = (abs(3/2-level_nummer%4)+0.5)%2
        if muis_x > x*125+100 and muis_x < x*125+100 + 65:
            if muis_y > y*125+160 and muis_y < y*125+160 + 65:
                muis_type = klik_cursor
                            
    return menu_aan, spelen, geselecteerd_level, maximum_level, muis_type, menu_help,scrollx,showtime,particles,autoplay,volume

###############
#Scorebord Def#
###############

def score_maken(scherm,score):
    scherm.blit(munt_cut_foto,(10,45))
    score_font = menufont_klein.render(str(score),True,(248,243,61))
    scherm.blit(score_font,(45,40))

def levens_maken(scherm,levens):
    if levens < 6:
        for keer in range(levens):
            scherm.blit(hartje_klein_foto,(((keer+1)*32)-20,10))
    else:
        for keer in range(5):
            scherm.blit(hartje_klein_foto,(((keer+1)*32)-20,10))
        levens_font = menufont_klein.render('+ ' + str(levens-5),True,(248,243,61))
        scherm.blit(levens_font,(180,5))
        
    #levens_font = menufont_klein.render('Lives: '+str(levens),True,(248,243,61))
    #scherm.blit(levens_font,(20,20))

def kogels_maken(scherm,kogel):
    if kogel < 26:
        for keer in range(kogel):
            scherm.blit(kogel_middel_foto,(1190-((keer+1)*20),10))
    else:
        for keer in range(25):
            scherm.blit(kogel_middel_foto,(1190-((keer+1)*20),10))
        kogels_font = menufont_klein.render('+ ' + str(kogel-25),True,(248,243,61))
        scherm.blit(kogels_font,(1130 - (len(str(kogel-25)) * 20),35))
        
#####################
#Input gebruiker Def#
#####################

def gebruiker_input(event_rij, richting, schermblit, showtime, bounce_point):
    # geeft terug: (menu_aan, richting, restart, kogels_afvuren,show time, bouncepoint?)
    menu_aan = False
    restart = False
    schieten = False
    for e in event_rij:
        if e.type == pg.QUIT:
            menu_aan = True
        if e.type == pg.VIDEORESIZE:
            schermblit = pg.display.set_mode(e.size,pg.RESIZABLE|pg.DOUBLEBUF|pg.SCALED, vsync=1)
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                pg.event.pump()
                menu_aan = True
            if e.key == pg.K_r:
                pg.event.pump()
                restart = True
            if e.key == pg.K_t:
                pg.event.pump()
                if showtime:
                    showtime = False
                else:
                    showtime = True
            if richting == 'stilstand' or bounce_point:
                if e.key == pg.K_LEFT or e.key == pg.K_a:
                    pg.event.pump()
                    richting = 'links'
                if e.key == pg.K_RIGHT or e.key == pg.K_d:
                    pg.event.pump()
                    richting = 'rechts'
                if e.key == pg.K_UP or e.key == pg.K_w:
                    pg.event.pump()
                    richting = 'omhoog'
                if e.key == pg.K_DOWN or e.key == pg.K_s:
                    pg.event.pump()
                    richting = 'omlaag'
            if e.key == pg.K_SPACE or e.key == pg.K_q:
                pg.event.pump()
                schieten = True
 
    pg.event.pump()
    return menu_aan, richting, restart ,schieten,showtime

##############
#Class Blokje#
##############
        
class blokje:
    def __init__(self):
        self.levens = 3
        self.x = 500
        self.y = 300
        self.vx = 1
        self.vy = 1
        self.breedte = 50
        self.oog_breedte = 5
        self.richting = 'stilstand'
        self.laatste_richting = 'stilstand'
        self.gebotst = False
        self.score = 0
        self.schild = False
        self.start_schild = -1000
        self.dubbel = False
        self.start_dubbel = -1000
        self.kogel = 0
        self.kogel_tijd = -1
        self.checkx = 500
        self.checky = 300
        self.bounce_snelheid = False
        self.boss_snelheid = False
        
    def reset(self):
        self.x = 500
        self.y = 300
        self.checkx = 500
        self.checky = 300
        self.breedte = 50
        self.oog_breedte = 5
        self.richting = 'stilstand'
        self.laatste_richting = 'stilstand'
        self.gebotst = False
        self.schild = False
        self.start_schild = -1000
        self.dubbel = False
        self.start_dubbel = -1000
        self.kogel_tijd = -1
        self.bounce_snelheid = False

    def dood(self,knop_muur_lijst,geest_lijst,boss_lijst,whirl_lijst):
        channel_sound.play(Game_Over)
        self.levens -= 1
        self.x = self.checkx
        self.y = self.checky
        self.richting = 'stilstand'
        self.laatste_richting = 'stilstand'
        self.gebotst = False
        self.bounce_snelheid = False
        
        for Knop_Muur in knop_muur_lijst:
            Knop_Muur.ingedrukt = False
            Knop_Muur.uit = False
            Knop_Muur.waarschuwing_tijd = 1e8
            Knop_Muur.start_ingedrukt = 0
            
        for Boss in boss_lijst:
            Boss.x = Boss.start_x
            Boss.y = Boss.start_y
            Boss.starttijd = t.perf_counter()
    
        for Geest in geest_lijst:
            Geest.x = Geest.start_x
            Geest.y = Geest.start_y
            Geest.richting = 'stilstand'
            Geest.emotie = 'neutraal'
            Geest.wakker = False
            Geest.starttijd = 1e9

        for Whirl in whirl_lijst:
            Whirl.breedte = 50
            Whirl.dood = False
            Whirl.x = Whirl.start_x
            Whirl.y = Whirl.start_y
            Whirl.genereer_foto()
    
    def af(self,scherm,schermblit):
        self.x = self.checkx
        self.y = self.checky
        af_font = titelfont.render('Game Over!',True,(255,0,0))
        scherm.blit(af_font,(400,250))
        schermblit.blit(pg.transform.scale(scherm, schermblit.get_rect().size).convert(), (0, 0))
        pg.display.flip()
        self.score = 0
        
    def beweeg(self,deltaTime):
        if not (self.bounce_snelheid or self.boss_snelheid):
            if self.richting == 'omhoog':
                self.y -= (self.vy/1.9) * deltaTime
            elif self.richting == 'omlaag':
                self.y += (self.vy/1.9) * deltaTime
            elif self.richting == 'rechts':
                self.x += (self.vx/1.9) * deltaTime
            elif self.richting == 'links': 
                self.x -= (self.vx/1.9) * deltaTime
        else:
            if self.bounce_snelheid:
                if self.richting == 'omhoog':
                    self.y -= (0.7/1.9) * deltaTime
                elif self.richting == 'omlaag':
                    self.y += (0.7/1.9) * deltaTime
                elif self.richting == 'rechts':
                    self.x += (0.7/1.9) * deltaTime
                elif self.richting == 'links': 
                    self.x -= (0.7/1.9) * deltaTime
                    
            if self.boss_snelheid:
                if self.richting == 'omhoog':
                    self.y -= (1/1.9) * deltaTime
                elif self.richting == 'omlaag':
                    self.y += (1/1.9) * deltaTime
                elif self.richting == 'rechts':
                    self.x += (1/1.9) * deltaTime
                elif self.richting == 'links': 
                    self.x -= (1/1.9) * deltaTime
            
            # anders: staat hij stil
    
    def input(self, richting):
        if self.richting != 'stilstand' and self.richting != richting:
            self.laatste_richting = self.richting
        self.richting = richting
            
            
    def teken(self,scherm,level):
        #if level == 10:
            #if t.perf_counter() > self.kogel_tijd + 3:
                #self.kogel += 1
            
        if self.schild and (t.perf_counter() - self.start_schild < 3.5 or int(2*(t.perf_counter() - self.start_schild))%2 == 1):
            kleur = (66, 135, 245)
        elif self.dubbel and (t.perf_counter() - self.start_dubbel < 7 or int (2*(t.perf_counter() - self.start_dubbel))%2 == 1):
            kleur = (116, 120, 10)
        elif level == 21:
            kleur = (194, 60, 33)
        else:
            kleur = (237, 145, 24)
        pg.draw.rect(scherm, (50, 50, 50), ((int(self.x), int(self.y)), (self.breedte, self.breedte)))
        pg.draw.rect(scherm, kleur, ((int(self.x), int(self.y)), (self.breedte, self.breedte)), 2)
        pg.draw.rect(scherm, kleur, ((int(self.x)+10, int(self.y)+10), (self.oog_breedte, self.oog_breedte)))
        pg.draw.rect(scherm, kleur, ((int(self.x)+40-self.oog_breedte, int(self.y)+10), (self.oog_breedte, self.oog_breedte)))

    def check_muur(self, muur_lijst):
        particleX = -5
        particleY = -5
        particleR = 'verticaal'
        
        #if self.gebotst:
        #    if self.richting == 'stilstand' or self.richting == self.laatste_richting:
        #        self.richting = 'stilstand'
        #    else:
        #        self.gebotst = False

        #huidige pos  
        for Muur in muur_lijst:
            if Muur.x < self.x + self.breedte and Muur.x + Muur.breedte > self.x:
                if Muur.y < self.y + self.breedte and Muur.y + Muur.lengte > self.y:
                    self.gebotst = True
                    if self.richting == 'rechts':
                        self.x = Muur.x - self.breedte
                        
                        particleX = self.x + self.breedte
                        particleY = self.y + self.breedte/2
                        particleR = 'verticaal'
                        
                    elif self.richting == 'links':
                        self.x = Muur.x + Muur.breedte
                        
                        particleX = self.x
                        particleY = self.y + self.breedte/2
                        particleR = 'verticaal'
                        
                    elif self.richting == 'omhoog':
                        self.y = Muur.y + Muur.lengte
                        
                        particleX = self.x + self.breedte/2
                        particleY = self.y
                        particleR = 'horizontaal'
                        
                    elif self.richting == 'omlaag':
                        self.y = Muur.y - self.breedte
                        
                        particleX = self.x + self.breedte/2
                        particleY = self.y + self.breedte
                        particleR = 'horizontaal'

                    self.laatste_richting = self.richting
                    self.richting = 'stilstand'
        
        return particleX, particleY, particleR
           
    def check_finish(self, Finish, level):
        if self.x < Finish.x+10 and self.x > Finish.x-10 and self.y < Finish.y+10 and self.y > Finish.y-10:
            channel_sound.play(Level_Up)
            return level + 1, True
        return level, False

    def check_checkpoint(self, Checkpoint):
        if self.x < Checkpoint.x+10 and self.x > Checkpoint.x-10 and self.y < Checkpoint.y+10 and self.y > Checkpoint.y-10 and (self.checkx != Checkpoint.x or self.checky != Checkpoint.y):
            channel_sound.play(Level_Up)
            self.checkx = Checkpoint.x
            self.checky = Checkpoint.y
            return True
        return False

    def check_stekel(self, stekel_lijst, knop_muur_lijst):
        for Stekel in stekel_lijst:
            if self.x < Stekel.x + Stekel.breedte and self.x + self.breedte > Stekel.x:
                if self.y < Stekel.y + Stekel.hoogte and self.y + self.breedte > Stekel.y and self.schild == False:
                    return True
        return False

    def check_stekel2(self, stekel2_lijst, knop_muur_lijst):
        self.check_muur(stekel2_lijst)
        for Stekel in stekel2_lijst:
            if self.x < Stekel.stekel_x + Stekel.breedte and self.x + self.breedte > Stekel.stekel_x:
                if self.y < Stekel.stekel_y + Stekel.hoogte and self.y + self.breedte > Stekel.stekel_y and self.schild == False:
                    return True
        return False

    def check_powerup(self,powerup_lijst):
        for powerup in powerup_lijst:
            if not powerup.gepakt:
                if self.x < powerup.x + powerup.hoogte and self.x + self.breedte > powerup.x:
                    if self.y < powerup.y + powerup.hoogte and self.y + self.breedte > powerup.y:
                        powerup.gepakt = True
                        if powerup.pu_type == 'Munt':
                            channel_sound.play(Coin)
                            if self.dubbel:
                                punten = 2
                            else:
                                punten = 1
                            self.score += punten
                        elif powerup.pu_type == 'Hartje':
                            channel_sound.play(Hartje_geluid)
                            self.levens += 1
                        elif powerup.pu_type == 'Versnelling':
                            channel_sound.play(Versnel_geluid)
                            self.vx += 0.5
                            self.vy += 0.5
                            if self.vx > 2:
                                self.vx = 2
                                self.vy = 2
                        elif powerup.pu_type == 'Schild':
                            channel_sound.play(Schild_geluid)
                            self.schild = True
                            self.start_schild = t.perf_counter()
                        elif powerup.pu_type == 'Muntx2':
                            self.dubbel = True
                            self.start_dubbel = t.perf_counter()
                        elif powerup.pu_type == 'Kogel':
                            channel_sound.play(Kogel_geluid)
                            self.kogel += 1
                        return True
        return False
                            

    def check_schild_en_x2(self):
        if self.schild:
            if t.perf_counter() >= self.start_schild + 7:
                self.schild = False
                
        if self.dubbel:
            if t.perf_counter() >= self.start_dubbel + 15:
                self.dubbel = False
                
    def check_geest(self, geest_lijst, knop_muur_lijst):
        for Geest in geest_lijst:
            if self.x < Geest.x + Geest.hoogte and self.x + self.breedte > Geest.x:
                if self.y < Geest.y + Geest.hoogte and self.y + self.breedte > Geest.y and self.schild == False:
                    if Geest.emotie == 'boos':
                        return True
        return False

    def check_whirl(self, whirl_lijst):
        for Whirl in whirl_lijst:
            if self.x < Whirl.x + Whirl.breedte and self.x + self.breedte > Whirl.x:
                if self.y < Whirl.y + Whirl.breedte and self.y + self.breedte > Whirl.y and self.schild == False and Whirl.dood == False:
                    return True
        return False

    def check_bounce_point(self,bounce_point_lijst):
        for Bounce_point in bounce_point_lijst:
            if self.x < Bounce_point.x + Bounce_point.breedte + 25 and self.x + self.breedte > Bounce_point.x - 25:
                if self.y < Bounce_point.y + Bounce_point.breedte + 25 and self.y + self.breedte > Bounce_point.y - 25 and Bounce_point.actief == True:
                    self.bounce_snelheid = True
                    self.laatste_richting = 'stilstand'
                    self.bounce_af_teller = t.perf_counter()
                    return True
        
        self.bounce_snelheid = False
        return False
            
        
############
#Class Muur#
############
        
class muur:
    def __init__(self,x,y,lengte,orientatie,dikte=5):
        self.x = x
        self.y = y
        self.orientatie = orientatie
        self.real_lengte = lengte
        self.real_breedte = dikte
        if orientatie == 'staand':
            self.lengte = lengte
            self.breedte = dikte
        else: # liggend
            self.lengte = dikte
            self.breedte = lengte
        self.kleur = (0, 0, 0)

    def teken(self, scherm, level):
        pg.draw.rect(scherm, get_color(level), ((self.x,self.y),(self.breedte, self.lengte)))

    def get_code(self,last):
        if last:
            if self.real_breedte == 5:
                return "muur("+str(self.x)+","+str(self.y)+","+str(self.real_lengte)+",'"+str(self.orientatie)+"')"
            else:
                return "muur("+str(self.x)+","+str(self.y)+","+str(self.real_lengte)+",'"+str(self.orientatie)+"',"+str(self.real_breedte)+")"
        else:
            if self.real_breedte == 5:
                return "muur("+str(self.x)+","+str(self.y)+","+str(self.real_lengte)+",'"+str(self.orientatie)+"'),"
            else:
                return "muur("+str(self.x)+","+str(self.y)+","+str(self.real_lengte)+",'"+str(self.orientatie)+"',"+str(self.real_breedte)+"),"

####################
#Class bounce_point#
####################

class bounce_point:
    def __init__(self,x,y,breedte=50):
        self.x = x
        self.y = y
        self.breedte = breedte
        self.actief = True
        self.animate_timer = -1
        self.animatie = 1

    def teken(self,scherm,Blokje):
        if t.perf_counter() > self.animate_timer + 0.15:
            self.animatie += 1
            self.animate_timer = t.perf_counter()
            
        if Blokje.x < self.x + self.breedte + 25 and Blokje.x + Blokje.breedte > self.x - 25 and Blokje.y < self.y + self.breedte + 25 and Blokje.y + Blokje.breedte > self.y - 25:
                scherm.blit(blob5_foto,(self.x,self.y))
        else:
            if self.animatie > 4:
                if self.animatie == 5:
                    scherm.blit(blob3_foto,(self.x,self.y))
                elif self.animatie > 5:
                    scherm.blit(blob2_foto,(self.x,self.y))
                    self.animatie = 1
            else:
                scherm.blit(eval("blob"+str(self.animatie)+"_foto"),(self.x,self.y))#blob1_foto

    def get_code(self,last):
        if last:
            return "bounce_point("+str(self.x)+","+str(self.y)+")"
        else:
            return "bounce_point("+str(self.x)+","+str(self.y)+"),"
            
#################
#Class Knop_Muur#
#################

class knop_muur(muur):
    def __init__(self,x,y,knop_x,knop_y,lengte,orientatie,dikte=5):
        super().__init__(x,y,lengte,orientatie,dikte)
        self.knop_x = knop_x
        self.knop_y = knop_y
        self.ingedrukt = False
        self.waarschuwing_tijd = 1e8
        self.uit = False
        self.knop_breedte = 10
        self.knop_lengte = 10
        self.start_ingedrukt = 0
        self.real_lengte = lengte
        
    def teken(self, scherm, level):
        if self.ingedrukt and self.uit == False:
            if self.waarschuwing_tijd == 1e8:
                self.waarschuwing_tijd = t.perf_counter()
            pg.draw.rect(scherm, (222, 61, 24), ((self.x,self.y),(self.breedte, self.lengte)))
        elif self.ingedrukt == False and self.uit == False:
            pg.draw.rect(scherm, get_color(level), ((self.x,self.y),(self.breedte, self.lengte)))
            pg.draw.rect(scherm, (255,0,0), ((self.knop_x, self.knop_y),(self.knop_breedte, self.knop_lengte)))
            
        if t.perf_counter() - self.waarschuwing_tijd > 1:
            self.uit = True

        if self.start_ingedrukt > 0:
            self.start_ingedrukt += 1
        if self.start_ingedrukt > 9:
            self.ingedrukt = True
     
    def detecteer_blokje(self,Blokje,detect):
        if self.knop_x < Blokje.x + Blokje.breedte and self.knop_x + self.knop_breedte > Blokje.x:
            if self.knop_y < Blokje.y + Blokje.breedte and self.knop_y + self.knop_breedte > Blokje.y:
                if detect:
                    self.start_ingedrukt += 1
                return True, self.x, self.y, self.orientatie
            
        return False, 0, 0, self.orientatie

    def get_code(self,last):
        if last:
            return "knop_muur("+str(self.x)+","+str(self.y)+","+str(self.knop_x)+","+str(self.knop_y)+","+str(self.real_lengte)+",'"+str(self.orientatie)+"')"
        else:
            return "knop_muur("+str(self.x)+","+str(self.y)+","+str(self.knop_x)+","+str(self.knop_y)+","+str(self.real_lengte)+",'"+str(self.orientatie)+"'),"
    
        
#################
#Genereer Stuffs#
#################

def loop_obj(posx,posy,lijst,knop = False):
    index_var = 0
    for Obj in lijst:
        if not knop:
            if Obj.x == posx and Obj.y == posy:
                return index_var
        else:
            try:
                if Obj.knop_x == posx and Obj.knop_y == posy:
                    return index_var
            except:
                pass
        index_var += 1
    return None

def check_object(x,y,muur_lijst,stekel_lijst,stekel2_lijst,stekel3_lijst,powerup_lijst,geest_lijst,plant_lijst,whirl_lijst,bewegende_muren_lijst,knop_muur_lijst,decoratie_lijst,bounce_point_lijst):
    returnval = loop_obj(x,y,muur_lijst)
    if returnval != None:
        return returnval, 'muur'
    returnval = loop_obj(x,y,stekel_lijst)
    if returnval != None:
        return returnval, 'stekel'
    returnval = loop_obj(x,y,stekel2_lijst)
    if returnval != None:
        return returnval, 'stekel2'
    returnval = loop_obj(x,y,stekel3_lijst)
    if returnval != None:
        return returnval, 'stekel3'
    returnval = loop_obj(x,y,powerup_lijst)
    if returnval != None:
        return returnval, 'powerup'
    returnval = loop_obj(x,y,geest_lijst)
    if returnval != None:
        return returnval, 'geest'
    returnval = loop_obj(x,y,plant_lijst)
    if returnval != None:
        return returnval, 'plant'
    returnval = loop_obj(x,y,whirl_lijst)
    if returnval != None:
        return returnval, 'whirl'
    returnval = loop_obj(x,y,bewegende_muren_lijst)
    if returnval != None:
        return returnval, 'bewegende muur'
    returnval = loop_obj(x,y,knop_muur_lijst,True)
    if returnval != None:
        return returnval, 'knop muur'
    returnval = loop_obj(x,y,decoratie_lijst,True)
    if returnval != None:
        return returnval, 'decoratie'
    returnval = loop_obj(x,y,bounce_point_lijst,True)
    if returnval != None:
        return returnval, 'bounce point'
    return returnval, ''


    
def check_object_existance(obj_list,objtype,objx,objy,objrotation='links',objlen=55,objorientation='liggend'):
    for Obj_loop in obj_list:
        if Obj_loop.x == objx and Obj_loop.y == objy:
            if objtype == 'muur':
                if Obj_loop.orientatie == objorientation:
                    return True
                else:
                    return False
            if objtype in ['stekel','stekel2','stekel3','plant']:
                if Obj_loop.richting == objrotation:
                    return True
            else:
                return True
    return False

def check_object_existance_index(obj_list,objtype,objx,objy,objrotation='links',objlen=55,objorientation='liggend'):
    index_var = 0
    for Obj_loop in obj_list:
        if Obj_loop.x == objx and Obj_loop.y == objy:
            if objtype == 'muur':
                if Obj_loop.orientatie == objorientation:
                    return index_var
                else:
                    return False
            elif objtype in ['stekel','stekel2','stekel3','plant']:
                if Obj_loop.richting == objrotation:
                    return index_var
            else:
                return index_var
        index_var += 1
    return False
    
def genereer_object(objecttype,objectx,objecty,objectlen = 55, objectorientation = 'liggend',objectrotation = 'omhoog',powerup_type = 'Munt',brush_distance=200,brush_wall_x=250,brush_wall_y=250,brush_deco_type=1):
    if objecttype == 'muur':
        return muur(objectx,objecty,objectlen,objectorientation)
    elif objecttype == 'stekels':
        return stekel(objectx,objecty,objectrotation)
    elif objecttype == 'stekel2':
        return stekel2(objectx,objecty,objectrotation)
    elif objecttype == 'stekel3':
        return stekel3(objectx,objecty,objectrotation)
    elif objecttype == 'powerup':
        return Powerup(objectx,objecty,powerup_type)
    elif objecttype == 'geest':
        return geest(objectx,objecty,0)
    elif objecttype == 'whirl':
        return whirl(objectx,objecty,0)
    elif objecttype == 'plant':
        return plant(objectx,objecty,0,objectrotation)
    elif objecttype == 'bewegende muur': #self,startx,starty,eindx,eindy,lengte,orientatie,tijd=5,dikte=5
        if objectorientation == 'staand':
            return bewegende_muur(objectx,objecty,objectx,objecty+brush_distance,objectlen,objectorientation)
        if objectorientation == 'liggend':
            return bewegende_muur(objectx,objecty,objectx+brush_distance,objecty,objectlen,objectorientation)
    elif objecttype == 'knop muur': #self,x,y,knop_x,knop_y,lengte,orientatie,dikte=5
        if objectorientation == 'staand':
            return knop_muur(brush_wall_x,brush_wall_y,objectx,objecty,objectlen,objectorientation)
        if objectorientation == 'liggend':
            return knop_muur(brush_wall_x,brush_wall_y,objectx,objecty,objectlen,objectorientation)
    elif objecttype == 'decoratie':
        return decoratie(objectx,objecty,brush_deco_type)
    elif objecttype == 'bounce point':
        return bounce_point(objectx,objecty)

##############
#Input Editor#
##############

def genereer_level_muren(level_nummer):
    if level_nummer == 1:
        return [muur(400,350,200,'liggend'), muur(600,145,210,'staand'), muur(150,145,450,'liggend'), muur(200,200,350,'liggend'),
                muur(400,200,150,'staand'), muur(145,145,100,'staand'), muur(20,300,380,'liggend'), muur(20,245,130,'liggend'),
                muur(20,245,60,'staand')]
    elif level_nummer == 2:
        return [muur(435,350,170,'liggend'),muur(550,200,155,'staand'),muur(495,200,155,'staand'),muur(470,90,110,'staand'),muur(445,90,10,'staand'),
                muur(380,90,95,'liggend'),muur(380,90,110,'staand'),muur(355,200,200,'staand'),muur(380,400,80,'staand'),muur(380,475,105,'liggend'),
                muur(485,450,240,'liggend'),muur(720,350,105,'staand'),muur(695,120,230,'staand'),muur(555,120,145,'liggend'),muur(475,145,80,'liggend'),
                muur(645,210,50,'liggend')]
    elif level_nummer == 3:
        return [muur(495,300,55,'staand'),muur(495,350,55,'liggend'),muur(550,300,55,'staand'),muur(495,60,55,'liggend'),muur(495,60,55,'staand'),
                muur(820,60,55,'staand'),muur(770,600,50,'liggend'),muur(1120,550,50,'staand'),muur(1070,190,55,'liggend'),muur(230,195,155,'staand'),
                muur(230,295,55,'liggend'),muur(230,600,50,'liggend')]
    elif level_nummer == 4:
        return [muur(500,115,50,'liggend'),muur(330,120,50,'staand'),muur(335,500,55,'liggend'),muur(385,450,50,'staand'),muur(5,500,50,'liggend'),
                muur(50,500,100,'staand'),muur(550,550,75,'staand'),muur(500,600,55,'liggend'),muur(50,600,55,'liggend'),muur(1000,120,50,'staand'),
                muur(950,115,55,'liggend'),muur(950,500,50,'liggend'),muur(1000,450,55,'staand'),muur(650,450,125,'staand'),muur(650,445,55,'liggend'),
                muur(655,625,50,'liggend'),muur(1145,625,50,'liggend'),muur(405,0,55,'staand'),muur(1100,300,50,'staand'),muur(550,350,55,'liggend'),
                muur(550,350,55,'staand'),muur(800,405,55,'liggend'),muur(850,355,50,'staand')]
    elif level_nummer == 5:
        return [muur(495,300,55,'staand'),muur(495,350,55,'liggend'),muur(550,300,55,'staand'),muur(30,225,50,'staand')]
    elif level_nummer == 6:
        return [muur(495,300,55,'staand'),muur(495,350,55,'liggend'),muur(550,300,55,'staand'),muur(500,100,50,'liggend'),muur(550,100,55,'staand'),
                muur(100,100,55,'staand'),muur(100,100,55,'liggend'),muur(100,400,55,'staand'),muur(100,450,100,'liggend'),muur(645,325,50,'staand'),
                muur(645,320,55,'liggend')]
    elif level_nummer == 7:
        return [muur(500,350,55,'liggend'),muur(495,126,595-126,'staand'),muur(550,126-55,355-(126-55),'staand'),muur(0,126-55,550,'liggend'),
                muur(110,126,495-105,'liggend',25),muur(55,126,595-126,'staand'),muur(55,590,115,'liggend'),muur(55+110,201,394,'staand'),
                muur(110,201,394-55,'staand'),muur(110,201,55,'liggend'),muur(220,201,399+50,'staand'),muur(220,201,445-220,'liggend'),
                muur(445-25,201,394,'staand',25),muur(495,590,1200-110-495,'liggend'),muur(1200-115,250,595-250,'staand'),muur(1200-115-20,240,55+20,'liggend'),
                muur(1200-60,295,650-295,'staand'),muur(1200-60,55,245-55,'staand'),muur(850,55,290,'liggend'),muur(850,55,230-55,'staand'),
                muur(795,0,230,'staand'),muur(795,225,55,'liggend')]
    elif level_nummer == 8:
        return [muur(495,300,55,'staand'),muur(495,350,55,'liggend'),muur(550,300,55,'staand'),muur(500,50,50,'liggend'),muur(100,50,55,'liggend'),muur(100,50,55,'staand'),
                muur(100,450,55,'staand'),muur(100,500,55,'liggend'),muur(250,500,55,'liggend'),muur(300,450,55,'staand'),muur(245,150,55,'staand'),muur(245,150,55,'liggend'),
                muur(650,150,55,'liggend'),muur(700,150,55,'staand'),muur(645,450,55,'staand'),muur(645,500,55,'liggend'),muur(1000,500,55,'liggend'),muur(1050,450,55,'staand'),
                muur(995,50,55,'staand'),muur(1000,50,55,'liggend'),muur(1050,50,55,'staand'),muur(800,50,55,'liggend'),muur(850,50,55,'staand'),muur(775,400,80,'liggend'),
                muur(1150,50,55,'staand'),muur(1100,50,55,'liggend'),muur(1095,50,55,'staand'),muur(1100,400,55,'liggend'),muur(1150,350,55,'staand')]
    elif level_nummer == 9:
        return [muur(495,300,55,'staand'),muur(495,350,55,'liggend'),muur(550,300,55,'staand'),muur(95,95,55,'staand'),muur(95,95,55,'liggend'),muur(150,95,55,'staand'),
                muur(95,550,50,'staand'),muur(1000,30,55,'staand'),muur(1000,545,55,'staand')]
    elif level_nummer == 10:
        return [muur(495,300,105,'staand'),muur(495,350,55,'liggend'),muur(550,145,210,'staand'),muur(495,50,55,'liggend'),muur(140,50,55,'staand'),muur(195,50,55,'staand'),muur(495,570,60,'liggend'),
                muur(550,570-50,55,'staand'),muur(1140,405,55,'liggend')]
    elif level_nummer == 11:
        return [muur(550,295,55,'staand'),muur(495,295,55,'staand'),muur(495,295,55,'liggend'),muur(610,360,150,'staand'),muur(560,355,55,'liggend'),muur(560,510,55,'liggend'),muur(550,595,55,'staand'),muur(95,240,55,'staand'),muur(550,240,55,'staand'),muur(95,240,55,'liggend'),muur(550,295,55,'liggend'),muur(205,5,55,'staand'),muur(205,55,55,'liggend'),muur(615,380,50,'liggend'),muur(1140,595,50,'staand'),muur(550,590,55,'liggend')]
    elif level_nummer == 12:
        return [muur(495,295,55,'staand'),muur(500,295,55,'liggend'),muur(550,300,50,'staand'),muur(475,525,75,'liggend'),muur(550,550,550,'liggend'),muur(550,420,550,'liggend'),muur(1100,525,55,'liggend'),muur(1140,525,55,'liggend'),muur(1140,420,55,'staand'),muur(1090,420,55,'liggend'),muur(975,5,55,'staand'),muur(650,365,55,'staand'),muur(650,5,55,'staand'),muur(805,5,55,'staand'),muur(805,140,80,'staand'),muur(1080,150,50,'staand'),muur(360,195,55,'liggend'),muur(225,30,55,'staand'),muur(225,195,55,'liggend'),muur(355,150,50,'staand'),muur(480,595,50,'staand'),muur(55,140,55,'liggend'),muur(150,290,50,'staand')]
    elif level_nummer == 13:
        return [muur(550,295,55,'staand'),muur(30,5,175,'staand'),muur(85,5,175,'staand'),muur(645,530,115,'staand'),muur(555,350,90,'liggend'),muur(500,350,55,'liggend'),muur(475,350,25,'liggend'),muur(490,5,295,'staand'),muur(495,295,55,'liggend'),muur(645,230,125,'staand'),muur(850,350,50,'liggend'),muur(1160,350,55,'staand'),muur(435,605,40,'liggend'),muur(455,605,40,'staand')]
    elif level_nummer == 14:
        return [muur(495,295,55,'staand'),muur(495,295,55,'liggend'),muur(550,295,55,'staand'),muur(875,300,50,'liggend'),muur(925,595,50,'staand'),muur(495,595,50,'staand'),muur(925,300,55,'staand'),muur(555,295,25,'liggend'),muur(550,350,30,'liggend'),muur(495,350,5,'liggend'),muur(300,5,50,'staand'),muur(1145,55,50,'liggend'),muur(305,350,50,'liggend'),muur(55,5,50,'staand'),muur(495,520,50,'staand'),muur(445,570,55,'liggend'),muur(445,355,55,'liggend'),muur(360,295,135,'liggend'),muur(305,295,55,'liggend')]
    elif level_nummer == 15:
        return [muur(495,295,55,'staand'),muur(495,295,55,'liggend'),muur(550,295,55,'staand'),muur(550,5,290,'staand'),muur(550,350,245,'staand'),muur(605,55,590,'staand'),muur(605,55,535,'liggend'),muur(605,55,540,'liggend'),muur(605,55,540,'liggend'),muur(660,110,535,'liggend'),muur(610,165,535,'liggend'),muur(660,220,535,'liggend'),muur(610,275,535,'liggend'),muur(660,330,535,'liggend'),muur(610,385,535,'liggend'),muur(660,440,535,'liggend'),muur(610,495,535,'liggend'),muur(610,590,50,'liggend'),muur(1005,595,50,'staand'),muur(950,595,50,'staand'),muur(55,5,50,'staand'),muur(895,500,95,'staand'),muur(1060,500,95,'staand')]
    elif level_nummer == 16:
        return [muur(495,295,55,'staand'),muur(495,295,55,'liggend'),muur(495,590,55,'staand'),muur(440,295,55,'liggend'),muur(440,295,55,'staand'),muur(5,590,135,'liggend'),muur(550,295,95,'staand'),muur(340,350,105,'liggend'),muur(340,355,240,'staand'),muur(340,245,105,'staand'),muur(315,240,30,'liggend'),muur(5,595,50,'staand'),muur(340,5,100,'staand'),muur(135,5,100,'staand'),muur(340,105,160,'liggend'),muur(550,105,190,'staand'),muur(1095,105,100,'liggend'),muur(550,105,255,'liggend'),muur(550,390,30,'liggend'),muur(580,390,290,'liggend'),muur(865,300,90,'staand'),muur(805,190,300,'liggend'),muur(1105,190,110,'staand'),muur(800,190,110,'staand'),muur(1105,300,90,'liggend'),muur(575,395,250,'staand')]
    elif level_nummer == 17:
        return [muur(495,295,55,'staand'),muur(495,295,55,'liggend'),muur(550,295,55,'staand'),muur(440,5,290,'staand'),muur(865,5,55,'staand'),muur(385,350,295,'staand'),muur(385,345,110,'liggend'),muur(285,5,30,'staand'),muur(330,295,50,'staand'),muur(235,540,50,'liggend'),muur(285,490,55,'staand'),muur(230,490,55,'staand')]
    elif level_nummer == 18:
        return [muur(500,480,50,'liggend'),muur(5,480,25,'liggend'),muur(5,590,55,'liggend'),muur(1135,5,55,'staand'),muur(390,5,30,'staand'),muur(645,5,30,'staand'),muur(130,55,165,'staand'),muur(340,535,55,'liggend'),muur(390,485,55,'staand'),muur(5,80,55,'liggend'),muur(75,155,55,'liggend'),muur(5,220,55,'liggend'),muur(130,300,50,'staand'),muur(735,55,165,'staand'),muur(740,55,395,'liggend'),muur(685,220,55,'liggend'),muur(130,220,55,'liggend'),muur(790,225,55,'staand'),muur(740,275,55,'liggend'),muur(80,275,55,'liggend'),muur(1135,225,55,'staand'),muur(1085,275,55,'liggend'),muur(1135,60,50,'staand'),muur(760,425,85,'liggend'),muur(130,295,30,'liggend'),muur(130,350,30,'liggend'),muur(5,275,50,'liggend'),muur(55,275,55,'staand'),muur(5,425,50,'liggend'),muur(810,430,50,'staand')]
    elif level_nummer == 19:
        return [muur(495,295,55,'staand'),muur(495,295,55,'liggend'),muur(495,350,55,'liggend'),muur(1145,350,55,'liggend'),muur(490,5,55,'staand'),muur(545,245,55,'staand'),muur(550,275,55,'liggend'),muur(600,245,30,'staand'),muur(270,245,55,'staand'),muur(270,295,55,'liggend'),muur(5,300,55,'liggend'),muur(220,245,55,'liggend'),muur(740,90,55,'liggend'),muur(740,90,55,'staand'),muur(970,90,55,'liggend'),muur(1020,90,55,'staand'),muur(440,55,55,'liggend'),muur(795,595,50,'staand')]
    elif level_nummer == 20:
        return [muur(495,300,170,'staand'),muur(495,295,60,'liggend'),muur(550,295,175,'staand'),muur(550,465,60,'liggend'),muur(555,295,55,'liggend'),muur(605,350,65,'staand'),muur(605,350,55,'liggend'),muur(660,295,60,'staand'),muur(660,295,195,'liggend'),muur(850,245,55,'staand'),muur(795,190,55,'staand'),muur(795,190,110,'liggend'),muur(905,190,165,'staand'),muur(715,350,190,'liggend'),muur(660,355,55,'staand'),muur(850,350,55,'staand'),muur(795,405,55,'staand'),muur(660,405,135,'liggend'),muur(660,405,115,'staand'),muur(605,410,55,'liggend'),muur(605,240,195,'liggend'),muur(550,190,245,'liggend'),muur(550,195,100,'staand'),muur(905,350,175,'staand'),muur(440,470,55,'staand'),muur(440,415,55,'liggend'),muur(385,360,115,'liggend'),muur(385,415,55,'staand'),muur(330,520,525,'liggend'),muur(330,305,115,'liggend'),muur(330,305,220,'staand'),muur(330,190,220,'liggend'),muur(330,245,65,'staand'),muur(440,195,50,'staand'),muur(725,465,55,'staand'),muur(665,65,50,'staand'),muur(530,65,50,'staand')]
    elif level_nummer == 22:
        return []
    elif level_nummer == 21:
        return [muur(500,65,50,'liggend'),muur(60,65,55,'liggend'),muur(60,65,55,'staand'),muur(60,500,55,'staand'),muur(60,550,55,'liggend'),muur(450,550,50,'liggend'),
                muur(445,300,55,'liggend'),muur(495,300,55,'staand'),muur(550,300,55,'liggend'),muur(550,300,55,'staand'),muur(60,300,50,'staand'),muur(495,500,50,'staand'),
                muur(550,500,55,'staand'),muur(550,550,50,'liggend'),muur(1090,550,55,'liggend'),muur(1140,500,55,'staand'),muur(1090,65,55,'liggend'),muur(1140,65,55,'staand'),
                muur(1140,300,55,'staand')]
    else:       
        return 5  # geen levels meer!

def genereer_stekels(level_nummer):
    if level_nummer == 1:
        return [stekel(375,205,'links'), stekel(375,250,'links')]
    elif level_nummer == 2:
        return [stekel(475,150,'rechts'),stekel(360,200,'rechts'),stekel(360,250,'rechts'),stekel(360,300,'rechts'),stekel(360,350,'rechts'),
                stekel(385,450,'omhoog'),stekel(435,450,'omhoog'),stekel(555,125,'omlaag'),stekel(600,125,'omlaag'),stekel(645,125,'omlaag'),
                stekel(645,215,'omlaag'),stekel(695,350,'links'),stekel(695,400,'links')]

    elif level_nummer == 4:
        return [stekel(5,5,'omlaag'),stekel(55,5,'omlaag'),stekel(105,5,'omlaag'),stekel(155,5,'omlaag'),stekel(205,5,'omlaag'),stekel(255,5,'omlaag'),
                stekel(305,5,'omlaag'),stekel(355,5,'omlaag'),stekel(1075,300,'links')]
    elif level_nummer == 10:
        return [stekel(1145, 5, 'omlaag')]
    elif level_nummer == 11:
        return [stekel(1145,620,'omhoog'),stekel(1115,595,'links')]
    elif level_nummer == 12:
        return [stekel(550,525,'omhoog'),stekel(600,525,'omhoog'),stekel(650,525,'omhoog'),stekel(700,525,'omhoog'),stekel(750,525,'omhoog'),stekel(800,525,'omhoog'),stekel(850,525,'omhoog'),stekel(900,525,'omhoog'),stekel(950,525,'omhoog'),stekel(1000,525,'omhoog'),stekel(1050,525,'omhoog'),stekel(1095,395,'omhoog'),stekel(1045,395,'omhoog'),stekel(600,395,'omhoog'),stekel(755,220,'omlaag'),stekel(1085,150,'rechts'),stekel(1055,150,'links'),stekel(550,395,'omhoog'),stekel(5,620,'omhoog'),stekel(750,425,'omlaag'),stekel(800,425,'omlaag'),stekel(850,425,'omlaag'),stekel(900,425,'omlaag'),stekel(950,425,'omlaag'),stekel(1000,425,'omlaag'),stekel(1050,425,'omlaag'),stekel(1115,425,'links')]
    elif level_nummer == 13:
        return [stekel(5,245,'rechts'),stekel(5,295,'rechts'),stekel(5,345,'rechts'),stekel(5,395,'rechts'),stekel(5,195,'rechts'),stekel(5,620,'omhoog'),stekel(55,620,'omhoog'),stekel(105,620,'omhoog'),stekel(155,620,'omhoog'),stekel(205,620,'omhoog'),stekel(255,620,'omhoog'),stekel(305,620,'omhoog'),stekel(355,620,'omhoog'),stekel(405,620,'omhoog'),stekel(1170,595,'links'),stekel(1170,545,'links'),stekel(1170,495,'links'),stekel(1170,445,'links'),stekel(1170,395,'links'),stekel(1170,345,'links'),stekel(1170,295,'links'),stekel(1170,245,'links'),stekel(1170,195,'links'),stekel(1170,145,'links'),stekel(1170,95,'links'),stekel(1170,45,'links'),stekel(1145,5,'omlaag'),stekel(1095,5,'omlaag'),stekel(1045,5,'omlaag'),stekel(995,5,'omlaag'),stekel(945,5,'omlaag'),stekel(895,5,'omlaag'),stekel(845,5,'omlaag'),stekel(795,5,'omlaag'),stekel(745,5,'omlaag'),stekel(695,5,'omlaag'),stekel(645,5,'omlaag'),stekel(595,5,'omlaag'),stekel(545,5,'omlaag'),stekel(495,5,'omlaag'),stekel(495,245,'rechts'),stekel(495,195,'rechts'),stekel(495,145,'rechts'),stekel(495,95,'rechts'),stekel(495,45,'rechts'),stekel(1115,620,'omhoog'),stekel(1065,620,'omhoog'),stekel(1015,620,'omhoog'),stekel(965,620,'omhoog'),stekel(915,620,'omhoog'),stekel(865,620,'omhoog'),stekel(815,620,'omhoog')]
    elif level_nummer == 14:
        return [stekel(470,300,'links'),stekel(1170,5,'links'),stekel(5,5,'omlaag'),stekel(305,355,'omlaag')]
    elif level_nummer == 16:
        return [stekel(500,620,'omhoog'),stekel(550,595,'links'),stekel(550,545,'links'),stekel(550,495,'links'),stekel(550,445,'links'),stekel(550,395,'links'),stekel(395,355,'omlaag'),stekel(345,355,'omlaag'),stekel(5,5,'rechts'),stekel(5,55,'rechts'),stekel(5,105,'rechts'),stekel(5,155,'rechts'),stekel(5,205,'rechts'),stekel(5,255,'rechts'),stekel(5,305,'rechts'),stekel(5,355,'rechts'),stekel(5,405,'rechts'),stekel(5,455,'rechts'),stekel(5,505,'rechts'),stekel(315,545,'links'),stekel(315,495,'links'),stekel(315,445,'links'),stekel(315,395,'links'),stekel(315,345,'links'),stekel(315,295,'links'),stekel(315,245,'links'),stekel(140,5,'omlaag'),stekel(190,5,'omlaag'),stekel(240,5,'omlaag'),stekel(290,5,'omlaag'),stekel(1170,5,'links'),stekel(1170,55,'links'),stekel(1170,110,'links'),stekel(1170,160,'links')]
    elif level_nummer == 17:
        return [stekel(390,620,'omhoog'),stekel(440,620,'omhoog'),stekel(490,620,'omhoog'),stekel(540,620,'omhoog'),stekel(590,620,'omhoog'),stekel(640,620,'omhoog'),stekel(1145,620,'omhoog'),stekel(1095,620,'omhoog'),stekel(1045,620,'omhoog'),stekel(995,620,'omhoog'),stekel(945,620,'omhoog'),stekel(895,620,'omhoog'),stekel(1170,570,'links'),stekel(1170,520,'links'),stekel(1170,470,'links'),stekel(1170,420,'links'),stekel(1170,370,'links'),stekel(1170,320,'links'),stekel(1170,5,'links'),stekel(1170,55,'links'),stekel(1170,105,'links'),stekel(1170,155,'links'),stekel(1170,205,'links'),stekel(1120,5,'omlaag'),stekel(1070,5,'omlaag'),stekel(1020,5,'omlaag'),stekel(970,5,'omlaag'),stekel(920,5,'omlaag'),stekel(870,5,'omlaag'),stekel(390,5,'omlaag'),stekel(340,5,'omlaag'),stekel(290,5,'omlaag')]
    elif level_nummer == 18:
        return [stekel(5,430,'rechts'),stekel(495,5,'omlaag'),stekel(445,5,'omlaag'),stekel(395,5,'omlaag'),stekel(545,5,'omlaag'),stekel(595,5,'omlaag'),stekel(135,300,'rechts'),stekel(1110,5,'links'),stekel(5,225,'rechts')]
    elif level_nummer == 19:
        return [stekel(550,250,'omhoog')]
    else:
        return []
    
def genereer_stekel2s(level_nummer):
    if level_nummer == 3:
        return [stekel2(210,550,'rechts')]
    elif level_nummer == 5:
        return [stekel2(500,20,'omlaag'),stekel2(550,45,'links'),stekel2(100,45,'rechts'),stekel2(125,20,'omlaag'),stekel2(125,500,'omhoog'),stekel2(100,450,'rechts'),
                stekel2(1000,500,'omhoog'),stekel2(1050,450,'links'),stekel2(1000,200,'omlaag')]
    elif level_nummer == 6:
        return_lijst = [stekel2(750,5,'links'),stekel2(775,5,'rechts')]
        for x in range(200,1150+1,50):
            if x <= 1050:
                return_lijst.append(stekel2(x,450,'omhoog'))
            return_lijst.append(stekel2(x,375,'omlaag'))
        return return_lijst
    elif level_nummer == 7:
        return[stekel2(1065,545,'rechts'),stekel2(1065,545-50,'rechts'),stekel2(1065,545-100,'rechts'),stekel2(1065,545-150,'rechts'),stekel2(1065,545-200,'rechts'),stekel2(1065,545-250,'rechts'),
               stekel2(1065,545-300,'rechts'),stekel2(1065,545,'rechts'),stekel2(1065,545,'rechts'),stekel2(1065,545,'rechts'),stekel2(1065,545,'rechts')]
    elif level_nummer == 10:
        return[stekel2(145,30,'omlaag'),stekel2(140-20,595-75,'rechts'),stekel2(1145,105,'omlaag'),stekel2(145,570,'omhoog'),stekel2(145+50,570,'omhoog'),stekel2(145+100,570,'omhoog'),
               stekel2(145+150,570,'omhoog'),stekel2(145+200,570,'omhoog'),stekel2(145+250,570,'omhoog'),stekel2(145+300,570,'omhoog')]
    elif level_nummer == 11:
        return [stekel2(75,595,'rechts')]
    elif level_nummer == 12:
        return [stekel2(475,475,'rechts'),stekel2(755,195,'omhoog'),stekel2(5,340,'omhoog'),stekel2(5,120,'omlaag')]
    elif level_nummer == 13:
        return [stekel2(35,5,'omlaag'),stekel2(5,555,'rechts'),stekel2(475,355,'rechts')]
    elif level_nummer == 14:
        return [stekel2(555,300,'rechts')]
    elif level_nummer == 16:
        return [stekel2(10,595,'rechts'),stekel2(805,195,'omlaag'),stekel2(855,195,'omlaag'),stekel2(905,195,'omlaag'),stekel2(955,195,'omlaag'),stekel2(1005,195,'omlaag'),stekel2(1055,195,'omlaag')]
    elif level_nummer == 18:
        return [stekel2(5,595,'rechts')]
    elif level_nummer == 19:
        return [stekel2(270,300,'links')]
    elif level_nummer == 21:
        return [stekel2(500,510,'omhoog')]
    else:
        return []

def genereer_stekel3s(level_nummer):
    if level_nummer == 6:
        return [stekel3(80,400,'rechts'),stekel3(1200,600,'links')]
    elif level_nummer == 7:
        return [stekel3(60,126,'omlaag'),stekel3(420,595,'rechts')]
    elif level_nummer == 8:
        return [stekel3(800-25,350,'rechts')]
    elif level_nummer == 10:
        return [stekel3(200,30,'omlaag'),stekel3(550,650,'omhoog'),stekel3(1200,600,'links')]
    elif level_nummer == 11:
        return [stekel3(1200,5,'links')]
    elif level_nummer == 12:
        return [stekel3(365,5,'omlaag'),stekel3(280,150,'links')]
    elif level_nummer == 13:
        return [stekel3(35,5,'omlaag'),stekel3(850,330,'omlaag')]
    elif level_nummer == 14:
        return [stekel3(5,570,'omhoog')]
    elif level_nummer == 15:
        return [stekel3(555,650,'omhoog')]
    elif level_nummer == 16:
        return [stekel3(870,620,'omhoog'),stekel3(920,620,'omhoog'),stekel3(970,620,'omhoog'),stekel3(1020,620,'omhoog'),stekel3(1070,620,'omhoog')]
    elif level_nummer == 19:
        return [stekel3(1195,300,'links')]
    else:
        return []

def genereer_powerups(level_nummer):
    if level_nummer == 1:
        return [Powerup(400,205,'Kogel'),Powerup(400,255,'Munt')]
    elif level_nummer == 2:
        return [Powerup(380,300,'Munt'),Powerup(380,350,'Kogel')]
    elif level_nummer == 3:
        return [Powerup(235,300,'Muntx2'),Powerup(335,300,'Munt'),Powerup(435,300,'Kogel'),Powerup(235,550,'Hartje')]
    elif level_nummer == 4:
        return [Powerup(600,355,'Versnelling'),Powerup(650,355,'Kogel'),Powerup(700,355,'Munt')]
    elif level_nummer == 5:
        return [Powerup(200,225,'Munt'),Powerup(250,225,'Hartje'),Powerup(300,225,'Kogel'),Powerup(350,225,'Hartje'),Powerup(400,225,'Munt')]
    elif level_nummer == 6:
        return [Powerup(800,5,'Hartje'),Powerup(850,5,'Kogel')]
    elif level_nummer == 7:
        return [Powerup(1145,545,'Kogel'),Powerup(1145,595,'Hartje'),Powerup(115,205,'Schild')]
    elif level_nummer == 8:
        return [Powerup(1000,55,'Kogel'),Powerup(1000,105,'Hartje'),Powerup(1000,155,'Versnelling'),Powerup(1000,205,'Munt'),Powerup(1000,255,'Muntx2')]
    elif level_nummer == 9:
        return [Powerup(100,150,'Kogel'),Powerup(100,200,'Hartje')]
    elif level_nummer == 10:
        return [Powerup(1145,50,'Schild'),Powerup(1145,600,'Munt'),Powerup(1100,600,'Hartje'),Powerup(1050,600,'Kogel'),Powerup(50,600,'Munt')]
    elif level_nummer == 11:
        return [Powerup(500,355,'Schild'),Powerup(100,250,'Kogel'),Powerup(495,595,'Hartje'),Powerup(210,5,'Hartje'),Powerup(310,5,'Hartje'),Powerup(260,5,'Versnelling')]
    elif level_nummer == 12:
        return [Powerup(500,475,'Munt'),Powerup(800,475,'Hartje'),Powerup(985,5,'Muntx2'),Powerup(995,370,'Munt'),Powerup(755,145,'Munt'),Powerup(595,5,'Kogel'),Powerup(230,30,'Hartje'),Powerup(95,300,'Munt')]
    elif level_nummer == 13:
        return [Powerup(35,40,'Hartje'),Powerup(35,90,'Kogel'),Powerup(35,395,'Munt'),Powerup(465,595,'Munt'),Powerup(590,595,'Munt'),Powerup(750,595,'Munt'),Powerup(655,595,'Muntx2'),Powerup(525,595,'Hartje'),Powerup(500,355,'Munt')]
    elif level_nummer == 14:
        return [Powerup(580,295,'Schild'),Powerup(580,5,'Hartje'),Powerup(500,595,'Hartje'),Powerup(305,5,'Hartje'),Powerup(55,5,'Kogel'),Powerup(100,5,'Hartje'),Powerup(150,5,'Munt'),Powerup(875,305,'Munt'),Powerup(305,300,'Munt')]
    elif level_nummer == 15:
        return [Powerup(1145,5,'Muntx2'),Powerup(610,170,'Munt'),Powerup(1140,225,'Munt'),Powerup(610,280,'Munt'),Powerup(1140,335,'Munt'),Powerup(610,390,'Munt'),Powerup(1145,445,'Munt'),Powerup(1145,115,'Munt'),Powerup(610,60,'Munt'),Powerup(1145,590,'Kogel'),Powerup(1095,590,'Hartje'),Powerup(1145,595,'Schild')]
    elif level_nummer == 16:
        return [Powerup(445,300,'Hartje'),Powerup(30,595,'Munt'),Powerup(85,5,'Schild'),Powerup(85,55,'Hartje'),Powerup(345,300,'Hartje'),Powerup(390,300,'Hartje'),Powerup(345,250,'Hartje'),Powerup(555,335,'Kogel'),Powerup(555,110,'Munt'),Powerup(580,595,'Hartje'),Powerup(815,340,'Hartje'),Powerup(115,275,'Muntx2')]
    elif level_nummer == 17:
        return [Powerup(500,390,'Schild'),Powerup(445,5,'Hartje'),Powerup(815,5,'Kogel'),Powerup(335,595,'Hartje'),Powerup(230,5,'Munt')]
    elif level_nummer == 18:
        return [Powerup(5,485,'Muntx2'),Powerup(5,535,'Munt'),Powerup(55,485,'Munt'),Powerup(105,485,'Munt'),Powerup(155,485,'Munt'),Powerup(210,485,'Hartje'),Powerup(260,485,'Hartje'),Powerup(80,105,'Munt'),Powerup(5,170,'Munt'),Powerup(5,30,'Munt'),Powerup(685,170,'Hartje'),Powerup(1085,225,'Hartje'),Powerup(1140,5,'Hartje'),Powerup(780,370,'Kogel')]
    elif level_nummer == 19:
        return [Powerup(810,595,'Hartje'),Powerup(1145,300,'Munt'),Powerup(495,245,'Munt'),Powerup(220,250,'Munt'),Powerup(5,595,'Munt'),Powerup(970,95,'Hartje'),Powerup(745,95,'Hartje'),Powerup(440,5,'Kogel')]
    elif level_nummer == 20:
        return [Powerup(445,470,'Hartje'),Powerup(445,195,'Hartje'),Powerup(855,300,'Hartje'),Powerup(670,470,'Hartje'),Powerup(555,410,'Kogel'),Powerup(390,365,'Munt'),Powerup(800,465,'Munt'),Powerup(665,300,'Munt'),Powerup(555,300,'Munt'),Powerup(800,195,'Munt'),Powerup(340,250,'Munt'),Powerup(320,545,'Muntx2'),Powerup(370,545,'Munt'),Powerup(420,545,'Munt'),Powerup(470,545,'Munt'),Powerup(515,545,'Munt'),Powerup(560,545,'Muntx2')]
    elif level_nummer == 21:
        return [Powerup(65,70,'Kogel'),Powerup(65,495,'Kogel'),Powerup(500,70,'Kogel'),Powerup(500,455,'Kogel'),Powerup(1090,70,'Kogel'),Powerup(1090,495,'Kogel')]
    else:
        return []

def genereer_geesten(level_nummer):
    if level_nummer == 7:
        return [geest(550,5,7)]
    elif level_nummer == 8:
        return [geest(50,5,8)]
    elif level_nummer == 10:
        return [geest(400,300,11)]
    elif level_nummer == 14:
        return [geest(935,245,0)]
    elif level_nummer == 19:
        return [geest(1065,235,0)]
    else:
        return []

def genereer_planten(level_nummer):
    if level_nummer == 11:
        return [plant(560,360,0,'rechts'),plant(560,410,0,'rechts'),plant(560,460,0,'rechts'),plant(555,245,0,'omhoog')]
    elif level_nummer == 12:
        return [plant(925,10,0,'rechts'),plant(550,425,0,'omlaag'),plant(600,425,0,'omlaag'),plant(650,425,0,'omlaag'),plant(700,425,0,'omlaag')]
    elif level_nummer == 13:
        return [plant(650,230,0,'links',3)]
    elif level_nummer == 15:
        return [plant(955,595,0,'omhoog'),plant(610,520,0,'links')]
    elif level_nummer == 16:
        return [plant(345,30,0,'links')]
    elif level_nummer == 18:
        return [plant(815,430,0,'links')]
    else:
        return []

def genereer_whirls(level_nummer):
    if level_nummer == 16:
        return []
    elif level_nummer == 17:
        return [whirl(755,340,1,0.2),whirl(120,165,1,1),whirl(120,300,1,1)]
    elif level_nummer == 18:
        return [whirl(898,128,1,2)]
    elif level_nummer == 19:
        return [whirl(112,87,1,2.5),whirl(93,438,1,2.5)]
    elif level_nummer == 20:
        return []
    else:
        return []

def genereer_bewegende_muren(level_nummer): #startx,starty,eindx,eindy,lengte,orientatie(,tijd)
    if level_nummer == 9:
        return [bewegende_muur(200,30,1000,30,50,'liggend'),bewegende_muur(200,600,1000,600,50,'liggend')]
    elif level_nummer == 12:
        return []
    elif level_nummer == 13:
        return [bewegende_muur(30,195,30,400,50,'staand'),bewegende_muur(5,605,410,605,50,'liggend'),bewegende_muur(645,355,645,530,175,'staand'),bewegende_muur(520,35,520,150,55,'staand'),bewegende_muur(810,470,810,590,55,'staand'),bewegende_muur(495,30,1100,30,95,'liggend')]
    elif level_nummer == 14:
        return [bewegende_muur(55,300,55,590,55,'staand')]
    elif level_nummer == 19:
        return [bewegende_muur(545,5,545,245,55,'staand')]
    else:
        return []
    
def genereer_knop_muren(level):
    if level == 4:
        return [knop_muur(650,575,520,590,55,'staand')]
    elif level == 7:
        return [knop_muur(800,170,1165,635,50,'liggend')]
    elif level == 8:
        return [knop_muur(250,445,840,75,55,'liggend')]
    elif level == 11:
        return [knop_muur(1145,435,1165,425,50,'liggend')]
    elif level == 13:
        return [knop_muur(850,40,855,60,55,'staand')]
    elif level == 14:
        return [knop_muur(300,55,320,45,55,'liggend'),knop_muur(355,350,360,370,55,'staand')]
    elif level == 15:
        return [knop_muur(495,595,610,620,50,'staand')]
    elif level == 19:
        return [knop_muur(270,590,5,330,55,'staand')]
    else:
        return []

def genereer_decoraties(level):
    if level == 1:
        return [decoratie(35,145,1)]
    elif level == 2:
        return [decoratie(570,35,1)]
    elif level == 3:
        return [decoratie(970,65,3)]
    elif level == 4:
        return [decoratie(700,490,2),decoratie(160,545,1)]
    elif level == 5:
        return [decoratie(700,270,3)]
    elif level == 6:
        return [decoratie(970,290,1),decoratie(920,290,1)]
    elif level == 7:
        return [decoratie(1005,100,2),decoratie(895,100,2),decoratie(260,550,1)]
    elif level == 8:
        return [decoratie(870,185,3)]
    elif level == 9:
        return [decoratie(160,545,1),decoratie(210,545,1),decoratie(260,545,1),decoratie(750,545,1),decoratie(800,545,1)]
    elif level == 10:
        return [decoratie(700,270,3)]
    elif level == 11:
        return [decoratie(825,5,2),decoratie(825,105,2),decoratie(825,205,2),decoratie(825,305,2),decoratie(825,405,2),decoratie(825,505,2),decoratie(825,605,2),decoratie(65,140,1),decoratie(90,140,1)]
    elif level == 12:
        return [decoratie(665,320,1),decoratie(250,245,3)]
    elif level == 13:
        return [decoratie(520,355,2),decoratie(520,455,2),decoratie(520,555,2),decoratie(225,120,3)]
    elif level == 14:
        return [decoratie(1010,5,2),decoratie(1010,105,2),decoratie(1010,205,2),decoratie(1010,305,2),decoratie(1010,405,2),decoratie(1010,505,2),decoratie(1010,605,2),decoratie(415,195,1),decoratie(390,195,1)]
    elif level == 15:
        return [decoratie(240,5,2),decoratie(240,105,2),decoratie(240,205,2),decoratie(240,305,2),decoratie(240,405,2),decoratie(240,505,2),decoratie(240,605,2),decoratie(720,525,3)]
    elif level == 16:
        return [decoratie(365,545,2),decoratie(1060,5,2),decoratie(645,290,1),decoratie(35,495,3)]
    elif level == 17:
        return [decoratie(740,545,1),decoratie(35,545,2)]
    elif level == 18:
        return [decoratie(850,545,2),decoratie(780,545,2),decoratie(705,545,2),decoratie(475,380,1)]
    elif level == 19:
        return [decoratie(200,150,3),decoratie(420,545,2),decoratie(540,545,2)]
    else:
        return []

def genereer_bounce_points(level):
    if level == 16:
        return [bounce_point(500,430),bounce_point(500,480),bounce_point(190,595),bounce_point(190,400),bounce_point(190,165),bounce_point(35,165),bounce_point(35,400),bounce_point(915,30),bounce_point(1060,470)]
    elif level == 17:
        return [bounce_point(500,490),bounce_point(1025,490),bounce_point(1025,120)]
    elif level == 18:
        return [bounce_point(495,115)]
    elif level == 19:
        return []
    elif level == 20:
        return [bounce_point(90,545),bounce_point(95,190),bounce_point(95,70),bounce_point(990,70),bounce_point(985,545),bounce_point(855,545)]
    else:
        return []

def genereer_tekst(level):
    if level == 1:
        return [tutorial(80,400,"Welcome to Swipe! To beat the level, you have to go to the finish.","Use WASD or Arrow keys to move. Don't touch spikes, they kill you!")]
    elif level == 3:
        return [tutorial(100,430,"Ouch! These tricky blocks contain spikes!","If you stand on them for too long, they will show you some spikes...")]
    elif level == 4:
        return [tutorial(580,170,"Some levels have buttons that","will remove walls once you step on them.","Try to get the powerups!")]
    elif level == 6:
        return [tutorial(180,180,"Some more tricky blocks!","These will launch an entire spike...","Careful!")]
    elif level == 7:
        return [tutorial(640,370,"These ghosts will chase you once","you come near one.","Try to kill them with spacebar!")]
    elif level == 9:
        return [tutorial(570,270,"Well, I guess you have to","time your movement right...","(you can float once they move away!)")]
    elif level == 11:
        return [tutorial(150,400,"Woah! These plants shoot spikes!","Try to avoid them...","(use the shield!)")]
    elif level == 16:
        return [tutorial(645,440,"These circles allow you to travel in","every direction when near one!")]
    elif level == 17:
        return [tutorial(560,125,"Whirls grow size over time...","Although some do that faster than others!","If you get in a whirl, you die...","(use the shield!)")]
    else:
        return []
    

#########################
#Special genereer stuffs#
#########################

def genereer_rand_muren():
    return [muur(0,0,1200,'liggend'), muur(0,0,650,'staand'),muur(0,645,1200,'liggend'),muur(1195,0,650,'staand')]

def genereer_rand_stekels(level_nummer):
    stekel_lijst = []
    if level_nummer in [3,5,9,20]:
        for y in range(13):
            stekel_lijst.append(stekel(0,y*50,'rechts'))
            stekel_lijst.append(stekel(1175,y*50,'links'))
        for x in range(24):
            stekel_lijst.append(stekel(x*50,0,'omlaag'))
            stekel_lijst.append(stekel(x*50,625,'omhoog'))
            
    return stekel_lijst

def genereer_bazen(level_nummer):
    if level_nummer == 21:
        return [boss(300,900)]
    else:
        return []


    
################
#Einde spel Def#
################

def einde_spel(scherm,schermblit): #win
    achtergrond(scherm)
    menufont = pg.font.Font('papyrus',100)
    tekst = menufont.render('Game Finished!',True,(255,255,255))
    scherm.blit(tekst,(250,250))
    
    schermblit.blit(pg.transform.scale(scherm, schermblit.get_rect().size).convert(), (0, 0))
    pg.display.flip()
    
    t.sleep(5)

##############
#Class Finish#
##############

class finish:
    def __init__(self):
        self.x = 25
        self.y = 250

    def update_locatie(self, level_nummer):
        if int(level_nummer) == 1: 
            self.x = 25
            self.y = 250
        elif int(level_nummer) == 2:
            self.x = 445
            self.y = 300
        elif int(level_nummer) == 3:
            self.x = 235
            self.y = 245
        elif int(level_nummer) == 4:
            self.x = 410
            self.y = 5
        elif int(level_nummer) == 5:
            self.x = 35
            self.y = 225
        elif int(level_nummer) == 6:
            self.x = 650
            self.y = 325
        elif int(level_nummer) == 7:
            self.x = 800
            self.y = 175
        elif int(level_nummer) == 8:
            self.x = 1100
            self.y = 55
        elif int(level_nummer) == 9:
            self.x = 100
            self.y = 100
        elif int(level_nummer) == 11:
            self.x = 555
            self.y = 595
        elif int(level_nummer) == 10:
            self.x = 5
            self.y = 595
        elif int(level_nummer) == 12:
            self.x = 1145
            self.y = 595
        elif int(level_nummer) == 13:
            self.x = 595
            self.y = 300
        elif int(level_nummer) == 14:
            self.x = 5
            self.y = 595
        elif int(level_nummer) == 15:
            self.x = 5
            self.y = 5
        elif int(level_nummer) == 16:
            self.x = 580
            self.y = 395
        elif int(level_nummer) == 17:
            self.x = 235
            self.y = 490
        elif int(level_nummer) == 18:
            self.x,self.y = 5,280
        elif int(level_nummer) == 19:
            self.x,self.y = 1145,595
        elif int(level_nummer) == 20:
            self.x,self.y = 575,140
        else:
            self.x = 10000
            self.y = 10000
            
    def teken(self,scherm):
        scherm.blit(finish_foto,(self.x,self.y))

##################
#Class Checkpoint#
##################

class checkpoint:
    def __init__(self):
        self.check = False
        self.frame = 1
        self.animatie_tijd = 0
        self.x = 0
        self.y = 0

    def update_locatie(self, level_nummer):
        self.check = False
        self.frame = 1
        self.animatie_tijd = 0
        if int(level_nummer) == 11:
            self.x = 500
            self.y = 245
        elif int(level_nummer) == 12:
            self.x = 750
            self.y = 370
        elif int(level_nummer) == 13:
            self.x = 430
            self.y = 555
        elif int(level_nummer) == 15:
            self.x = 1075
            self.y = 445
        elif int(level_nummer) == 16:
            self.x = 500
            self.y = 245
        elif int(level_nummer) == 17:
            self.x = 445
            self.y = 295
        elif int(level_nummer) == 19:
            self.x,self.y = 275,245
        else:
            self.x = 10000
            self.y = 10000
            
    def teken(self,scherm):
        scherm.blit(eval('checkpoint'+str(self.frame)+'_foto'),(self.x,self.y))

    def animate(self):
        if t.perf_counter() > self.animatie_tijd + 0.05:
            if self.frame < 11:
                self.frame += 1
            else:
                return False
            self.animatie_tijd = t.perf_counter()
        return True

        
#################
#Particle Stuffs#
#################

def update_particles(particle_lijst,deltaTime):
    for particle in particle_lijst:
        
        particle[0][0] += particle[1][0]#x pos
        particle[0][1] += particle[1][1]#y pos
        if r.randint(0,10) > 9 and particle[3] == 1:
            particle[1][0] = r.randint(-10,10)/10
        particle[2] -= 0.1
        if particle[2] < 0.2:
            particle_lijst.remove(particle)
                
    return particle_lijst
    
def teken_particles(scherm,particle_lijst,level):
    kleur = (255,255,255)
    if level == 21:
        kleur = (222, 61, 24)
    elif level < 11: #pyramid
        kleur = (248, 243, 61)
    elif level < 16: #jungle
        kleur = (24, 163, 33)
    elif level < 21: #underwater
        kleur = (32, 113, 245)
        
    for particle in particle_lijst:
        if particle[3] == 1:#normal
            pg.draw.rect(scherm,kleur,((round(particle[0][0]),round(particle[0][1])),(int(particle[2]/6),int(particle[2]/6))))
        elif particle[3] == 2:#explosive
            pg.draw.rect(scherm,kleur,((round(particle[0][0]),round(particle[0][1])),(int(particle[2]/2),int(particle[2]/2))))
        elif particle[3] == 3:#hit
            pg.draw.rect(scherm,kleur,((round(particle[0][0]),round(particle[0][1])),(int(particle[2]/3),int(particle[2]/3))))
        elif particle[3] == 4:#collect
            pg.draw.rect(scherm,kleur,((round(particle[0][0]),round(particle[0][1])),(int(particle[2]/4),int(particle[2]/5))))
        elif particle[3] == 5:#big boi
            pg.draw.rect(scherm,kleur,((round(particle[0][0]),round(particle[0][1])),(int(particle[2]),int(particle[2]))))
        elif particle[3] == 6:#spiky boi
            pg.draw.rect(scherm,(255, 0, 0),((round(particle[0][0]),round(particle[0][1])),(int(particle[2]/4),int(particle[2]/4))))
            
################################
#Stekel genereer afbeelding Def#
################################

def genereer_stekel_afbeelding(richting):
    if richting == 'omhoog':
        afbeelding = stekels_foto
        hoogte = 25
        breedte = 50
    elif richting == 'rechts':
        afbeelding = pg.transform.rotate(stekels_foto, 270)
        hoogte = 50
        breedte = 25
    elif richting == 'omlaag':
        afbeelding = pg.transform.rotate(stekels_foto, 180)
        hoogte = 25
        breedte = 50
    else: # links
        afbeelding = pg.transform.rotate(stekels_foto, 90)
        hoogte = 50
        breedte = 25
    return afbeelding,hoogte,breedte

################################
#Class Stekel, Stekel2, Stekel3#
################################

class stekel:
    def __init__(self,x,y,richting):
        self.x = x
        self.y = y
        self.richting = richting
        self.afbeelding,self.hoogte,self.breedte = genereer_stekel_afbeelding(richting)

    def teken(self,scherm):
        scherm.blit(self.afbeelding,(self.x,self.y))
        
    def get_code(self,last):
        if last:
            return "stekel("+str(self.x)+","+str(self.y)+",'"+str(self.richting)+"')"
        else:
            
            return "stekel("+str(self.x)+","+str(self.y)+",'"+str(self.richting)+"'),"
            
class stekel2:
    def __init__(self,x,y,richting):
        self.x = x
        self.y = y
        self.stekel_x = x
        self.stekel_y = y
        self.richting = richting
        self.afbeelding,self.hoogte,self.breedte = genereer_stekel_afbeelding(richting)
        self.lengte = self.hoogte
        self.start_tijd = -5
        if self.richting in ['omhoog','links']:
            self.lijn_x = self.x
            self.lijn_y = self.y
        elif self.richting == 'rechts':
            self.lijn_y = self.y
            self.lijn_x = self.x + self.breedte - 5
        else: # omlaag
            self.lijn_y = self.y + self.hoogte - 5
            self.lijn_x = self.x

    def update_stekel_locatie(self):
        if t.perf_counter() - self.start_tijd > 1.2 and t.perf_counter() - self.start_tijd < 3:
            if self.richting == 'omhoog':
                self.stekel_y = self.y - 25
            elif self.richting == 'omlaag':
                self.stekel_y = self.y + 25
            elif self.richting == 'links':
                self.stekel_x = self.x - 25
            else: #rechts
                self.stekel_x = self.x + 25
        else:
            self.stekel_x = self.x
            self.stekel_y = self.y

    def teken(self,scherm,level,tekenen):
        self.update_stekel_locatie()
        if tekenen:
            scherm.blit(self.afbeelding,(self.stekel_x,self.stekel_y)) # stekel
            pg.draw.rect(scherm,get_color(level), ((self.x,self.y),(self.breedte, self.hoogte)))
            if self.richting in ['links','rechts']:
                pg.draw.rect(scherm,(2, 242, 242),((self.lijn_x,self.lijn_y),(5,self.hoogte)))
            else: #omhoog,omlaag
                pg.draw.rect(scherm,(2, 242, 242),((self.lijn_x,self.lijn_y),(self.breedte,5)))
        return self.x,self.y,self.richting

    def begin_timer(self,Blokje,type_stekel='2'):
        if (t.perf_counter() - self.start_tijd > 3 and type_stekel == '2') or (t.perf_counter() - self.start_tijd < 0 and type_stekel == '3'):
            if self.richting == 'omhoog':
                if self.x < Blokje.x + Blokje.breedte and self.x + self.breedte > Blokje.x:
                    if self.y > Blokje.y and self.y - self.hoogte < Blokje.y + Blokje.breedte:
                        self.start_tijd = t.perf_counter()
                        return True
            elif self.richting == 'omlaag':
                if self.x < Blokje.x + Blokje.breedte and self.x + self.breedte > Blokje.x:
                    if self.y + self.hoogte < Blokje.y + Blokje.breedte and self.y + self.hoogte * 2 > Blokje.y:
                        self.start_tijd = t.perf_counter()
                        return True
            elif self.richting == 'links':
                if self.x > Blokje.x and self.x - self.breedte < Blokje.x + Blokje.breedte:
                    if self.y < Blokje.y + Blokje.breedte and self.y + self.hoogte > Blokje.y:
                        self.start_tijd = t.perf_counter()
                        return True
            else: #rechts
                if self.x + self.breedte < Blokje.x + Blokje.breedte and self.x + 2*self.breedte > Blokje.x:
                    if self.y < Blokje.y + Blokje.breedte and self.y + self.hoogte > Blokje.y:
                        self.start_tijd = t.perf_counter()
                        return True
        return False

    def get_code(self,last):
        if last:
            return "stekel2("+str(self.x)+","+str(self.y)+",'"+str(self.richting)+"')"
        else:
            
            return "stekel2("+str(self.x)+","+str(self.y)+",'"+str(self.richting)+"'),"

class stekel3(stekel2):
    def __init__(self,x,y,richting):
        super().__init__(x,y,richting)
        self.knop_grootte = 10
        self.vx = 0
        self.vy = 0
        self.start_tijd = 1e7
        if self.richting == 'omhoog':
            self.knop_x = self.x + (self.breedte-self.knop_grootte) / 2
            self.knop_y = self.y - self.knop_grootte
            self.vy = -1
        elif self.richting == 'links':
            self.knop_x = self.x - self.knop_grootte
            self.knop_y = self.y + (self.lengte-self.knop_grootte) / 2
            self.vx = -1
        elif self.richting == 'omlaag':
            self.knop_x = self.x + (self.breedte-self.knop_grootte) / 2
            self.knop_y = self.y + self.lengte
            self.vy = 1
        else: #rechts
            self.knop_x = self.x + self.breedte
            self.knop_y = self.y + (self.lengte-self.knop_grootte) / 2
            self.vx = 1

    def update_stekel_locatie(self,deltaTime,teken):
        if t.perf_counter() - self.start_tijd > 1.2:
            if teken:
                self.stekel_x += self.vx/1.9 * deltaTime
                self.stekel_y += self.vy/1.9 * deltaTime
            if self.stekel_x < -25 or self.stekel_x > 1225 or self.stekel_y < -25 or self.stekel_y > 675:
                self.stekel_x = self.x
                self.stekel_y = self.y
                self.start_tijd = 1e8


    def teken(self,scherm, deltaTime,level,teken):
        self.update_stekel_locatie(deltaTime,teken)
        if teken:
            scherm.blit(self.afbeelding,(int(self.stekel_x),int(self.stekel_y))) # stekel
            pg.draw.rect(scherm,get_color(level), ((self.x,self.y),(self.breedte, self.hoogte)))
            pg.draw.rect(scherm,(255,0,0),((self.knop_x,self.knop_y),(self.knop_grootte,self.knop_grootte)))
        return self.x, self.y, self.richting

    def get_code(self,last):
        if last:
            return "stekel3("+str(self.x)+","+str(self.y)+",'"+str(self.richting)+"')"
        else:
            
            return "stekel3("+str(self.x)+","+str(self.y)+",'"+str(self.richting)+"'),"
        
###############
#Class Powerup#
###############
                        
class Powerup:
    def __init__(self,x,y,pu_type):
        self.x = x
        self.y = y
        self.gepakt = False
        self.hoogte = 50
        self.pu_type = pu_type
        self.animatie = 1
        self.animatie_tijd = -1
        if self.pu_type == 'Munt':
            self.foto = munt1_foto
        elif self.pu_type == 'Muntx2':
            self.foto = muntx21_foto
        elif self.pu_type == 'Hartje':
            self.foto = hartje1_foto
        elif self.pu_type == 'Versnelling':
            self.foto = versnelling1_foto
        elif self.pu_type == 'Schild':
            self.foto = schild1_foto
        elif self.pu_type == 'Kogel':
            self.foto = kogel1_foto

    def get_code(self,last):
        if last:
            return "Powerup("+str(self.x)+","+str(self.y)+",'"+str(self.pu_type)+"')"
        else:
            
            return "Powerup("+str(self.x)+","+str(self.y)+",'"+str(self.pu_type)+"'),"
        
    def teken(self,scherm):
        if not self.gepakt:
            if self.pu_type == 'Munt':
                if self.animatie%8 == 0:
                    scherm.blit(munt1_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 1:
                    scherm.blit(munt2_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 2:
                    scherm.blit(munt3_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 3:
                    scherm.blit(munt4_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 4:
                    scherm.blit(munt5_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 5:
                    scherm.blit(munt6_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 6:
                    scherm.blit(munt7_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 7:
                    scherm.blit(munt8_foto,(self.x+ 5, self.y+ 5))
                    
            elif self.pu_type == 'Muntx2':
                if self.animatie%8 == 0:
                    scherm.blit(muntx21_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 1:
                    scherm.blit(muntx22_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 2:
                    scherm.blit(muntx23_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 3:
                    scherm.blit(muntx24_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 4:
                    scherm.blit(muntx25_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 5:
                    scherm.blit(muntx26_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 6:
                    scherm.blit(muntx27_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 7:
                    scherm.blit(muntx28_foto,(self.x+ 5, self.y+ 5))
                    
            elif self.pu_type == 'Hartje':
                if self.animatie%4 == 0:
                    scherm.blit(hartje1_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%4 == 1:
                    scherm.blit(hartje2_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%4 == 2:
                    scherm.blit(hartje3_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%4 == 3:
                    scherm.blit(hartje4_foto,(self.x+ 5, self.y+ 5))

            elif self.pu_type == 'Kogel':
                if self.animatie%4 == 0:
                    scherm.blit(kogel1_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%4 == 1:
                    scherm.blit(kogel2_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%4 == 2:
                    scherm.blit(kogel3_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%4 == 3:
                    scherm.blit(kogel2_foto,(self.x+ 5, self.y+ 5))
                    
            elif self.pu_type == 'Versnelling':
                if self.animatie%7 == 0:
                    scherm.blit(versnelling1_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%7 == 1:
                    scherm.blit(versnelling2_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%7 == 2:
                    scherm.blit(versnelling3_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%7 == 3:
                    scherm.blit(versnelling4_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%7 == 4:
                    scherm.blit(versnelling5_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%7 == 5:
                    scherm.blit(versnelling6_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%7 == 6:
                    scherm.blit(versnelling7_foto,(self.x+ 5, self.y+ 5))
                    
            elif self.pu_type == 'Schild':
                if self.animatie%8 == 0:
                    scherm.blit(schild1_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 1:
                    scherm.blit(schild2_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 2:
                    scherm.blit(schild3_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 3:
                    scherm.blit(schild4_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 4:
                    scherm.blit(schild5_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 5:
                    scherm.blit(schild6_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 6:
                    scherm.blit(schild7_foto,(self.x+ 5, self.y+ 5))
                if self.animatie%8 == 7:
                    scherm.blit(schild8_foto,(self.x+ 5, self.y+ 5))
                    
            else:
                scherm.blit(self.foto,(self.x+ 5, self.y+ 5))
                
    def animatie_set(self):
        if t.perf_counter() > self.animatie_tijd + 0.1:
            self.animatie += 1
            self.animatie_tijd = t.perf_counter()

            

#############
#Class Geest#
#############

class geest:
    def __init__(self,x,y,level):
        self.x = x
        self.y = y
        self.level = level
        self.boss = False
        self.hoogte = 50
        self.emotie = 'neutraal'
        self.wakker = False        
        self.vx = 1
        self.vy = 1
        self.richting = 'stilstand'
        self.starttijd = 1e9
        self.beweeg_teller = 0
        self.start_x = x
        self.start_y = y
        
    def get_code(self,last):
        if last:
            return "geest("+str(self.x)+","+str(self.y)+","+str(self.level)+")"
        else:
            
            return "geest("+str(self.x)+","+str(self.y)+","+str(self.level)+"),"

    def teken(self,scherm):
        self.afbeelding = eval('geest_'+self.emotie+'_foto')
        scherm.blit(self.afbeelding,(round(self.x),round(self.y)))

    def beweeg(self,level,deltaTime):
        if level == 21 and not self.boss:
            self.vx = 1.5
            self.vy = 1.5
            
        self.beweeg_teller += 1
        
        if self.wakker and self.emotie == 'boos' and self.beweeg_teller % 2 == 0:
            if self.richting == 'omhoog':
                self.y -= self.vy/5 * deltaTime
            elif self.richting == 'omlaag':
                self.y += self.vy/5 * deltaTime
            elif self.richting == 'rechts':
                self.x += self.vx/5 * deltaTime
            elif self.richting == 'links':
                self.x -= self.vx/5 * deltaTime

    def word_wakker(self,Blokje):
        if self.x +self.hoogte + 100 > Blokje.x and self.x -100 < Blokje.x + Blokje.breedte and not self.wakker:
            if self.y + self.hoogte + 100 > Blokje.y and self.y - 100 < Blokje.y + Blokje.breedte:
                self.wakker = True
                self.emotie = 'boos'
                self.starttijd = t.perf_counter()
                

    def bepaal_richting(self,Blokje):
        if self.wakker and self.emotie == 'boos' and t.perf_counter()-self.starttijd > 2: # wacht 2 seconden met bewegen
            DX = Blokje.x - self.x
            DY = Blokje.y - self.y
            if abs(DX) > abs(DY):
                if DX > 0 :
                    self.richting = 'rechts'
                else:
                    self.richting = 'links'
            else:
                if DY > 0:
                    self.richting = 'omlaag'
                else:
                    self.richting = 'omhoog'

    def check_stekel(self, stekel_lijst):
        for Stekel in stekel_lijst:
            if self.x < Stekel.x + Stekel.breedte and self.x + self.hoogte > Stekel.x:
                if self.y < Stekel.y + Stekel.hoogte and self.y + self.hoogte > Stekel.y:
                    self.emotie = 'dood'

    def check_stekel2(self, stekel2_lijst):    
        for Stekel in stekel2_lijst:
            if t.perf_counter() - Stekel.start_tijd > 0.7 and t.perf_counter() - Stekel.start_tijd < 3:
                if self.x < Stekel.stekel_x + Stekel.breedte and self.x + self.hoogte > Stekel.stekel_x:
                    if self.y < Stekel.stekel_y + Stekel.hoogte and self.y + self.hoogte > Stekel.stekel_y:
                        self.emotie = 'dood'

    def check_stekel3(self, stekel_lijst):
        for Stekel in stekel_lijst:
            if t.perf_counter() - Stekel.start_tijd > 0.7:
                if Stekel.stekel_x < -25 or Stekel.stekel_x > 1225 or Stekel.stekel_y < -25 or Stekel.stekel_y > 675:
                    if self.x < Stekel.x + Stekel.breedte and self.x + self.hoogte > Stekel.x:
                        if self.y < Stekel.y + Stekel.hoogte and self.y + self.hoogte > Stekel.y:
                            self.emotie = 'dood'

    def check_kogel(self,kogel_lijst):
        for Kogel in kogel_lijst:
            if Kogel.actief:
                if self.x < Kogel.x + Kogel.breedte and self.x + self.hoogte > Kogel.x:
                    if self.y < Kogel.y + Kogel.hoogte and self.y + self.hoogte > Kogel.y:
                        self.emotie = 'dood'

#############
#Class Plant#
#############

class plant(geest):
    def __init__(self,x,y,level,richting,wachttijd=0.7):
        super().__init__(x,y,level)
        self.emotie = 'boos'
        self.wachttijd = wachttijd
        self.x = x
        self.y = y
        self.level = level
        self.richting = richting
        self.hoogte = 0
        self.vx = 0
        self.vy = 0
        self.start_tijd = t.perf_counter() + self.wachttijd
        self.stekel_x = self.x
        self.stekel_y = self.y
        self.lengte = 0
        self.breedte = 0
        self.afbeelding_plant1 = pg.transform.rotate(plant1_foto, 0)
        self.afbeelding_plant2 = pg.transform.rotate(plant2_foto, 0)
        self.afbeelding_plant3 = pg.transform.rotate(plant3_foto, 0)
        self.afbeelding_plant4 = pg.transform.rotate(plant4_foto, 0)
        self.animatie_tijd = -1
        self.animatie = 1
        self.show = False
        
        if self.richting == 'rechts':
            self.vx = -1
            self.vy = 0
            self.afbeelding_plant1 = pg.transform.rotate(plant1_foto, 90)
            self.afbeelding_plant2 = pg.transform.rotate(plant2_foto, 90)
            self.afbeelding_plant3 = pg.transform.rotate(plant3_foto, 90)
            self.afbeelding_plant4 = pg.transform.rotate(plant4_foto, 90)
            self.afbeelding,self.hoogte,self.breedte = genereer_stekel_afbeelding('links')
        elif self.richting == 'links':
            self.vx = 1
            self.vy = 0
            self.afbeelding_plant1 = pg.transform.rotate(plant1_foto, 270)
            self.afbeelding_plant2 = pg.transform.rotate(plant2_foto, 270)
            self.afbeelding_plant3 = pg.transform.rotate(plant3_foto, 270)
            self.afbeelding_plant4 = pg.transform.rotate(plant4_foto, 270)
            self.afbeelding,self.hoogte,self.breedte = genereer_stekel_afbeelding('rechts')
        elif self.richting == 'omlaag':
            self.vx = 0
            self.vy = 1
            self.afbeelding_plant1 = pg.transform.rotate(plant1_foto, 180)
            self.afbeelding_plant2 = pg.transform.rotate(plant2_foto, 180)
            self.afbeelding_plant3 = pg.transform.rotate(plant3_foto, 180)
            self.afbeelding_plant4 = pg.transform.rotate(plant4_foto, 180)
            self.afbeelding,self.hoogte,self.breedte = genereer_stekel_afbeelding(self.richting)
        else: #omhoog
            self.afbeelding_plant1 = pg.transform.rotate(plant1_foto, 0)
            self.afbeelding_plant2 = pg.transform.rotate(plant2_foto, 0)
            self.afbeelding_plant3 = pg.transform.rotate(plant3_foto, 0)
            self.afbeelding_plant4 = pg.transform.rotate(plant4_foto, 0)
            self.vx = 0
            self.vy = -1
            self.afbeelding,self.hoogte,self.breedte = genereer_stekel_afbeelding(self.richting)
        self.lengte = self.hoogte

    def get_code(self,last):
        if last:
            return "plant("+str(self.x)+","+str(self.y)+","+str(self.level)+",'"+str(self.richting)+"')"
        else:
            
            return "plant("+str(self.x)+","+str(self.y)+","+str(self.level)+",'"+str(self.richting)+"'),"


    def update_stekel_locatie(self,deltaTime):
        if t.perf_counter() - self.start_tijd > self.wachttijd-0.1:
            self.show = True
        if t.perf_counter() - self.start_tijd > self.wachttijd:
            self.stekel_x += self.vx/1.9 * deltaTime
            self.stekel_y += self.vy/1.9 * deltaTime
            if self.stekel_x < -25 or self.stekel_x > 1225 or self.stekel_y < -25 or self.stekel_y > 675:
                if self.richting == 'omlaag' or self.richting == 'links':
                    self.stekel_x = self.x + self.vx*25
                    self.stekel_y = self.y + self.vy*25
                else:
                    self.stekel_x = self.x
                    self.stekel_y = self.y
                self.show = False
                self.start_tijd = t.perf_counter()
        if self.emotie == 'dood':
            self.stekel_x = 10000
            self.stekel_y = 10000
            self.start_tijd = 1e8 + t.perf_counter()

    def teken(self,scherm):
        if self.show and self.emotie == 'boos':
            scherm.blit(self.afbeelding,(self.stekel_x,self.stekel_y))
        if self.emotie != 'dood':
            if self.animatie%4 == 0:
                scherm.blit(self.afbeelding_plant1,(self.x, self.y))
            elif self.animatie%4 == 1:
                scherm.blit(self.afbeelding_plant2,(self.x, self.y))
            elif self.animatie%4 == 2:
                scherm.blit(self.afbeelding_plant3,(self.x, self.y))
            else:
                scherm.blit(self.afbeelding_plant4,(self.x, self.y))

    def animatie_set(self):
        if t.perf_counter() > self.animatie_tijd + 0.3:
            self.animatie += 1
            self.animatie_tijd = t.perf_counter()


#############
#Class Whirl#
#############

class whirl:
    def __init__(self,x,y,level,groeisnelheid=1.2):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.groeisnelheid = groeisnelheid
        self.animatie_tijd = -5
        self.animatie = 1
        self.vergroot_tijd = -5
        self.breedte = 50
        self.level = level
        self.genereer_foto()
        self.dood = False
        if self.level == 0 :#boss fight
            self.groeisnelheid = 2.5

    def teken(self,scherm):
        if not self.dood:
            scherm.blit(eval('self.whirl'+str(self.animatie)+'_foto'),(self.x,self.y))
        if t.perf_counter() > self.vergroot_tijd + self.groeisnelheid:
            self.breedte += 2
            self.x -= 1
            self.y -= 1
            self.vergroot_tijd = t.perf_counter()
            self.genereer_foto()
            if self.breedte > 100 and self.level == 0:
                self.dood = True
            

    def genereer_foto(self):
        self.whirl1_foto = import_foto("Assets/Whirl-1.png",self.breedte,self.breedte)
        self.whirl2_foto = import_foto("Assets/Whirl-2.png",self.breedte,self.breedte)
        self.whirl3_foto = import_foto("Assets/Whirl-3.png",self.breedte,self.breedte)
        self.whirl4_foto = import_foto("Assets/Whirl-4.png",self.breedte,self.breedte)
        self.whirl5_foto = import_foto("Assets/Whirl-5.png",self.breedte,self.breedte)
        self.whirl6_foto = import_foto("Assets/Whirl-6.png",self.breedte,self.breedte)
        self.whirl7_foto = import_foto("Assets/Whirl-7.png",self.breedte,self.breedte)
        self.whirl8_foto = import_foto("Assets/Whirl-8.png",self.breedte,self.breedte)
        self.whirl9_foto = import_foto("Assets/Whirl-9.png",self.breedte,self.breedte)
        self.whirl10_foto = import_foto("Assets/Whirl-10.png",self.breedte,self.breedte)
        self.whirl11_foto = import_foto("Assets/Whirl-11.png",self.breedte,self.breedte)
        self.whirl12_foto = import_foto("Assets/Whirl-12.png",self.breedte,self.breedte)

    def animatie_set(self):
        if t.perf_counter() > self.animatie_tijd + 0.1:
            self.animatie += 1
            self.animatie_tijd = t.perf_counter()
            if self.animatie > 12:
                self.animatie = 1

    def get_code(self,last):
        if last:
            return "whirl("+str(self.x)+","+str(self.y)+","+str(1)+","+str(self.groeisnelheid)+")"
        else:
            
            return "whirl("+str(self.x)+","+str(self.y)+","+str(1)+","+str(self.groeisnelheid)+"),"

        
    
#####################
#Class Bewegede Muur#
#####################

class bewegende_muur(muur):
    def __init__(self,startx,starty,eindx,eindy,lengte,orientatie,tijd=3,dikte=5):
        self.x = startx
        self.y = starty
        self.startx = startx
        self.starty = starty
        self.eindx = eindx
        self.eindy = eindy
        self.start_t = t.perf_counter()
        self.orientatie = orientatie
        self.tijd = tijd
        self.kleur = (248, 243, 61)
        self.real_lengte = lengte
        if orientatie == 'staand':
            self.lengte = lengte
            self.breedte = dikte
        else: # liggend
            self.lengte = dikte
            self.breedte = lengte
        self.vx = (self.eindx-self.startx)/tijd
        self.vy = (self.eindy-self.starty)/tijd

    def beweeg(self):
        bezig_tijd = t.perf_counter()-self.start_t
        bepaal_richting = (bezig_tijd/self.tijd)%2
        if bepaal_richting < 1:
            richting = 1
            self.x = int(self.startx + (bezig_tijd%self.tijd)*richting*self.vx)
            self.y = int(self.starty + (bezig_tijd%self.tijd)*richting*self.vy)
        else:
            richting = -1
            self.x = int(self.eindx + (bezig_tijd%self.tijd)*richting*self.vx)
            self.y = int(self.eindy + (bezig_tijd%self.tijd)*richting*self.vy)

    def get_code(self,last):
        if last:
            return "bewegende_muur("+str(self.startx)+","+str(self.starty)+","+str(self.eindx)+","+str(self.eindy)+","+str(self.real_lengte)+",'"+str(self.orientatie)+"')"
        else:
            return "bewegende_muur("+str(self.startx)+","+str(self.starty)+","+str(self.eindx)+","+str(self.eindy)+","+str(self.real_lengte)+",'"+str(self.orientatie)+"'),"

############
#Class Boss#
############

class boss(geest):
    def __init__(self,x,y):
        super().__init__(x,y,0)
        self.boss = True
        self.hoogte = 128
        self.emotie = 'boos'
        self.wakker = True
        self.vx = 1
        self.vy = 1
        self.levens = 12
        self.max_levens = 12
        self.starttijd = t.perf_counter()
        self.score_lengte = 75
        self.attack = 0
        self.richting = 'omhoog'
        
    def teken(self,scherm):
        if not self.emotie == 'dood':
            scherm.blit(boss_foto,(self.x,self.y))
            pg.draw.rect(scherm,(0,255,0),((self.x+int((self.hoogte-self.score_lengte)/2),self.y+self.hoogte+10),(int(self.score_lengte*self.levens/self.max_levens),10)))
            if self.levens < self.max_levens:
                pg.draw.rect(scherm,(255,0,0),((self.x+int((self.hoogte-self.score_lengte)/2)+int(self.score_lengte*self.levens/self.max_levens),self.y+self.hoogte+10),(self.score_lengte-int(self.score_lengte*self.levens/self.max_levens),10)))

    def check_kogel(self,kogel_lijst,geest_lijst,plant_lijst,whirl_lijst):
        self.attack = 0
        for Kogel in kogel_lijst:
            if Kogel.actief:
                if self.x < Kogel.x + Kogel.breedte and self.x + self.hoogte > Kogel.x:
                    if self.y < Kogel.y + Kogel.hoogte and self.y + self.hoogte > Kogel.y:
                        self.levens -= 1
                        Kogel.actief = False
                        if self.levens > 0:
                            self.attack = r.randint(1,3)
                            if self.attack == 1:
                                if not ((self.x > 300 and self.x < 600) and (self.y > 250 and self.y < 450)):
                                    geest_lijst.append(geest(self.x+40, self.y+40,21))
                                    for geest_ in range(-1,0):
                                        geest_lijst[geest_].emotie = 'boos'
                                        geest_lijst[geest_].wakker = True
                                        geest_lijst[geest_].starttijd = t.perf_counter()
                                        
                            elif self.attack == 2:
                                if (self.x < 400 or self.x > 600) and (self.y < 250 or self.y > 450):
                                    self.attack = r.randint(1,4)
                                    if self.attack == 1:
                                        plant_lijst.append(plant(5, self.y,21,'links',3))
                                    elif self.attack == 2:
                                        plant_lijst.append(plant(self.x, 5,21,'omlaag',3))
                                    elif self.attack == 3:
                                        plant_lijst.append(plant(1145, self.y,21,'rechts',3))
                                    else:    
                                        plant_lijst.append(plant(self.x, 595,21,'omhoog',3))
                                    for plant_ in range(-1,0):
                                        plant_lijst[plant_].starttijd = t.perf_counter()
                                        plant_lijst[plant_].level = 0
                                        
                            elif self.attack == 3:
                                if not ((self.x > 300 and self.x < 600) and (self.y > 200 and self.y < 400)):
                                    whirl_lijst.append(whirl(self.x+40, self.y+40,0))
                                    
                        if self.levens == 0:
                            self.emotie = 'dood'
                            if self.attack == 0:
                                return True,kogel_lijst,geest_lijst,plant_lijst,whirl_lijst, False #je bent klaar flag!
                            else:
                                return True,kogel_lijst,geest_lijst,plant_lijst,whirl_lijst, True #je bent klaar flag!
                            
        if self.attack == 0:
            return False,kogel_lijst,geest_lijst,plant_lijst,whirl_lijst, False
        else:
            return False,kogel_lijst,geest_lijst,plant_lijst,whirl_lijst, True
        
##################################
#Class Decoratie/Class Decoration#
##################################

class decoratie:
    def __init__(self,x,y,soort):
        self.x = x
        self.y = y
        self.soort = soort

    def teken(self,scherm,level):
        if level < 11: #pyramide
            if self.soort == 1:
                scherm.blit(Dec11,(self.x,self.y))
            elif self.soort == 2:
                scherm.blit(Dec12,(self.x,self.y))
            else:
                scherm.blit(Dec13,(self.x,self.y))
        elif level < 16: #jungle
            if self.soort == 1:
                scherm.blit(Dec21,(self.x,self.y))
            elif self.soort == 2:
                scherm.blit(Dec22,(self.x,self.y))
            else:
                scherm.blit(Dec23,(self.x,self.y))
        elif level < 21: #underwater
            if self.soort == 1:
                scherm.blit(Dec31,(self.x,self.y))
            elif self.soort == 2:
                scherm.blit(Dec32,(self.x,self.y))
            else:
                scherm.blit(Dec33,(self.x,self.y))
        else:
            pass

    def get_code(self,last):         
        if last:
            return "decoratie("+str(self.x)+","+str(self.y)+","+str(self.soort)+")"
        else:
            return "decoratie("+str(self.x)+","+str(self.y)+","+str(self.soort)+"),"
                        
#############
#Class Kogel#
#############

class kogel():
    def __init__(self,x,y,richting):
        self.x = x
        self.y = y
        self.richting = richting
        self.afstand = 350
        self.actief = True
        if self.richting == 'links':
            self.vx = -3
            self.vy = 0
            self.eindx = self.x - self.afstand
            self.eindy = self.y
            self.afbeelding = pg.transform.rotate(kogel_klein_foto,90)
            self.hoogte =  25
            self.breedte = 50
        elif self.richting == 'rechts':
            self.vx = 3
            self.vy = 0
            self.eindx = self.x + self.afstand
            self.eindy = self.y
            self.afbeelding = pg.transform.rotate(kogel_klein_foto,270)
            self.hoogte =  25
            self.breedte = 50
        elif self.richting == 'omlaag':
            self.vy = 3
            self.vx = 0
            self.eindx = self.x 
            self.eindy = self.y + self.afstand
            self.afbeelding = pg.transform.rotate(kogel_klein_foto,180)
            self.hoogte =  50
            self.breedte = 25
        else: #omhoog
            self.vx = 0
            self.vy = -3
            self.eindx = self.x
            self.eindy = self.y - self.afstand
            self.afbeelding = kogel_klein_foto
            self.hoogte =  50
            self.breedte = 25


    def bewegen(self,deltaTime):
        self.x += self.vx*deltaTime/5
        self.y += self.vy*deltaTime/5
        if self.x == self.eindx and self.y == self.eindy:
            self.actief = False

    def teken(self,scherm):
        if self.actief:
            scherm.blit(self.afbeelding,(int(self.x),int(self.y)))

def genereer_kogels(Blokje,kogel_lijst):
    if Blokje.kogel > 0:
        channel_sound.play(Kogel_Schiet_Geluid)
        Blokje.kogel -= 1
        kogel_lijst.append(kogel(Blokje.x+Blokje.breedte/2,Blokje.y+Blokje.breedte/2,'omhoog'))
        kogel_lijst.append(kogel(Blokje.x+Blokje.breedte/2,Blokje.y+Blokje.breedte/2,'links'))
        kogel_lijst.append(kogel(Blokje.x+Blokje.breedte/2,Blokje.y+Blokje.breedte/2,'rechts'))
        kogel_lijst.append(kogel(Blokje.x+Blokje.breedte/2,Blokje.y+Blokje.breedte/2,'omlaag'))
        for Kogel in range(-4,0):
            kogel_lijst[Kogel].x -= int(kogel_lijst[Kogel].breedte/2)
            kogel_lijst[Kogel].eindx -= int(kogel_lijst[Kogel].breedte/2)
            kogel_lijst[Kogel].y -= int(kogel_lijst[Kogel].hoogte/2)
            kogel_lijst[Kogel].eindy -= int(kogel_lijst[Kogel].hoogte/2)
    return kogel_lijst

################
#Class Tutorial#
################

class tutorial:
    def __init__(self,x,y,tekst,tekst2='', tekst3='',tekst4='',tekst5=''):
        self.x = x
        self.y = y
        self.tekst = tekst
        self.tekst2 = tekst2
        self.tekst3 = tekst3
        self.tekst4 = tekst4
        self.tekst5 = tekst5

    def teken(self,scherm):
        tekst(scherm, self.tekst, self.x, self.y, 'tekst_groot')
        tekst(scherm, self.tekst2, self.x, self.y+30, 'tekst_groot')
        tekst(scherm, self.tekst3, self.x, self.y+60, 'tekst_groot')
        tekst(scherm, self.tekst4, self.x, self.y+90, 'tekst_groot')
        tekst(scherm, self.tekst5, self.x, self.y+120, 'tekst_groot')

def teken_raster(scherm,raster_spacing, muisx, muisy):
    for x in range(round(muisx/raster_spacing)-15,round(muisx/raster_spacing)+15):
        for y in range(round(muisy/raster_spacing)-15,round(muisy/raster_spacing)+15):
            if x%5 == 0 and y%5 == 0:
                pg.draw.line(scherm,(152,68,128),(0,y*raster_spacing),(x*raster_spacing + 1200,y*raster_spacing),2)
                pg.draw.line(scherm,(152,68,128),(x*raster_spacing,0),(x*raster_spacing,y*raster_spacing+650),2)
            else:
                pg.draw.line(scherm,(152,68,128),(0,y*raster_spacing),(x*raster_spacing + 1200,y*raster_spacing))
                pg.draw.line(scherm,(152,68,128),(x*raster_spacing,0),(x*raster_spacing,y*raster_spacing+650))

            
##############
#Muis Cursors#
##############

leeg_cursor = (               
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ")

normaal_cursor = (
  "X                       ",
  "XX                      ",
  "X.X                     ",
  "X..X                    ",
  "X...X                   ",
  "X....X                  ",
  "X.....X                 ",
  "X......X                ",
  "X.......X               ",
  "X........X              ",
  "X.........X             ",
  "X..........X            ",
  "X......XXXXX            ",
  "X...X..X                ",
  "X..X X..X               ",
  "X.X  X..X               ",
  "XX    X..X              ",
  "      X..X              ",
  "       XX               ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ")


klik_cursor = (
  "     XX                 ",
  "    X..X                ",
  "    X..X                ",
  "    X..X                ",
  "    X..X                ",
  "    X..XXX              ",
  "    X..X..XXX           ",
  "    X..X..X..XX         ",
  "    X..X..X..X.X        ",
  "XXX X..X..X..X..X       ",
  "X..XX........X..X       ",
  "X...X...........X       ",
  " X..............X       ",
  "  X.............X       ",
  "  X.............X       ",
  "   X............X       ",
  "   X...........X        ",
  "    X..........X        ",
  "    X..........X        ",
  "     X........X         ",
  "     X........X         ",
  "     XXXXXXXXXX         ",
  "                        ",
  "                        ")

    
##################################
#Overig maar toch zeer belangrijk#
##################################
        
if __name__ == '__main__':
    pg.font.quit()
    pg.quit()


#######################
#Einde: 2246ste regel!#
#######################
