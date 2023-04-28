import random as r
import time as t
import numpy as np
import pygame as pg
from Swipe_functies import *
import pdb
import sys

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

channel = pg.mixer.Channel(0)
channel.set_volume(0.1)

SwipeFoto = import_foto("Assets\SwipeFoto.png",30,30)
pg.display.set_caption("Swipe! EDITOR - v.1.4")
pg.display.set_icon(SwipeFoto)
deltaTime = 0

playtime = 0
menutime = 0
showtime = False

brush = ''
brush_orientation = 'liggend'
brush_richting = 'omhoog'
brush_powerup_type = ''
brush_length = 50
brush_distance = 250
brush_wall_x = 250
brush_wall_y = 250
brush_deco_type = 1

enter_key = False

move_lijst = [False,False,False,False,False,False,False,False] #m,n, b,v, i,j,k,l

toggle_raster = False

clock = pg.time.Clock()

schermheightx, schermheighty = pg.display.get_surface().get_size()

Blokje.kogel = 100000
Blokje.levens = 100000
Blokje.score = 100000
maximum_vrijgespeeld_level = 20
maximum_level = 20

menu_scroll_x = 0

muur_lijst = []
level_muren = []
geest_lijst = []
boss_lijst = []
stekel_lijst = []
stekel2_lijst = []
stekel3_lijst = []
stekel_lijst_rand = []
powerup_lijst = []
decoratie_lijst = []
bewegende_muren_lijst = []
plant_lijst = []
whirl_lijst = []
knop_muur_lijst = []
bounce_point_lijst = []
            
