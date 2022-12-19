import pygame
from pygame import mixer
import os
import threading
import random
from fighter import Fighter
from time import sleep

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
mixer.init()

info = pygame.display.Info()

SCREEN_WIDTH,SCREEN_HEIGHT = info.current_w, info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fight with a warrior")
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#set framerate
clock = pygame.time.Clock()
FPS = 60
WORK = 10000000

#define game vatiables
intro_count = 5
last_count_update = pygame.time.get_ticks()
score = [0, 0] #Player scores [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000


#define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#define fighter variavles
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112,107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
#load music and sounds
music_links = ['music.mp3', 'war2.mp3', 'war3.mp3', 'war5.mp3']

def get_music(array):
     return random.randrange(len(music_links))

pygame.mixer.music.load('assets/audio/war4.mp3')
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound('assets/audio/sword.wav')
sword_fx.set_volume(0.15)
magic_fx = pygame.mixer.Sound('assets/audio/magic.wav')
magic_fx.set_volume(0.25)
fight1_scream = pygame.mixer.Sound('assets/audio/fight1.wav')
fight1_scream.set_volume(0.15)
fight2_scream = pygame.mixer.Sound('assets/audio/fight2.wav')
fight2_scream.set_volume(0.15)


#load background image
bg_image = pygame.image.load("assets/images/background/background11.jpg").convert_alpha()
loading_image1 = pygame.image.load("assets/images/background/castle1.jpg").convert_alpha()
loading_image2 = pygame.image.load("assets/images/background/castle2.jpg").convert_alpha()

# load background spritesheets
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

#load victory image
victory_img = pygame.image.load('assets/images/icons/victory.png').convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

#define font
count_font = pygame.font.Font('assets/fonts/turok.ttf', 80)
score_font = pygame.font.Font('assets/fonts/turok.ttf', 30)

#function for drawing background
def draw_bg(image):
  scaled_bg = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))

#function for drawing fighter healts bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-2, y-2, 402, 34))
    pygame.draw.rect(screen, BLACK, (x, y, 400, 30))
    pygame.draw.rect(screen, RED, (x,y, 400*ratio, 30))

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#Create 2 instances of fighters
fighter_1 = Fighter(1, 200, SCREEN_HEIGHT-200, False, WARRIOR_DATA,  warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, fight1_scream)
fighter_2 = Fighter(2, SCREEN_WIDTH - 420, SCREEN_HEIGHT-200, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, fight2_scream)

loading = True

while loading:
    clock.tick(FPS)
    draw_bg(loading_image1)
    loading_text = 'Loading....'
    font = pygame.font.Font('assets/fonts/turok.ttf', 32)
    font2 = pygame.font.SysFont("corbel.tff", 26)
    for x in range(7):
        for i, v in enumerate(loading_text):
            if x < 3:
                draw_bg(loading_image1)
                advice = 'Press R or T to attack as warrior.'
                text2 = font2.render(advice, True, WHITE, BLACK)
                textRect2 = text2.get_rect()
                textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
                screen.blit(text2, textRect2)
            elif x >= 3:
                draw_bg(loading_image2)
                advice = 'Press 1 or 2 to attack as wizard.'
                text2 = font2.render(advice, True, WHITE, BLACK)
                textRect2 = text2.get_rect()
                textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
                screen.blit(text2, textRect2)
            text = font.render(loading_text[0:i], True, WHITE)
            textRect = text.get_rect()
            textRect.center = (200, SCREEN_HEIGHT-100)
            screen.blit(text, textRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    run = False
            pygame.display.update()

            sleep(0.25)

    screen.fill((0,0,0))
    loaded_text = 'Welcome. '
    text = font.render(loaded_text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (200, SCREEN_HEIGHT - 100)
    screen.blit(text, textRect)
    pygame.display.update()

    loading = False
    sleep(10)

pygame.mixer.music.load('assets/audio/' + music_links[get_music(music_links)])
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1, 0.0, 5000)

run = True

while run:
    clock.tick(FPS)

    if loading == False:
        draw_bg(bg_image)

        #show player stats
        draw_health_bar(fighter_1.health, 30, 20)
        draw_health_bar(fighter_2.health, SCREEN_WIDTH - 430, 20)
        draw_text("Warrior: " + str(score[0]), score_font, RED, 20, 60)
        draw_text("Wizard: " + str(score[1]), score_font, RED, SCREEN_WIDTH - 420, 60)
        #update countdown
        if intro_count <= 0:
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
        else:
            #display count timer
            draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH/2, SCREEN_HEIGHT / 3)
            #update count timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro_count -= 1
                last_count_update = pygame.time.get_ticks()


        #update figthers
        fighter_1.update()
        fighter_2.update()

        #draw figthers
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        #check for player defeat
        if round_over == False:
            if fighter_1.alive == False:
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif fighter_2.alive == False:
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else:
            #display victory image
            screen.blit(victory_img, (SCREEN_WIDTH/2.55, SCREEN_HEIGHT /3))
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                pygame.mixer.pause()
                pygame.mixer.music.load('assets/audio/' + music_links[get_music(music_links)])
                pygame.mixer.music.play(-1, 0.0, 5000)
                sword_fx = pygame.mixer.Sound('assets/audio/sword.wav')
                sword_fx.set_volume(0.15)
                magic_fx.set_volume(0.15)
                magic_fx = pygame.mixer.Sound('assets/audio/magic.wav')
                fight1_scream = pygame.mixer.Sound('assets/audio/fight1.wav')
                fight1_scream.set_volume(0.15)
                fight2_scream = pygame.mixer.Sound('assets/audio/fight2.wav')
                fight2_scream.set_volume(0.15)
                round_over = False
                intro_count = 5
                fighter_1 = Fighter(1, 200, SCREEN_HEIGHT - 200, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, fight1_scream)
                fighter_2 = Fighter(2, SCREEN_WIDTH - 420, SCREEN_HEIGHT - 200, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, fight2_scream)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
    pygame.display.update()

pygame.quit()