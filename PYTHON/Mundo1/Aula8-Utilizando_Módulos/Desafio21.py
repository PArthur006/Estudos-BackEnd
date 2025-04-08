#Faça um programa que execute um arquivo em mp3
import pygame
pygame.init()
pygame.mixer.music.load('kalimba.mp3')
pygame.mixer.music.play()
import time
time.sleep(15)