def gebruiker_input_editor(enter_key,event_rij, richting, schermblit,showtime,toggle_raster,brush,brush_orientation,brush_richting,brush_powerup_type,brush_length,brush_distance,brush_wall_x,brush_wall_y,move_lijst,brush_deco_type,check_bounce_point):
    # geeft terug: (menu_aan, richting, restart, kogels_afvuren,show time)
    muisx = 0
    muisy = 0
    key_escape = False
    key_restart = False
    key_shoot = False
    key_richting = richting

    #m,n, b,v, i,j,k,l :D
    
    for e in event_rij:
        screenwidth, screenheight = pg.display.get_surface().get_size()
        if e.type == pg.VIDEORESIZE:
            schermblit = pg.display.set_mode(e.size,pg.RESIZABLE|pg.DOUBLEBUF)

        if e.type == pg.KEYUP:
            if e.key == pg.K_m:
                move_lijst[0] = False
            if e.key == pg.K_n:
                move_lijst[1] = False
            if e.key == pg.K_v:
                move_lijst[2] = False
            if e.key == pg.K_b:
                move_lijst[3] = False
            if e.key == pg.K_i:
                move_lijst[4] = False
            if e.key == pg.K_j:
                move_lijst[5] = False
            if e.key == pg.K_k:
                move_lijst[6] = False
            if e.key == pg.K_l:
                move_lijst[7] = False
                
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_m:
                move_lijst[0] = True
            if e.key == pg.K_n:
                move_lijst[1] = True
            if e.key == pg.K_v:
                move_lijst[2] = True
            if e.key == pg.K_b:
                move_lijst[3] = True
            if e.key == pg.K_i:
                move_lijst[4] = True
            if e.key == pg.K_j:
                move_lijst[5] = True
            if e.key == pg.K_k:
                move_lijst[6] = True
            if e.key == pg.K_l:
                move_lijst[7] = True
                
            if e.key == pg.K_r:
                pg.event.pump()
                if brush_orientation == 'liggend':
                    brush_orientation = 'staand'
                else:
                    brush_orientation = 'liggend'
                        
                if brush_richting == 'omhoog':
                    brush_richting = 'rechts'
                elif brush_richting == 'rechts':
                    brush_richting = 'omlaag'
                elif brush_richting == 'omlaag':
                    brush_richting = 'links'
                else:
                    brush_richting = 'omhoog'
                    
            if e.key == pg.K_0:
                pg.event.pump()
                brush = ''
                brush_orientation = 'liggend'
                brush_richting = 'omhoog'
                brush_powerup_type = ''
                brush_length = 55
                
            if e.key == pg.K_1:
                pg.event.pump()
                brush = 'muur'
                if brush_orientation == 'liggend':
                    brush_orientation = 'staand'
                else:
                    brush_orientation = 'liggend'
                    
            if e.key == pg.K_2:
                pg.event.pump()
                if brush == 'stekels':
                    brush = 'stekel2'
                elif brush == 'stekel2':
                    brush = 'stekel3'
                elif brush == 'stekel3':
                    brush = 'stekels'
                else:
                    brush = 'stekels'

            if e.key == pg.K_3:
                pg.event.pump()
                brush = 'powerup'
                if brush_powerup_type == 'Munt':
                    brush_powerup_type = 'Muntx2'
                elif brush_powerup_type == 'Muntx2':
                    brush_powerup_type = 'Hartje'
                elif brush_powerup_type == 'Hartje':
                    brush_powerup_type = 'Versnelling'
                elif brush_powerup_type == 'Versnelling':
                    brush_powerup_type = 'Schild'
                elif brush_powerup_type == 'Schild':
                    brush_powerup_type = 'Kogel'
                elif brush_powerup_type == 'Kogel':
                    brush_powerup_type = 'Munt'
                else:
                    brush_powerup_type = 'Munt'
               
            if e.key == pg.K_4:
                pg.event.pump()
                if brush == 'geest':
                    brush = 'plant'
                elif brush == 'plant':
                    brush = 'whirl'
                elif brush == 'whirl':
                    brush = 'geest'
                else:
                    brush = 'geest'
             
            if e.key == pg.K_5:
                pg.event.pump()
                if brush == 'bewegende muur':
                    brush = 'knop muur'
                elif brush == 'knop muur':
                    brush = 'bewegende muur'
                else:
                    brush = 'bewegende muur'

            if e.key == pg.K_6:
                pg.event.pump()
                brush = 'decoratie'
                if brush_deco_type < 3:
                    brush_deco_type += 1
                elif brush_deco_type == 3:
                    brush_deco_type = 1
                else:
                    brush_deco_type = 1

            if e.key == pg.K_7:
                pg.event.pump()
                if brush == 'finish':
                    brush = 'checkpoint'
                elif brush == 'checkpoint':
                    brush = 'finish'
                else:
                    brush = 'finish'

            if e.key == pg.K_8:
                brush = 'bounce point'
                
            if e.key == pg.K_ESCAPE:
                pg.event.pump()
                key_escape = True
                
            if e.key == pg.K_q:
                pg.event.pump()
                key_restart = True

            if e.key == pg.K_t:
                pg.event.pump()
                if toggle_raster:
                    toggle_raster = False
                else:
                    toggle_raster = True
               
            if richting == 'stilstand' or check_bounce_point:
                if e.key == pg.K_LEFT or e.key == pg.K_a:
                    pg.event.pump()
                    key_richting = 'links'
                    
                if e.key == pg.K_RIGHT or e.key == pg.K_d:
                    pg.event.pump()
                    key_richting = 'rechts'
                    
                if e.key == pg.K_UP or e.key == pg.K_w:
                    pg.event.pump()
                    key_richting = 'omhoog'
                    
                if e.key == pg.K_DOWN or e.key == pg.K_s:
                    pg.event.pump()
                    key_richting = 'omlaag'
                
                    
            if e.key == pg.K_SPACE:
                pg.event.pump()
                key_shoot = True


        
        if e.type == pg.MOUSEBUTTONDOWN:
            muisx,muisy = pg.mouse.get_pos()
            muisx = muisx*(1200/screenwidth)
            muisy = muisy*(650/screenheight)
            muisx = round(muisx/5)*5
            muisy = round(muisy/5)*5

            
    pg.event.pump()
    if move_lijst[0] == True and enter_key:
        if not brush_length > 600:
              brush_length += 5

    if move_lijst[1] == True and enter_key:
         if not brush_length < 5:
              brush_length -= 5
                
    if move_lijst[2] == True and enter_key:
          if not brush_distance < 5:
               brush_distance -= 5
                
    if move_lijst[3] == True and enter_key:
          if not brush_distance > 600:
              brush_distance += 5

    if move_lijst[4] == True and enter_key:
        if not brush_wall_y < 5:
              brush_wall_y -= 5

    if move_lijst[5] == True and enter_key:
          if not brush_wall_x < 5:
              brush_wall_x -= 5
                
    if move_lijst[6] == True and enter_key:
         if not brush_wall_y > 645:
              brush_wall_y += 5
                
    if move_lijst[7] == True and enter_key:
        if not brush_wall_x > 1195:
            brush_wall_x += 5
            
    return key_escape, key_richting, key_restart,key_shoot,showtime,muisx,muisy,toggle_raster,brush,brush_orientation,brush_richting,brush_powerup_type,brush_length,brush_distance,brush_wall_x,brush_wall_y,move_lijst,brush_deco_type

