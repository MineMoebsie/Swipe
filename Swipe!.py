import random as r
import time as t
import numpy as np
import pygame as pg
from Swipe_functies import *
import pdb

pg.init()
pg.font.init()
pg.display.init()

schermblit = pg.display.set_mode((1200,650),pg.RESIZABLE|pg.DOUBLEBUF)
scherm = schermblit.copy()
pg.display.flip()
#scherm = pg.display.set_mode((1200,650),pg.RESIZABLE)# ,pg.FULLSCREEN)

Blokje = blokje()
Finish = finish()
Checkpoint = checkpoint()

pg.mouse.set_visible(True)

spelen = True
richting = 'stilstand'
maximum_level = 21
maximum_vrijgespeeld_level = 1
level = 1
nieuw_level = True
menu_aan = True
geselecteerd_level = 1
menuaudio = False
geestaudio = False
speel_geestaudio = False
menu_help_aan = False
klaar = False
kogel_cooldown = -1
checkpoint_animate = False
bosslevel = 21

particle_lijst = []#location x and y, velocity x and y, timer
particle_tijd = -1

menu_scroll_x = 0

channel = pg.mixer.Channel(0)
channel.set_volume(0.1)

SwipeFoto = import_foto("Assets\SwipeFoto.png",30,30)
pg.display.set_caption("Swipe! v.1.4")
pg.display.set_icon(SwipeFoto)
deltaTime = 0

playtime = 0
menutime = 0

showtime = False
particles = True

autoplay = False
trigger_menu = False

volume = True
volume_check = False

maak_boss_particle = False
maak_power_particle = False
maak_schiet_particle = False
maak_bounce_particle = False

maak_ambient_particle = 0

maak_death_particle = [False,False,False,False,False,False,False]

maak_knop_particle = []
maak_knop_particleX = []
maak_knop_particleY = []
maak_knop_particleR = []

maak_stekel2_particle = []
maak_stekel2_particleX = []
maak_stekel2_particleY = []
maak_stekel2_particleR = []

maak_stekel3_particle = []
maak_stekel3_particleX = []
maak_stekel3_particleY = []
maak_stekel3_particleR = []

maak_blokje_particleX = [-1,-1,-1]
maak_blokje_particleY = [-1,-1,-1]
maak_blokje_particleR = ['verticaal','verticaal','verticaal']

clock = pg.time.Clock()

schermheightx, schermheighty = pg.display.get_surface().get_size()

datafiles = np.genfromtxt('Assets\datafile.txt',dtype='int',delimiter=' ')
for index in range(len(datafiles)):
    if int(datafiles[index]) > -1:
        if index == 0:
            maximum_vrijgespeeld_level = datafiles[index]
        elif index == 1:
            Blokje.kogel = datafiles[index]
        elif index == 2:
            Blokje.levens = datafiles[index]
        elif index == 3:
            Blokje.score = datafiles[index]
        elif index == 4:
            playtime = int(datafiles[index])/100
        elif index == 5:
            Blokje.vx = datafiles[index]
            Blokje.vy = datafiles[index]
        elif index == 6:
            particles = datafiles[index]
        elif index == 7:
            showtime = datafiles[index]
        elif index == 8:
            autoplay = datafiles[index]
        elif index == 9:
            volume = datafiles[index]

if particles == 1:
    particles = True
else:
    particles = False
    
if showtime == 1:
    showtime = True
else:
    showtime = False

if autoplay == 1:
    autoplay = True
else:
    autoplay = False

if volume == 1:
    volume = True
    channel.set_volume(0.1)
    set_volume(volume)
else:
    volume = False
    channel.set_volume(0.0)
    set_volume(volume)

