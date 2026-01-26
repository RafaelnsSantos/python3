#faça um programa em python que abra e reproduza o audio de um arquivo mp3.
#impossivel nao o codigo mesmo assistindo o video do curso em video ele nao funciona
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("ex21.mp3   ")
pygame.mixer.music.play()

input()
