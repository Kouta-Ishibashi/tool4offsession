#!/usr/bin/env python
#coding:utf-8

import pygame
from pygame.locals import *
import time
import sys
import random
def main():
    pygame.init()
    san_check = pygame.mixer.Sound('sancheck.wav')
    dice_role = pygame.mixer.Sound('dice.wav')
    screen = pygame.display.set_mode((300,200))
    pygame.display.set_caption("TEST")
    pygame.mixer.music.load('Taxiheaven.mp3')
    pygame.mixer.music.play(-1) # ()内は再生回数 -1:ループ再生
    while True:
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_0):
                pygame.mixer.music.fadeout(5000)
                time.sleep(8)
                pygame.mixer.music.load('Taxiheaven.mp3')
                pygame.mixer.music.play(-1)
            
            if (event.type == KEYDOWN and event.key == K_1):
                pygame.mixer.music.fadeout(5000)
                time.sleep(8)
                pygame.mixer.music.load('MarxSyndrome.mp3')
                pygame.mixer.music.play(-1)

            if (event.type == KEYDOWN and event.key == K_s):
                san_check.play()

            if (event.type == KEYDOWN and event.key == K_d):
                dice_role.play()
                time.sleep(2)
                print random.randint(1,100)

            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.mixer.music.fadeout(5000)
                time.sleep(5)
                return

            


        #pygame.mixer.music.pause() # 音楽の一時停止
        #pygame.mixer.music.unpause # 一時停止した音楽の再開
        #pygame.mixer.music.set_volume(0.8) # ボリュームの設定
        #pygame.mixer.music.queue('test2.mp3') # 次の再生ファイルのセット
        
        #print "音量:%s" % pygame.mixer.music.get_volume() #ボリュームの取得
        #print "再生時間:%s[ms]"%pygame.mixer.music.get_busy() # 再生時間の取得[ms]
    
#    time.sleep(10)
 #   pygame.mixer.music.stop() # 再生の終了
#

 #   print "終了"
if __name__ == '__main__': main()
