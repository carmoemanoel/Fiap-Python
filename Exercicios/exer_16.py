# Faça um programa em Python que abra e reproduza uma música de um arquivo em MP3

import pygame
pygame.init()
pygame.mixer.music.load('exer_15.mp3')
pygame.mixer.music.play()
pygame.event.wait()