while spelen:
    if particles:
        particle_lijst = update_particles(particle_lijst,deltaTime)
    else:
        particle_lijst = []

    
    
    if t.perf_counter() - particle_tijd > 0.45 or (level in [21] and t.perf_counter() - particle_tijd > 0.1) and particles == True:
        particle_lijst.append([[r.randint(0,1200),700],[r.randint(-1,1),r.randint(-20,-10)/10],r.randint(50,75),1])
        particle_tijd = t.perf_counter()
            
    speel_geestaudio = False
    if level == bosslevel and menu_aan == False:
        speel_geestaudio = True
    else:
        try:
            for Geest in geest_lijst:
                if Geest.emotie == 'boos' and menu_aan == False:
                    speel_geestaudio = True
        except NameError:
            pass
        
    if speel_geestaudio and geestaudio == False:
        channel.play(Boze_Geest)
        geestaudio = True
        menuaudio = False
        
    elif geestaudio == True and speel_geestaudio == False:
        geestaudio = False
        song = r.randint(1,4)
        channel.play(eval('ost'+str(song)))
    
    elif menuaudio == False and menu_aan == True:
        channel.play(Nimbus)
        menuaudio = True
    
    elif menuaudio == True and menu_aan == False:
        menuaudio = False
        song = r.randint(1,5)
        channel.play(eval('ost'+str(song)))
    
                
    if menu_aan == True:
        if trigger_menu and autoplay:
            menu_aan = False
            trigger_menu = False
        else:
            trigger_menu = False
        if geselecteerd_level > maximum_vrijgespeeld_level:
            geselecteerd_level = maximum_vrijgespeeld_level
        menutime = t.perf_counter() - playtime
        geestaudio = False
        menu(scherm,maximum_vrijgespeeld_level,geselecteerd_level,menu_scroll_x,particles,showtime,autoplay,volume)
        teken_particles(scherm,particle_lijst,geselecteerd_level)
        volume_check = volume
        menu_aan, spelen, geselecteerd_level, maximum_level, muis_type, menu_help_aan, menu_scroll_x, showtime,particles,autoplay,volume = gebruiker_input_menu(pg.event.get(), menu_aan, spelen, geselecteerd_level, level, maximum_level, menu_help_aan, schermblit, schermheightx, schermheighty, menu_scroll_x,showtime,particles,autoplay,volume)
        if volume_check != volume:
            if volume:
                channel.set_volume(0.1)
                set_volume(volume)
            else:
                channel.set_volume(0.0)
                set_volume(volume)
                
        level = geselecteerd_level
        nieuw_level = True
        data_cursor,mask_cursor = pg.cursors.compile(muis_type)
        pg.mouse.set_cursor((24,24),(0,0),data_cursor,mask_cursor)
        if menu_help_aan:
            help_menu(scherm)
                    
    else: #menu uit
        playtime = t.perf_counter() - menutime
        data_cursor,mask_cursor = pg.cursors.compile(leeg_cursor)
        pg.mouse.set_cursor((24,24),(0,0),data_cursor,mask_cursor)
        if nieuw_level == True:
            maak_boss_particle = False
            maak_power_particle = False
            maak_schiet_particle = False
            maak_bounce_particle = False
            maak_ambient_particle = 0
            maak_death_particle = [False,False,False,False,False,False,False]
            maak_knop_particle = []
            maak_knop_particleX = []
            maak_knop_particleY = []
            maak_knop_particleR = []
            maak_stekel2_particle = []
            maak_stekel2_particleX = []
            maak_stekel2_particleY = []
            maak_stekel2_particleR = []
            maak_stekel3_particle = []
            maak_stekel3_particleX = []
            maak_stekel3_particleY = []
            maak_stekel3_particleR = []
            maak_blokje_particleX = [-1,-1,-1]
            maak_blokje_particleY = [-1,-1,-1]
            maak_blokje_particleR = ['verticaal','verticaal','verticaal']
            checkpoint_animate = False
            Blokje.reset()
            knop_muur_lijst = genereer_knop_muren(level)
            muur_lijst = genereer_rand_muren()
            level_muren = genereer_level_muren(level)
            Finish.update_locatie(level)
            Checkpoint.update_locatie(level)
            bounce_point_lijst = genereer_bounce_points(level)
            geest_lijst = genereer_geesten(level)
            boss_lijst = genereer_bazen(level)
            stekel_lijst = genereer_stekels(level)
            stekel2_lijst = genereer_stekel2s(level)
            stekel3_lijst = genereer_stekel3s(level)
            stekel_lijst_rand = genereer_rand_stekels(level)
            powerup_lijst = genereer_powerups(level)
            decoratie_lijst = genereer_decoraties(level)
            bewegende_muren_lijst = genereer_bewegende_muren(level)
            plant_lijst = genereer_planten(level)
            whirl_lijst = genereer_whirls(level)
            tekst_lijst = genereer_tekst(level)
            kogel_lijst = []
            if level_muren == 5:  #geen levels meer -> einde spel
                einde_spel(scherm,schermblit)
                menu_aan = True
                continue
            for muur in level_muren:
                muur_lijst.append(muur)
            for stekel in stekel_lijst_rand:
                stekel_lijst.append(stekel)
            Blokje.x = 500
            Blokje.y = 300
            Blokje.checkx = 500
            Blokje.checky = 300
            Blokje.richting = 'stilstand'
            Blokje.laatste_richting = 'stilstand'
            if level == bosslevel:
                Blokje.boss_snelheid = True
            else:
                Blokje.boss_snelheid = False
            nieuw_level = False
            
            
        achtergrond(scherm)
        if particles:
            teken_particles(scherm,particle_lijst,level)
        menu_aan, richting, restart, vuur_kogels, showtime = gebruiker_input(pg.event.get(), Blokje.richting, schermblit,showtime,maak_bounce_particle)

        if vuur_kogels and t.perf_counter() > kogel_cooldown + 0.5:
            kogel_cooldown = t.perf_counter()
            kogel_lijst = genereer_kogels(Blokje,kogel_lijst)
            maak_schiet_particle = True

        Blokje.input(richting)
        Blokje.beweeg(deltaTime)
        
        maak_blokje_particleX[0], maak_blokje_particleY[0], maak_blokje_particleR[0] = Blokje.check_muur(muur_lijst)
        maak_blokje_particleX[1], maak_blokje_particleY[1], maak_blokje_particleR[1] = Blokje.check_muur(bewegende_muren_lijst)
        maak_bounce_particle = Blokje.check_bounce_point(bounce_point_lijst)
        
        for muur in knop_muur_lijst:
            if not muur.ingedrukt:
                maak_knop_particle.append(muur.detecteer_blokje(Blokje, True)[0])
                if particles:
                    maak_knop_particleX.append(muur.detecteer_blokje(Blokje, False)[1])
                    maak_knop_particleY.append(muur.detecteer_blokje(Blokje, False)[2])
                    maak_knop_particleR.append(muur.detecteer_blokje(Blokje, False)[3])
                maak_blokje_particleX[2], maak_blokje_particleY[2], maak_blokje_particleR[2] = Blokje.check_muur([muur])
                
        maak_death_particle[0] = Blokje.check_stekel(stekel_lijst,knop_muur_lijst)
        maak_death_particle[1] = Blokje.check_geest(geest_lijst, knop_muur_lijst)
        maak_death_particle[2] = Blokje.check_stekel2(stekel2_lijst, knop_muur_lijst)
        maak_death_particle[3] = Blokje.check_stekel2(stekel3_lijst, knop_muur_lijst) # omdat de muur en de stekel toch hetzelfde werken
        maak_death_particle[4] = Blokje.check_stekel2(plant_lijst, knop_muur_lijst)
        maak_death_particle[5] = Blokje.check_geest(boss_lijst, knop_muur_lijst)
        maak_death_particle[6] = Blokje.check_whirl(whirl_lijst)
        maak_power_particle = Blokje.check_powerup(powerup_lijst)
        
        Blokje.check_schild_en_x2()
        level, nieuw_level = Blokje.check_finish(Finish, level)
        
        if Blokje.check_checkpoint(Checkpoint):
            checkpoint_animate = True

        if checkpoint_animate:
            checkpoint_animate = Checkpoint.animate()
            
        if Blokje.levens == 0:
            maximum_vrijgespeeld_level = int((maximum_vrijgespeeld_level-1)/5)*5
            geselecteerd_level = maximum_vrijgespeeld_level
            Blokje.af(scherm,schermblit)
            pg.display.flip()
            menu_scroll_x = 0
            t.sleep(3)
            menu_aan = True
            Blokje.levens = 5
            if Blokje.kogel > 4:
                Blokje.kogel -= 5
            else:
                Blokje.kogel = 0
                
        if nieuw_level:
            if level - 1  < maximum_level:
                if level - 1  == maximum_vrijgespeeld_level:
                    maximum_vrijgespeeld_level += 1
            geselecteerd_level += 1
            trigger_menu = True
            menu_aan = True
            
        if restart == True:
            Blokje.x = 500
            Blokje.y = 300
            Blokje.reset()
            maak_death_particle = [True,True,True,True,True,True,True]
            Checkpoint.frame = 1
            Blokje.laatste_richting = 'stilstand'
            for Knop_Muur in knop_muur_lijst:
                Knop_Muur.ingedrukt = False
                Knop_Muur.uit = False
                Knop_Muur.waarschuwing_tijd = 1e8
                Knop_Muur.start_ingedrukt = 0
        
        Finish.teken(scherm)
        Checkpoint.teken(scherm)
        
        for Decoratie in decoratie_lijst:
            Decoratie.teken(scherm,level)
        for Stekel in stekel_lijst:
            Stekel.teken(scherm)
        for Muur in muur_lijst:
            Muur.teken(scherm,level)
        for Bewegende_muur in bewegende_muren_lijst:
            Bewegende_muur.beweeg()
            Bewegende_muur.teken(scherm,level)
        for Knop_Muur in knop_muur_lijst:
            Knop_Muur.teken(scherm, level)
        for Tekst in tekst_lijst:
            Tekst.teken(scherm)
        for Stekel2 in stekel2_lijst:
            maak_stekel2_particle.append(Stekel2.begin_timer(Blokje))
            dummy_var = Stekel2.teken(scherm,level,True)
            if particles:
                maak_stekel2_particleX.append(Stekel2.teken(scherm,level,False)[0])
                maak_stekel2_particleY.append(Stekel2.teken(scherm,level,False)[1])
                maak_stekel2_particleR.append(Stekel2.teken(scherm,level,False)[2])
        for Stekel3 in stekel3_lijst:
            maak_stekel3_particle.append(Stekel3.begin_timer(Blokje,'3'))
            dummy_var = Stekel3.teken(scherm,deltaTime,level,True)
            if particles:
                maak_stekel3_particleX.append(Stekel3.teken(scherm,deltaTime,level,False)[0])
                maak_stekel3_particleY.append(Stekel3.teken(scherm,deltaTime,level,False)[1])
                maak_stekel3_particleR.append(Stekel3.teken(scherm,deltaTime,level,False)[2])
        for Powerup in powerup_lijst:
            Powerup.teken(scherm)
            Powerup.animatie_set()
        for Bounce_point in bounce_point_lijst:
            Bounce_point.teken(scherm,Blokje)
        for Geest in geest_lijst:
            Geest.word_wakker(Blokje)
            Geest.bepaal_richting(Blokje)
            Geest.check_stekel(stekel_lijst)
            Geest.check_stekel2(stekel2_lijst)
            Geest.check_stekel2(stekel3_lijst)
            Geest.check_kogel(kogel_lijst)
            Geest.beweeg(level,deltaTime)
        for Boss in boss_lijst:
            Boss.bepaal_richting(Blokje)
            klaar,kogel_lijst,geest_lijst,plant_lijst,whirl_lijst,maak_boss_particle = Boss.check_kogel(kogel_lijst,geest_lijst,plant_lijst,whirl_lijst)
            Boss.beweeg(level,deltaTime)
        for Kogel in kogel_lijst:
            Kogel.bewegen(deltaTime)
            Kogel.teken(scherm)
        for Geest in geest_lijst:
            Geest.teken(scherm)
        for Whirl in whirl_lijst:
            Whirl.teken(scherm)
            Whirl.animatie_set()
        for Boss in boss_lijst:
            Boss.teken(scherm)
        for Plant in plant_lijst:
            Plant.teken(scherm)
            Plant.update_stekel_locatie(deltaTime)
            Plant.animatie_set()
            Plant.check_kogel(kogel_lijst)
            
        if True in maak_death_particle:
            if particles:
                for ykeer in range(0,11):
                    for xkeer in range(0,11):
                        particle_lijst.append([[int(Blokje.x)+xkeer*5,int(Blokje.y)+ykeer*5],[r.randint(-2,2),r.randint(-2,2)],6,2])
                        
            Blokje.dood(knop_muur_lijst,geest_lijst,boss_lijst,whirl_lijst)
            if particles:
                for ykeer in range(0,6):
                    for xkeer in range(0,6):
                        particle_lijst.append([[int(Blokje.x)+xkeer*10,int(Blokje.y)+ykeer*10],[r.randint(-4,4),r.randint(-4,4)],9,1])
            maak_death_particle = [False,False,False,False,False,False,False]
            
        if particles:
            maak_ambient_particle += 1
            if maak_ambient_particle > 10:
                particle_lijst.append([[int(Blokje.x)+r.randint(0,50),int(Blokje.y)+r.randint(0,50)],[r.randint(-100,100)/100,r.randint(-100,100)/100],5,5])
                maak_ambient_particle = 0
                
            if maak_boss_particle == True and particles == True:
                for keer in range(1,25):
                    particle_lijst.append([[int(Boss.x)+r.randint(0,128),int(Boss.y)+r.randint(0,128)],[r.randint(-4,4),r.randint(-4,4)],30,2])
                maak_boss_particle == False

            if maak_power_particle == True and particles == True:
                for keer in range(1,15):
                    particle_lijst.append([[int(Blokje.x)+r.randint(0,50),int(Blokje.y)+r.randint(0,50)],[r.randint(-4,4),r.randint(-4,4)],15,4])
                maak_power_particle == False

            if maak_schiet_particle == True and particles == True:
                for keer in range(1,20):
                    particle_lijst.append([[int(Blokje.x)+r.randint(0,50),int(Blokje.y)+r.randint(0,50)],[r.randint(-4,4),r.randint(-4,4)],10,5])
                maak_schiet_particle = False
            
            if True in maak_knop_particle and particles == True:
                for particle_item in range(len(maak_knop_particle)):
                    if maak_knop_particleX[particle_item] > 0:
                        if maak_knop_particleR[particle_item] == 'liggend':
                            for keer in range(0,8):
                                particle_lijst.append([[maak_knop_particleX[particle_item]+r.randint(0,15),maak_knop_particleY[particle_item]+r.randint(0,50)],[r.randint(-50,50)/10,r.randint(-1,1)],9,5])
                        else:
                            for keer in range(0,8):
                                particle_lijst.append([[maak_knop_particleX[particle_item]+r.randint(0,50),maak_knop_particleY[particle_item]+r.randint(0,15)],[r.randint(-1,1),r.randint(-50,50)/10],9,5])
      
            maak_knop_particle = []
            maak_knop_particleX = []
            maak_knop_particleY = []
            maak_knop_particleR = []
            
            if True in maak_stekel2_particle and particles == True:
                for particle_item in range(len(maak_stekel2_particle)):
                    if maak_stekel2_particle[particle_item] > 0:
                        if maak_stekel2_particleR[particle_item] in ['rechts','links']:
                            for keer in range(0,25):
                                particle_lijst.append([[maak_stekel2_particleX[particle_item]+r.randint(0,25),maak_stekel2_particleY[particle_item]+r.randint(0,50)],[r.randint(-50,50)/7,r.randint(-50,50)/10],9,6])
                        else:
                            for keer in range(0,25):
                                particle_lijst.append([[maak_stekel2_particleX[particle_item]+r.randint(0,50),maak_stekel2_particleY[particle_item]+r.randint(0,25)],[r.randint(-50,50)/10,r.randint(-50,50)/7],9,6])
      
            maak_stekel2_particle = []
            maak_stekel2_particleX = []
            maak_stekel2_particleY = []
            maak_stekel2_particleR = []

            if True in maak_stekel3_particle and particles == True:
                for particle_item in range(len(maak_stekel3_particle)):
                    if maak_stekel3_particle[particle_item] > 0:
                        if maak_stekel3_particleR[particle_item] in ['rechts','links']:
                            for keer in range(0,25):
                                particle_lijst.append([[maak_stekel3_particleX[particle_item]+r.randint(0,25),maak_stekel3_particleY[particle_item]+r.randint(0,50)],[r.randint(-50,50)/7,r.randint(-50,50)/10],9,6])
                        else:
                            for keer in range(0,25):
                                particle_lijst.append([[maak_stekel3_particleX[particle_item]+r.randint(0,50),maak_stekel3_particleY[particle_item]+r.randint(0,25)],[r.randint(-50,50)/10,r.randint(-50,50)/7],9,6])
      
            maak_stekel3_particle = []
            maak_stekel3_particleX = []
            maak_stekel3_particleY = []
            maak_stekel3_particleR = []
            
            if particles == True:
                for particle_item in range(0,3):
                    if maak_blokje_particleX[particle_item] > 0: #is particle aanwezig
                        if maak_blokje_particleR[particle_item] == 'verticaal':
                            for keer in range(0,4):
                                particle_lijst.append([[maak_blokje_particleX[particle_item],maak_blokje_particleY[particle_item]],[r.randint(-1,1),r.randint(-2,2)],6,3])
                        else:
                            for keer in range(0,4):
                                particle_lijst.append([[maak_blokje_particleX[particle_item],maak_blokje_particleY[particle_item]],[r.randint(-2,2),r.randint(-1,1)],6,3])
                
        score_maken(scherm,Blokje.score)
        levens_maken(scherm,Blokje.levens)
        kogels_maken(scherm,Blokje.kogel)

        Blokje.teken(scherm,level)   

        if klaar == True and level == bosslevel:
            einde_spel(scherm,schermblit)
            menu_aan = True

    if showtime:
        tekst(scherm, str(round(playtime,2)), 10,610, 'tekst_groot')

    if t.perf_counter() < kogel_cooldown + 0.5:
         tekst(scherm, str(round(kogel_cooldown - t.perf_counter() + 0.5,2)), 1140,35, 'tekst_groot')

    deltaTime = clock.tick(360)
    if schermblit.get_width() == 1200 and schermblit.get_height() == 650:
        schermblit.blit(scherm, (0, 0))
    else:
        schermblit.blit(pg.transform.scale(scherm, schermblit.get_rect().size).convert(), (0, 0))
    pg.display.flip()
    schermheightx, schermheighty = pg.display.get_surface().get_size()

#save file
datafile = open('Assets\datafile.txt','w')
if particles:
    particles = 1
else:
    particles = 0
if showtime:
    showtime = 1
else:
    showtime = 0
if autoplay:
    autoplay = 1
else:
    autoplay = 0
if volume:
    volume = 1
else:
    volume = 0
datafile.write(str(maximum_vrijgespeeld_level)+' '+str(Blokje.kogel)+' '+str(Blokje.levens)+' '+str(Blokje.score)+' '+str(playtime*100)+' '+str(Blokje.vx)+' '+str(particles)+' '+str(showtime)+' '+str(autoplay)+' '+str(volume))
datafile.close()

pg.display.quit()        
pg.font.quit()
pg.quit()
