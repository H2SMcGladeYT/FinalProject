import pygame
import random
from time import sleep

#Initiate pygame
pygame.init()
speed = 200
screen = pygame.display.set_mode((800, 600))
angle = 45
prev_touched = 1
p1_points = 0
p2_points = 0
font = pygame.font.Font(None, 32)
pygame.display.set_caption('Ping Pong')

#Load and scale imgs
#abbacn daeyfdgehn idjoko
bat1_img = pygame.image.load('square.png')
bat2_img = pygame.image.load('square.png')
ball_img = pygame.image.load('circle.jpg')
ball_img = pygame.transform.scale(ball_img, (50, 50))
bat1_img = pygame.transform.scale(bat1_img, (20, 100))
bat2_img = pygame.transform.scale(bat2_img, (20, 100))

#Set origin of the bats and ball
ball_x, ball_y = 350, 250
bat1_x, bat1_y = 0, 0
bat2_x, bat2_y = 780, 500
#sleep(15)
#Main Loop
run = True
while run:
    bat2_y = ball_y
    screen.fill(0)
    amount = speed/1000
    if ball_x < 1:
        p1_points += 1
        ball_x, ball_y = 350, 350
        angle = 45
    if ball_x > 800:
        p2_points += 1
        ball_x, ball_y = 350, 350
        angle = 45
    #Render value of scores onto screen
    p1_text = font.render(str(p2_points), True, (0, 0, 0),(255, 255, 255))
    p2_text = text = font.render(str(p1_points), True, (0, 0, 0),(255, 255, 255))
    speed_text = font.render(str(int(speed/10)), True, (0, 0, 0),(255, 255, 255))

    #Detect keys to move bats
    mouse_x, mouse_y = pygame.mouse.get_pos()
    bat1_y = mouse_y
    '''key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        bat1_y -= speed/1000
    if key[pygame.K_s]:
        bat1_y += speed/1000'''
    #Show images on screen
    screen.blit(ball_img, (ball_x, ball_y))
    screen.blit(bat1_img, (bat1_x, bat1_y))
    screen.blit(bat2_img, (bat2_x, bat2_y))
    screen_edge1 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 800, 20))
    screen_edge2 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 580, 800, 600))
    screen.blit(p1_text, (300, 0))
    screen.blit(p2_text, (500, 0))
    screen.blit(speed_text, (400, 0))

    ball_rect = ball_img.get_rect(topleft=(ball_x, ball_y))
    bat1_rect = bat1_img.get_rect(topleft=(bat1_x, bat1_y))
    bat2_rect = bat2_img.get_rect(topleft=(bat2_x, bat2_y))

    #Check Collision
    if ball_rect.colliderect(screen_edge1):
        if prev_touched == 1:
            angle += 90
        if prev_touched == 2:
            angle -= 90
    if ball_rect.colliderect(screen_edge2):
        if prev_touched == 1:
            angle -= 90
        if prev_touched == 2:
            angle += 90
    if ball_rect.colliderect(bat1_rect):
        angle += 90
        speed += 10
        sleep(0.01)
    if ball_rect.colliderect(bat2_rect):
        angle -= 90
        speed += 10
        sleep(0.01)

    #Set angles within 360 degree boundary
    if angle > 359:
        angle = angle - 360
    if angle < 0:
        angle = angle + 360

    #Set direction based on angle
    if angle == 45:
        ball_x += amount
        ball_y -= amount
    if angle == 90:
        ball_x += amount
    if angle == 135:
        ball_x += amount
        ball_y += amount
    if angle == 180:
        ball_y += amount
    if angle == 225:
        ball_y += amount
        ball_x -= amount
    if angle == 270:
        ball_x -= amount
    if angle == 315:
        ball_x -= amount
        ball_y -= amount
    if angle == 0:
        ball_y -= amount

    if p1_points == 3:
        print('AI wins!')
        break
    if p2_points == 3:
        print('Player 1 wins!')
        break
        
    #Close window if X pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

pygame.quit()
