#!/usr/bin/env python
#coding:utf-8

import pygame
from pygame.locals import *
import time
import sys
import random
import glob

def main():
    playlist = sorted(glob.glob('bgms/*'))
    pygame.init()
    san_check = pygame.mixer.Sound('sancheck.wav')
    dice_role = pygame.mixer.Sound('dice.wav')
    screen = pygame.display.set_mode((1300,720))
    pygame.display.set_caption("tool for offline session")    
    pygame.mixer.music.load(playlist[0])
    #pygame.mixer.music.play(-1) 
    smallfont = pygame.font.Font("ipag.ttf", 12) 
    font = pygame.font.Font("ipag.ttf", 24)
    largefont = pygame.font.Font("ipag.ttf", 36)
    title = largefont.render(u"BGMのリスト", False, (0,0,0))
    namelist = [font.render(unicode(str(playlist.index(x)) + ":" + (x[5:]).replace(".mp3",""), "UTF-8"), False, (0,0,0)) for x in playlist]
    playnamelist = [largefont.render(unicode("Now Playing-"+ (x[5:]).replace(".mp3",""), "UTF-8"), False, (0,0,0)) for x in playlist]
    screen.fill((255,255,255))
    screen.blit(title, (4, 0))
    i=0
    while i < 10:
        try:
            screen.blit(namelist[i],(4,40 + 25*i))
            i=i+1
        except IndexError:
            break
    st_screen = pygame.display.get_surface()
    pygame.display.update()
    while True:
        pygame.display.update(0,600,1300,720)
        for event in pygame.event.get():
            #曲の再生
            try:
                if (event.type == KEYDOWN and event.key == K_0):
                    t = playnamelist[0]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[0])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)
                if (event.type == KEYDOWN and event.key == K_1):
                    t = playnamelist[1]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[1])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)

                if (event.type == KEYDOWN and event.key == K_2):
                    t = playnamelist[2]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[2])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)
                    
                if (event.type == KEYDOWN and event.key == K_3):
                    t = playnamelist[3]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[3])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)
                    
                if (event.type == KEYDOWN and event.key == K_4):
                    t = playnamelist[4]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[4])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)

                if (event.type == KEYDOWN and event.key == K_5):
                    t = playnamelist[5]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[5])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)
                    
                if (event.type == KEYDOWN and event.key == K_6):
                    t = playnamelist[6]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[6])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)
                    
                if (event.type == KEYDOWN and event.key == K_7):
                    t = playnamelist[7]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[7])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)

                if (event.type == KEYDOWN and event.key == K_8):
                    t = playnamelist[8]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)
                    pygame.mixer.music.load(playlist[8])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)

                if (event.type == KEYDOWN and event.key == K_9):
                    t = playnamelist[9]
                    screen.fill((255,255,255),(0,600,1300,720))
                    pygame.display.update(0,600,1300,720)
                    screen.blit(t, (10,640))
                    pygame.mixer.music.fadeout(5000)                    
                    pygame.mixer.music.load(playlist[9])
                    time.sleep(2)
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.display.update(0,600,1300,720)

            except IndexError:
                screen.fill((255,255,255),(0,600,1300,720))
                pygame.display.update(0,600,1300,720)
                caution = font.render(u"その番号には曲がありません", False, (255,0,0))
                screen.blit(caution, (10,680))
                pygame.display.update(0,600,1300,720)
                screen.fill((255,255,255),(0,600,1300,720))
                time.sleep(4)
                pygame.display.update(0,600,1300,720)
                                
            #Sound Effect
            if (event.type == KEYDOWN and event.key == K_s): #SANチェックのSE
                san_check.set_volume(1)
                san_check.play()

            if (event.type == KEYDOWN and event.key == K_d): #心理学などのシークレットダイス.
                                        
                screen.fill((255,255,255),(0,680,1300,720))
                pygame.display.update(0,600,1300,720)
                dice_role.play()
                time.sleep(2)
                dice = font.render(unicode(str(random.randint(1,100)),"UTF-8"), False, (255,0,0))
                screen.blit(dice, (10,680))
            
            #終了処理
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                flag = True
                while flag:
                    for event in pygame.event.get():
                        screen.fill((255,255,255),(0,680,1300,720))
                        pygame.display.update(0,600,1300,720)
                        confirm = font.render(u"本当に終了しますか?(y/n)", False, (255,0,0))
                        screen.blit(confirm, (10,680))
                        pygame.display.update(0,600,1300,720)
                        if (event.type == KEYDOWN and event.key == K_y):
                            screen.fill((255,255,255),(0,680,1300,720))
                            pygame.display.update(0,600,1300,720)
                            close = font.render(u"終了しています", False, (255,0,0))
                            screen.blit(close, (10,680))
                            pygame.display.update(0,600,1300,720)
                            pygame.mixer.music.fadeout(5000)
                            time.sleep(5)
                            return
                        if (event.type == KEYDOWN and event.key == K_n):
                            screen.fill((255,255,255),(0,680,1300,720))
                            pygame.display.update(0,600,1300,720)
                            cancel = font.render(u"キャンセルしました", False, (255,0,0))
                            screen.blit(cancel, (10,680))
                            pygame.display.update(0,600,1300,720)
                            screen.fill((255,255,255),(0,600,1300,720))
                            time.sleep(4)
                            pygame.display.update(0,600,1300,720)
                            flag = False
                            break
                        
if __name__ == '__main__': main()
