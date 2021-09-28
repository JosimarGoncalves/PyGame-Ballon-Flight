from math import fabs
import pgzrun
import pygame
from random import randint

width =800
height = 600
balloon = Actor ("balloon")
balloon.pos = 400,300
bird = Actor ("bird-up")
bird.pos = randint(800,1600), randint(10,200)
house = Actor("house")
house.pos = randint(800,1600),460
tree = Actor ("tree")
tree.pos = randint(800,1600),450

bird_up = True
up = False
game_over = False
score = 0
number_of_updates=0

scores = []



def update_high_scores():
    global score, scores
    filename = r"high-scores.txt"
    scores = []
    with open (filename,"r")as file:
        line = file.readline()
        high_scores = line.split()
        for high_scores in high_scores:
            if(score >int(high_score)):
                scores.append(str(score)+ " ")
                score = int(high_score)
            else:
                scores.append(str(high_score)+ " ")
    with open(filename, "w") as file:
        for high_score in scores:
            file.write(high_score)

def display_high_scores():
    screen.draw.text("HIGH SCORES",(350,150),color = "black")
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position)+". "+ high_score, (350,y), color ="black")
        y += 25
        position +=1                            

def draw():
    screen.blit("background",(0,0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score:"+ str(score),(700,5), color="black")
    else:
        display_high_scores()

def on_mouse_down():
    global up
    up = True
    balloon.y -=50

def on_mouse_up():
    global up
    up = False 

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird.up = True

def update():
    global game_over, score , number_of_updates
    if not game_over:
        if not up:
            balloon.y += 1                               