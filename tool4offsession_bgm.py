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
    pygame.mixer.music.play(-1) 
    smallfont = pygame.font.Font("ipag.ttf", 12) 
    font = pygame.font.Font("ipag.ttf", 24)
    largefont = pygame.font.Font("ipag.ttf", 36)
    title = font.render(u"BGMのリスト", False, (0,0,0))
    namelist = [font.render(unicode(str(playlist.index(x)) + ":" + x[5:], "UTF-8"), False, (0,0,0)) for x in playlist]
    screen.fill((255,255,255))
    screen.blit(title, (4, 0))
    i=0
    while i < 10:
        try:
            screen.blit(namelist[i],(4,25 + 25*i))
            i=i+1
        except IndexError:
            break
    st_screen = pygame.display.get_surface()
    pygame.display.update()
    while True:
        pygame.display.update(0,600,1300,720)
        for event in pygame.event.get():
            try:
                if (event.type == KEYDOWN and event.key == K_0):
                    pygame.mixer.music.load(playlist[0])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)
                    
                if (event.type == KEYDOWN and event.key == K_1):
                    pygame.mixer.music.load(playlist[1])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)

                if (event.type == KEYDOWN and event.key == K_2):
                    pygame.mixer.music.load(playlist[2])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)
                    
                if (event.type == KEYDOWN and event.key == K_3):
                    pygame.mixer.music.load(playlist[3])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)
                    
                if (event.type == KEYDOWN and event.key == K_4):
                    pygame.mixer.music.load(playlist[4])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)

                if (event.type == KEYDOWN and event.key == K_5):
                    pygame.mixer.music.load(playlist[5])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)
                    
                if (event.type == KEYDOWN and event.key == K_6):
                    pygame.mixer.music.load(playlist[6])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)
                    
                if (event.type == KEYDOWN and event.key == K_7):
                    pygame.mixer.music.load(playlist[7])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)

                if (event.type == KEYDOWN and event.key == K_8):
                    pygame.mixer.music.load(playlist[8])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)

                if (event.type == KEYDOWN and event.key == K_9):
                    pygame.mixer.music.load(playlist[9])
                    pygame.mixer.music.fadeout(5000)
                    time.sleep(2)
                    pygame.mixer.music.play(-1)
            except IndexError:
                print "There is no music assigned that key."

            if (event.type == KEYDOWN and event.key == K_s): #SANチェックのSE
                san_check.set_volume(1)
                san_check.play()

            if (event.type == KEYDOWN and event.key == K_d): #心理学などのシークレットダイス.
                                        
                screen.fill((255,255,255),(0,600,1300,720))
                pygame.display.update(0,600,1300,720)
                dice_role.play()
                time.sleep(2)
                dice = font.render(unicode(str(random.randint(1,100)),"UTF-8"), False, (255,0,0))
                screen.blit(dice, (10,680))


            if (event.type == KEYDOWN and event.key == K_ESCAPE): #終了
                flag = True
                while flag:
                    for event in pygame.event.get():
                        #本当に終了しますか？
                        screen.fill((255,255,255),(0,600,1300,720))
                        pygame.display.update(0,600,1300,720)
                        confirm = font.render(u"本当に終了しますか?(Y/n)", False, (255,0,0))
                        screen.blit(confirm, (10,680))
                        pygame.display.update(0,600,1300,720)
                        if (event.type == KEYDOWN and event.key == K_y):
                            screen.fill((255,255,255),(0,600,1300,720))
                            pygame.display.update(0,600,1300,720)
                            close = font.render(u"終了しています", False, (255,0,0))
                            screen.blit(close, (10,680))
                            pygame.display.update(0,600,1300,720)
                            #終了しています
                            pygame.mixer.music.fadeout(5000)
                            time.sleep(5)
                            return
                        if (event.type == KEYDOWN and event.key == K_n):
                            #キャンセルしました宣言
                            screen.fill((255,255,255),(0,600,1300,720))
                            pygame.display.update(0,600,1300,720)
                            cancel = font.render(u"キャンセルしました", False, (255,0,0))
                            screen.blit(cancel, (10,680))
                            pygame.display.update(0,600,1300,720)
                            flag = False
                            break
                        
if __name__ == '__main__': main()