while spelen:
    speel_geestaudio = False
    if level == 21 and menu_aan == False:
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
        if r.randint(1,3) == 1:
            channel.play(ost1)
        else:
            song = r.randint(1,4)
            if song == 1:
                channel.play(ost2)
            elif song == 2:
                channel.play(ost3)
            elif song == 3:
                channel.play(ost4)
            else:
                channel.play(ost5)
    
    elif menuaudio == False and menu_aan == True:
        channel.play(Nimbus)
        menuaudio = True
    
    elif menuaudio == True and menu_aan == False:
        menuaudio = False
        if r.randint(1,3) == 1:
            channel.play(ost1)
        else:
            song = r.randint(1,4)
            if song == 1:
                channel.play(ost2)
            elif song == 2:
                channel.play(ost3)
            elif song == 3:
                channel.play(ost4)
            else:
                channel.play(ost5)
                
    if menu_aan == True:
        if geselecteerd_level > maximum_vrijgespeeld_level:
            geselecteerd_level = maximum_vrijgespeeld_level
        menutime = t.perf_counter() - playtime
        geestaudio = False
        menu(scherm,maximum_vrijgespeeld_level,geselecteerd_level,menu_scroll_x,False,False,False,False)
        menu_aan, spelen, geselecteerd_level, maximum_level, muis_type, menu_help_aan,menu_scroll_x,showtime,dummy_var,dummy_var1,dummy_var2 = gebruiker_input_menu(pg.event.get(), menu_aan, spelen, geselecteerd_level, level, maximum_level, menu_help_aan, schermblit, schermheightx, schermheighty,menu_scroll_x,showtime, False,False,False)
        level = geselecteerd_level
        nieuw_level = True
        data_cursor,mask_cursor = pg.cursors.compile(muis_type)
        pg.mouse.set_cursor((24,24),(0,0),data_cursor,mask_cursor)
        if menu_help_aan:
            help_menu(scherm)
                    
    else: #menu uit
        if enter_key:
            enter_key = False
        else:
            enter_key = True
            
        playtime = t.perf_counter() - menutime
        data_cursor,mask_cursor = pg.cursors.compile(normaal_cursor)
        pg.mouse.set_cursor((24,24),(0,0),data_cursor,mask_cursor)
        if nieuw_level == True:
            checkpoint_animate = False
            Blokje.reset()
            knop_muur_lijst = genereer_knop_muren(level)
            muur_lijst = genereer_rand_muren()
            level_muren = genereer_level_muren(level)
            Finish.update_locatie(level)
            Checkpoint.update_locatie(level)
            geest_lijst = genereer_geesten(level)
            boss_lijst = genereer_bazen(level)
            stekel_lijst = genereer_stekels(level)
            stekel2_lijst = genereer_stekel2s(level)
            stekel3_lijst = genereer_stekel3s(level)
            whirl_lijst = genereer_whirls(level)
            stekel_lijst_rand = genereer_rand_stekels(level)
            powerup_lijst = genereer_powerups(level)
            decoratie_lijst = genereer_decoraties(level)
            bewegende_muren_lijst = genereer_bewegende_muren(level)
            bounce_point_lijst = genereer_bounce_points(level)
            hover_lijst = []
            plant_lijst = genereer_planten(level)
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
            nieuw_level = False
        achtergrond(scherm)
        menu_aan, richting, restart,vuur_kogels,showtime,objectx,objecty,toggle_raster,brush,brush_orientation,brush_richting,brush_powerup_type,brush_length,brush_distance,brush_wall_x,brush_wall_y,move_lijst,brush_deco_type = gebruiker_input_editor(enter_key,pg.event.get(), Blokje.richting, schermblit,showtime,toggle_raster,brush,brush_orientation,brush_richting,brush_powerup_type,brush_length,brush_distance,brush_wall_x,brush_wall_y,move_lijst,brush_deco_type,Blokje.check_bounce_point(bounce_point_lijst))

        if objectx > 0 and objecty > 0:
            if brush == '':# gummy :)
                index_delete, delete_item = check_object(objectx,objecty,muur_lijst,stekel_lijst,stekel2_lijst,stekel3_lijst,powerup_lijst,geest_lijst,plant_lijst,whirl_lijst,bewegende_muren_lijst,knop_muur_lijst,decoratie_lijst,bounce_point_lijst)
                if delete_item == 'muur':
                    muur_lijst.pop(index_delete)
                elif delete_item == 'stekel':
                    stekel_lijst.pop(index_delete)
                elif delete_item == 'stekel2':
                    stekel2_lijst.pop(index_delete)
                elif delete_item == 'stekel3':
                    stekel3_lijst.pop(index_delete)
                elif delete_item == 'powerup':
                    powerup_lijst.pop(index_delete)
                elif delete_item == 'geest':
                    geest_lijst.pop(index_delete)
                elif delete_item == 'plant':
                    plant_lijst.pop(index_delete)
                elif delete_item == 'whirl':
                    whirl_lijst.pop(index_delete)
                elif delete_item == 'bewegende muur':
                    bewegende_muren_lijst.pop(index_delete)
                elif delete_item == 'knop muur':
                    knop_muur_lijst.pop(index_delete)
                elif delete_item == 'decoratie':
                    knop_muur_lijst.pop(index_delete)
                    
            elif brush == 'muur':
                if not check_object_existance(muur_lijst,'muur',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    muur_lijst.append(genereer_object('muur',objectx,objecty,brush_length,brush_orientation))
                else:
                    muur_lijst.pop(check_object_existance_index(muur_lijst,'muur',objectx,objecty,brush_richting,brush_length,brush_orientation))
            elif brush == 'stekels':
                if not check_object_existance(stekel_lijst,'stekel',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    stekel_lijst.append(genereer_object('stekels',objectx,objecty,brush_length,brush_orientation,brush_richting))
                else:
                    stekel_lijst.pop(check_object_existance_index(stekel_lijst,'stekel',objectx,objecty,brush_richting,brush_length,brush_orientation))
            elif brush == 'stekel2':
                if not check_object_existance(stekel2_lijst,'stekel2',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    stekel2_lijst.append(genereer_object('stekel2',objectx,objecty,brush_length,brush_orientation,brush_richting))
                else:
                    stekel2_lijst.pop(check_object_existance_index(stekel2_lijst,'stekel2',objectx,objecty,brush_richting,brush_length,brush_orientation))
            elif brush == 'stekel3':
                if not check_object_existance(stekel3_lijst,'stekel3',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    stekel3_lijst.append(genereer_object('stekel3',objectx,objecty,brush_length,brush_orientation,brush_richting))
                else:
                    stekel3_lijst.pop(check_object_existance_index(stekel3_lijst,'stekel3',objectx,objecty,brush_richting,brush_length,brush_orientation))
            elif brush == 'powerup':
                if not check_object_existance(powerup_lijst,'powerup',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    powerup_lijst.append(genereer_object('powerup',objectx,objecty,brush_length,brush_orientation,brush_richting,brush_powerup_type))
                else:
                    powerup_lijst.pop(check_object_existance_index(powerup_lijst,'powerup',objectx,objecty,brush_richting,brush_length,brush_orientation))
            elif brush == 'geest':
                if not check_object_existance(geest_lijst,'geest',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    geest_lijst.append(genereer_object('geest',objectx,objecty,brush_length,brush_orientation,brush_richting))
                else:
                    geest_lijst.pop(check_object_existance_index(geest_lijst,'geest',objectx,objecty,brush_richting,brush_length,brush_orientation))
            elif brush == 'plant':
                if not check_object_existance(plant_lijst,'plant',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    plant_lijst.append(genereer_object('plant',objectx,objecty,brush_length,brush_orientation,brush_richting))
                else:
                    plant_lijst.pop(check_object_existance_index(plant_lijst,'plant',objectx,objecty,brush_richting,brush_length,brush_orientation))

            elif brush == 'whirl':
                if not check_object_existance(whirl_lijst,'whirl',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    whirl_lijst.append(genereer_object('whirl',objectx,objecty,brush_length,brush_orientation,brush_richting))
                else:
                    whirl_lijst.pop(check_object_existance_index(whirl_lijst,'whirl',objectx,objecty,brush_richting,brush_length,brush_orientation))
           
            elif brush == 'bewegende muur':
                bewegende_muren_lijst.append(genereer_object('bewegende muur',objectx,objecty,brush_length,brush_orientation,brush_richting,brush_powerup_type,brush_distance))
                
            elif brush == 'knop muur':
                knop_muur_lijst.append(genereer_object('knop muur',objectx,objecty,brush_length,brush_orientation,brush_richting,brush_powerup_type,brush_distance,brush_wall_x,brush_wall_y))

            elif brush == 'decoratie':
                if not check_object_existance(decoratie_lijst,'decoratie',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    decoratie_lijst.append(genereer_object('decoratie',objectx,objecty,brush_length,brush_orientation,brush_richting,brush_powerup_type,brush_distance,brush_wall_x,brush_wall_y,brush_deco_type))
                else:
                    decoratie_lijst.pop(check_object_existance_index(decoratie_lijst,'decoratie',objectx,objecty,brush_richting,brush_length,brush_orientation))

            elif brush == 'finish':
                Finish.x = objectx
                Finish.y = objecty

            elif brush == 'checkpoint':
                Checkpoint.x = objectx
                Checkpoint.y = objecty

            elif brush == 'bounce point':
                if not check_object_existance(bounce_point_lijst,'bounce point',objectx,objecty,brush_richting,brush_length,brush_orientation):
                    bounce_point_lijst.append(genereer_object('bounce point',objectx,objecty,brush_length,brush_orientation,brush_richting,brush_powerup_type,brush_distance,brush_wall_x,brush_wall_y,brush_deco_type))
                else:
                    bounce_point_lijst.pop(check_object_existance_index(bounce_point_lijst,'bounce point',objectx,objecty,brush_richting,brush_length,brush_orientation))


                
        if vuur_kogels and t.perf_counter() > kogel_cooldown + 0.5:
            kogel_cooldown = t.perf_counter()
            kogel_lijst = genereer_kogels(Blokje,kogel_lijst)

        
        Blokje.input(richting)
        Blokje.check_muur(muur_lijst)
        Blokje.check_muur(bewegende_muren_lijst)
        for muur in knop_muur_lijst:
            if not muur.ingedrukt:
                muur.detecteer_blokje(Blokje,True)
                Blokje.check_muur([muur])
        Blokje.check_stekel(stekel_lijst,knop_muur_lijst)
        Blokje.check_geest(geest_lijst, knop_muur_lijst)
        Blokje.check_stekel2(stekel2_lijst, knop_muur_lijst)
        Blokje.check_stekel2(stekel3_lijst, knop_muur_lijst) # omdat de muur en de stekel toch hetzelfde werken
        Blokje.check_stekel2(plant_lijst, knop_muur_lijst)
        Blokje.check_whirl(whirl_lijst)
        Blokje.check_powerup(powerup_lijst)
        Blokje.check_schild_en_x2()
        Blokje.check_geest(boss_lijst, knop_muur_lijst)
        level, nieuw_level = Blokje.check_finish(Finish, level)

        if Blokje.check_checkpoint(Checkpoint):
            checkpoint_animate = True
        if checkpoint_animate:
            checkpoint_animate = Checkpoint.animate()
            
        if Blokje.levens == 0:
            maximum_vrijgespeeld_level = 1
            geselecteerd_level = 1
            Blokje.af(scherm,schermblit)
            pg.display.flip()
            t.sleep(3)
            menu_aan = True
            Blokje.levens = 3

        if level == 16:
            Blokje.vx = 2
            Blokje.vy = 2
            
        if nieuw_level:
            if level - 1  < maximum_level:
                if level - 1  == maximum_vrijgespeeld_level:
                    maximum_vrijgespeeld_level += 1
            geselecteerd_level += 1
            menu_aan = True
            
        if restart == True:
            Blokje.x = 500
            Blokje.y = 300
            Blokje.laatste_richting = 'stilstand'
            Blokje.reset()
            Checkpoint.frame = 1
            for Knop_Muur in knop_muur_lijst:
                Knop_Muur.ingedrukt = False
                Knop_Muur.uit = False
                Knop_Muur.waarschuwing_tijd = 1e8
                Knop_Muur.start_ingedrukt = 0
                
        Blokje.beweeg(deltaTime)
        
        Finish.teken(scherm)
        Checkpoint.teken(scherm)

        for Bounce_point in bounce_point_lijst:
            Bounce_point.teken(scherm,Blokje)
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
            Knop_Muur.teken(scherm,level)
        for Tekst in tekst_lijst:
            Tekst.teken(scherm)
        for Stekel2 in stekel2_lijst:
            Stekel2.begin_timer(Blokje)
            Stekel2.teken(scherm,level,True)
        for Stekel3 in stekel3_lijst:
            Stekel3.begin_timer(Blokje,'3')
            Stekel3.teken(scherm,deltaTime,level,True)
        for Powerup in powerup_lijst:
            Powerup.teken(scherm)
            Powerup.animatie_set()
        for Geest in geest_lijst:
            Geest.word_wakker(Blokje)
            Geest.bepaal_richting(Blokje)
            Geest.check_stekel(stekel_lijst)
            Geest.check_stekel2(stekel2_lijst)
            Geest.check_stekel2(stekel3_lijst)
            Geest.check_kogel(kogel_lijst)
            Geest.beweeg(level,deltaTime)
        for Boss in boss_lijst:
            #Boss.word_wakker(Blokje)
            Boss.bepaal_richting(Blokje)
            klaar,kogel_lijst,geest_lijst,plant_lijst = Boss.check_kogel(kogel_lijst,geest_lijst,plant_lijst)
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
            
        score_maken(scherm,Blokje.score)
        levens_maken(scherm,Blokje.levens)
        kogels_maken(scherm,Blokje.kogel)

        Blokje.teken(scherm,level)
            
        if showtime:
            tekst(scherm, str(round(playtime,2)), 10,610, 'tekst_groot')

        if t.perf_counter() < kogel_cooldown + 0.5:
             tekst(scherm, str(round(kogel_cooldown - t.perf_counter() + 0.5,2)), 1140,35, 'tekst_groot')

        screenwidth, screenheight = schermblit.get_size()
        muisx,muisy = pg.mouse.get_pos()
        muisx = muisx*(1200/screenwidth)
        muisy = muisy*(650/screenheight)
        muisx = round(muisx/5)*5
        muisy = round(muisy/5)*5
        
        if brush == 'muur':
            if brush_orientation == 'liggend':
                pg.draw.rect(scherm,(222, 61, 24),((muisx,muisy),(brush_length,5)))
            else:
                pg.draw.rect(scherm,(222, 61, 24),((muisx,muisy),(5,brush_length)))
                
        elif brush == 'stekels':
            stekels_foto_hover,hoogte,breedte = genereer_stekel_afbeelding(brush_richting)
            scherm.blit(stekels_foto_hover,(muisx,muisy))
            
        elif brush == 'stekel2':
            if brush_richting == 'omhoog':
                hoogte = 25
                breedte = 50
                lijn_x = muisx
                lijn_y = muisy
            elif brush_richting == 'links':
                hoogte = 50
                breedte = 25
                lijn_x = muisx
                lijn_y = muisy
            elif brush_richting == 'rechts':
                hoogte = 50
                breedte = 25
                lijn_y = muisy
                lijn_x = muisx + breedte - 5
            else: # omlaag
                hoogte = 25
                breedte = 50
                lijn_y = muisy + hoogte - 5
                lijn_x = muisx
                
            pg.draw.rect(scherm,(248,243,61), ((muisx,muisy),(breedte, hoogte)))
            
            if brush_richting in ['links','rechts']:
                pg.draw.rect(scherm,(2, 242, 242),((lijn_x,lijn_y),(5,hoogte)))
            else: #omhoog,omlaag
                pg.draw.rect(scherm,(2, 242, 242),((lijn_x,lijn_y),(breedte,5)))
        elif brush == 'stekel3':
            if brush_richting == 'omhoog':
                hoogte = 25
                breedte = 50
            elif brush_richting == 'links':
                hoogte = 50
                breedte = 25
            elif brush_richting == 'rechts':
                hoogte = 50
                breedte = 25
            else: # omlaag
                hoogte = 25
                breedte = 50
                
            knop_grootte = 10
            lengte = hoogte
            if brush_richting == 'omhoog':
                knop_x = muisx + (breedte-knop_grootte) / 2
                knop_y = muisy - knop_grootte
            elif brush_richting == 'links':
                knop_x = muisx - knop_grootte
                knop_y = muisy + (lengte-knop_grootte) / 2
            elif brush_richting == 'omlaag':
                knop_x = muisx + (breedte-knop_grootte) / 2
                knop_y = muisy + lengte
            else: #rechts
                knop_x = muisx + breedte
                knop_y = muisy + (lengte-knop_grootte) / 2

            pg.draw.rect(scherm,(248,243,61), ((muisx,muisy),(breedte, hoogte)))
            pg.draw.rect(scherm,(255,0,0),((knop_x,knop_y),(knop_grootte,knop_grootte)))
            
        elif brush == 'powerup':
            if brush_powerup_type == 'Munt':
                scherm.blit(munt1_foto,(muisx+5,muisy+5))
            elif brush_powerup_type == 'Muntx2':
                scherm.blit(muntx21_foto,(muisx+5,muisy+5))
            elif brush_powerup_type == 'Hartje':
                scherm.blit(hartje1_foto,(muisx+5,muisy+5))
            elif brush_powerup_type == 'Versnelling':
                scherm.blit(versnelling1_foto,(muisx+5,muisy+5))
            elif brush_powerup_type == 'Schild':
                scherm.blit(schild1_foto,(muisx+5,muisy+5))
            else:
                scherm.blit(kogel1_foto,(muisx+5,muisy+5))

        elif brush == 'geest':
            scherm.blit(geest_neutraal_foto,(muisx,muisy))
            
        elif brush == 'plant':
            if brush_richting == 'omhoog':
                afbeelding_plant1 = pg.transform.rotate(plant1_foto, 0)
            elif brush_richting == 'rechts':
                afbeelding_plant1 = pg.transform.rotate(plant1_foto, 90)
            elif brush_richting == 'omlaag':
                afbeelding_plant1 = pg.transform.rotate(plant1_foto, 180)
            else:
                afbeelding_plant1 = pg.transform.rotate(plant1_foto, 270)
            scherm.blit(afbeelding_plant1,(muisx,muisy))

        elif brush == 'whirl':
            scherm.blit(whirl11_foto,(muisx,muisy))
            
        elif brush == 'bewegende muur':
            if brush_orientation == 'liggend':
                pg.draw.rect(scherm,(222, 61, 24),((muisx,muisy),(brush_length,5)))
                pg.draw.rect(scherm,(222, 61, 24),((muisx+brush_distance,muisy),(brush_length,5)))
            else:
                pg.draw.rect(scherm,(222, 61, 24),((muisx,muisy),(5,brush_length)))
                pg.draw.rect(scherm,(222, 61, 24),((muisx,muisy+brush_distance),(5,brush_length)))

        elif brush == 'knop muur':
            pg.draw.rect(scherm,(255,0,0),((muisx,muisy),(10,10)))
            if brush_orientation == 'liggend':
                pg.draw.rect(scherm,(255,0,0),((brush_wall_x,brush_wall_y),(brush_length,5)))
            else:
                pg.draw.rect(scherm,(255,0,0),((brush_wall_x,brush_wall_y),(5,brush_length)))

        elif brush == 'decoratie':
            if level < 11: #pyramide
                if brush_deco_type == 1:
                    scherm.blit(Dec11,(muisx,muisy))
                elif brush_deco_type == 2:
                    scherm.blit(Dec12,(muisx,muisy))
                else:
                    scherm.blit(Dec13,(muisx,muisy))
            elif level < 16: #jungle
                if brush_deco_type == 1:
                    scherm.blit(Dec21,(muisx,muisy))
                elif brush_deco_type == 2:
                    scherm.blit(Dec22,(muisx,muisy))
                else:
                    scherm.blit(Dec23,(muisx,muisy))
            else:
                if brush_deco_type == 1:
                    scherm.blit(Dec31,(muisx,muisy))
                elif brush_deco_type == 2:
                    scherm.blit(Dec32,(muisx,muisy))
                else:
                    scherm.blit(Dec33,(muisx,muisy))
                    
        elif brush == 'finish':
            scherm.blit(finish_foto,(muisx,muisy))
            
        elif brush == 'checkpoint':
            scherm.blit(checkpoint11_foto,(muisx,muisy))
            
        elif brush == 'bounce point':
            scherm.blit(blob2_foto,(muisx,muisy))
            
        if toggle_raster:
            teken_raster(scherm,5,muisx,muisy)
    deltaTime = clock.tick(360)
    schermblit.blit(pg.transform.scale(scherm, schermblit.get_rect().size).convert(), (0, 0))
    pg.display.flip()
    schermheightx, schermheighty = pg.display.get_surface().get_size()

def print_code(tag,obj_list):
    try:
        indexvar = 1
        print(tag + ':')
        sys.stdout.write('[')
        for Obj in obj_list:
            if len(obj_list) == indexvar:
                Obj_code = Obj.get_code(True).strip('"')
            else:
                Obj_code = Obj.get_code(False).strip('"')
            indexvar += 1
            sys.stdout.write(Obj_code)
        sys.stdout.write(']')
        print('')
    except NameError:
        print('No '+tag+' in level')

def get_code_value(obj_list):
    list_store = []
    try:
        indexvar = 1
        for Obj in obj_list:
            if len(obj_list) == indexvar:
                list_store.append(Obj.get_code(True).strip('"'))
            else:
                list_store.append(Obj.get_code(False).strip('"'))
            print(Obj_code)
            indexvar += 1
            #list_store.append(Obj_code)
        return list_store
    except NameError:
        return list_store

level_store = get_code_value(muur_lijst)
print_code('Muren',muur_lijst)
print_code('Stekels',stekel_lijst)
print_code('Stekel2',stekel2_lijst)
print_code('Stekel3',stekel3_lijst)
print_code('Powerups',powerup_lijst)
print_code('Geesten',geest_lijst)
print_code('Planten',plant_lijst)
print_code('Whirl',whirl_lijst)
print_code('Bewegende muren',bewegende_muren_lijst)
print_code('Knop muren',knop_muur_lijst)
print_code('Decoraties',decoratie_lijst)
print_code('Bounce points',bounce_point_lijst)
print('Finish: '+str(Finish.x)+','+str(Finish.y))
print('Checkpoint: '+str(Checkpoint.x)+','+str(Checkpoint.y))

pg.display.quit()        
pg.font.quit()
pg.quit()
