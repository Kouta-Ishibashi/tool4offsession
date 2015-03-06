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
    screen = pygame.display.set_mode()
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

        
    while True:
        pygame.display.update()
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

            if (event.type == KEYDOWN and event.key == K_d): #心理学などのシークレットダイス，出力は端末なので注意
                dice_role.play()
                time.sleep(2)
                print random.randint(1,100)

            if (event.type == KEYDOWN and event.key == K_ESCAPE): #終了
                pygame.mixer.music.fadeout(5000)
                time.sleep(5)
                return

if __name__ == '__main__': main()
