# Project Name / File Name: Space invadors 
# Written by:Maxim Mikulin
# Date: Start 04.02.2021
# Version:  2.0 
#What added: New menu, restart function
import pygame, sys
import random
import time
import math
pygame.init()
screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
running = True


#Title and icon
pygame.display.set_caption('Space invadors')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#objects
transparent = (0, 0, 0, 0)
back_menu = pygame.image.load('menu_backgound.jpg')
background = pygame.image.load('background.png')
# Player
playerImg = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

# Enemy
enemyImg = []
enemy_x = []
enemy_y = []

num_of_enemies = 6


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))

#Enemy_2
enemy2Img = []
enemy2_x = []
enemy2_y = []

num_of_enemies_2 = 6

for i in range(num_of_enemies_2):
    enemy2Img.append(pygame.image.load('alien.png'))
    enemy2_x.append(random.randint(0, 736))
    enemy2_y.append(random.randint(50, 150))
#Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_state = 'ready'
#score
score_value = 0
font = pygame.font.Font('ARCADECLASSIC.TTF', 32)
text_x = 10
text_y = 10
#File for high score
#high = open('highscore.txt','x')
def highscore():    
    file_high_score = open('highscore.txt','r')
    high_score = file_high_score.read()
    high_score_int = int(high_score)
    if high_score_int < score_value:
        highscore_write()
def highscore_write():
    score_value_str = str(score_value)
    highscore = open('highscore.txt','w')
    highscore.write(score_value_str)
def show_score(x,y):
    score = font.render('Score ' + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def show__high_score(x,y):
    file_high_score = open('highscore.txt','r')
    high_score = file_high_score.read()
    high_score = font.render('High score  ' + str(high_score),True,(255,255,255))
    screen.blit(high_score,(x,y))
 #gameover font
over_font = pygame.font.Font('ARCADECLASSIC.TTF', 64)  
#player positionning
def player(x,y):
    screen.blit(playerImg,(x,y) )
#enemy postioning
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y) )
#enemy2 positioning
def enemy2(x,y,i):
    screen.blit(enemy2Img[i],(x,y) )
#bullet postioning
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg,(x+16,y+10))
#coilision ofr enemy1
def colision(bullet_x,bullet_y,enemy_x,enemy_y):
    distnace = math.sqrt((enemy_x-bullet_x)**2+(enemy_y-bullet_y)**2)#calculationg distance from bullet to enemy with math equation
    if distnace < 30:
        return True
    else:
        return False
#colisoin for enemy 2
def colision2(bullet_x,bullet_y,enemy2_x,enemy2_y):
    distnace = math.sqrt((enemy2_x-bullet_x)**2+(enemy2_y-bullet_y)**2)#calculationg distance from bullet to enemy2 with math equation
    if distnace < 30:
        return True
    else:
        return False
#Lives
global lives
lives = 6
def live(x,y):
    
    live = font.render('Lives  ' + str(lives),True,(255,255,255))
    screen.blit(live,(x,y))
#gameover positioning    
def gameover():
    gameover_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover_text, (260, 250))
    return True
def restart():  
    gameover_text = font.render("Press   R   to   restart", True, (255, 255, 255))
    screen.blit(gameover_text, (260, 350)) 
# Game loop    
def game():
    # i disn't wanted to redocode for menu so i just made this 
    global player_x
    global player_x_change
    global bullet_x
    global bullet_y
    global score_value
    global bullet_state
    global running
    global screen
    #------
    while running :
        
        screen.fill((51,  51,  86))
        screen.blit(background,(0,0))#background 
        #exit button
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)

            if event.type == pygame.QUIT:
                exit()
                #Trunning = False
            #while game_over == False:
            global lives
            if event.type == pygame.KEYDOWN:
                if lives > 0:
                    if event.key == pygame.K_LEFT:
                            player_x_change = -0.5
                    if event.key == pygame.K_RIGHT: 
                            player_x_change = 0.5
                    if event.key == pygame.K_SPACE:
                            if bullet_state is "ready":
                    
                            # Get the current x cordinate of the spaceship
                                bullet_x = player_x
                                fire_bullet(bullet_x, bullet_y)   
                
                if event.key == pygame.K_r:
                        score_value = 0
                        lives = 6
                        for i in range(num_of_enemies):
                            enemy_x[i] = random.randint(0, 800)
                            enemy_y[i] = random.randint(50, 150)
                        for i in range(num_of_enemies_2):
                            enemy2_x[i] = random.randint(0, 800)
                            enemy2_y[i] = random.randint(50, 150)
                        main_menu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0
                    

            

                
        #player movement
        player_x += player_x_change
        if player_x <= 0:
            player_x = 0
        if player_x >= 736:
            player_x = 736  
        #enemy1 moevement
        if score_value >= 0:
            for i in range(num_of_enemies):
                enemy_x[i] += 0.25
                while enemy_x[i] < 0:
                    enemy_x[i] = 799
                    enemy_y[i] += 150

                while enemy_x[i] > 800:
                    enemy_x[i] = 1
                    enemy_y[i] += 150 
                    #collision_enemy1
                iscollision=colision(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
                if iscollision:
                    bullet_y = 480
                    bullet_state = "ready"
                    score_value += 1
                    enemy_x[i] = random.randint(0, 800)
                    enemy_y[i] = random.randint(50, 150)
                    highscore()
                if enemy_y[i] > 480:
                    lives -= 1
                    enemy_y[i] -= 5000
                if enemy_y[i] < 0:
                    enemy_y[i] -= 1
                        
                enemy(enemy_x[i],enemy_y[i],i)
        #enemy2
        if score_value >= 50:

            for i in range(num_of_enemies_2):
                enemy2_x[i] += 0.4
                while enemy2_x[i] < 0:
                    enemy2_x[i] = 799
                    enemy2_y[i] += 150

                while enemy2_x[i] > 800:
                    enemy2_x[i] = 1
                    enemy2_y[i] += 150 
                #collision_enemy2
                iscollision2=colision2(enemy2_x[i],enemy2_y[i],bullet_x,bullet_y)
                if iscollision2:
                    bullet_y = 480
                    bullet_state = "ready"
                    score_value += 2
                    enemy2_x[i] = random.randint(0, 800)
                    enemy2_y[i] = random.randint(50, 150)
                    highscore()
                if enemy2_y[i] > 480:
                    lives -= 1
                    enemy2_y[i] -= 5000
                if enemy_y[i]<0:
                    enemy_y[i]-=1
                enemy2(enemy2_x[i],enemy2_y[i],i)
        #bullet movemet
        while bullet_y < 0:
            bullet_y = 500
            bullet_state = 'ready'
            
        if bullet_state is 'fire':

            fire_bullet(bullet_x,bullet_y)
            bullet_y -= 1.5
        
        #GAME OVER
        while lives <= 0:
            live(5000,5000)
            for i in range(num_of_enemies):
                enemy_x[i] = 50000
                enemy_y[i] = 50000
            for i in range(num_of_enemies_2):
                enemy2_x[i] = 50000
                enemy2_y[i] = 50000  
            gameover()
            restart()
            break
        while lives > 0: 
            live(660,10)
            break
        #showing objects
        show__high_score(10,40)
        show_score(text_x,text_y)
        player(player_x,player_y)
        pygame.display.update() 
        pass
def main_menu_txt():
    button_1 = pygame.Rect(235, 110, 300, 50)
    pygame.draw.rect(screen, (0, 0, 0), button_1)
    text = over_font.render('Main menu',True,(255, 255, 255))
    screen.blit(text,(247,100))
def button1_txt():
    button_1_txt = font.render('Play',True,(255, 255, 255))
    screen.blit(button_1_txt,(362,210))
click = False
def controls_txt():
    button_1_txt = font.render('controlS',True,(255, 255, 255))
    screen.blit(button_1_txt,(330,310))
def main_menu():
    global click
    global screen
    while True:
        screen.blit(back_menu,(0,0))
        
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(300, 200, 200, 50)
        
        button_2 = pygame.Rect(300, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                click = False
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                click = False
                controls()
        pygame.draw.rect(screen, (69, 69, 69), button_1,border_radius=5)
        button1_txt()
        pygame.draw.rect(screen, (69, 69, 69), button_2,border_radius=5)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        controls_txt()
        main_menu_txt()
        pygame.display.update()
def arrow_right():
    button_1 = pygame.Rect(100, 100, 550, 50)
    pygame.draw.rect(screen, (0, 0, 0), button_1)
    text = font.render(': Right   arrow   to   move   player   right',True,(255, 255, 255))#the : should be there it's element of design 
    screen.blit(text,(100,110))
    return
def arrow_left():
    button_1 = pygame.Rect(100, 200, 500, 50)
    pygame.draw.rect(screen, (0, 0, 0), button_1)
    text = font.render(': Left   arrow   to   move   player   left',True,(255, 255, 255))
    screen.blit(text,(100,210))
    return
def k_esc():
    button_1 = pygame.Rect(100, 300, 650, 50)
    pygame.draw.rect(screen, (0, 0, 0), button_1)
    text = font.render(': Press   ESC   to   return   back   to   main   menu',True,(255, 255, 255))
    screen.blit(text,(100,310))
    return
def controls():
    running = True
    while running:
        global screen
        screen.blit(back_menu,(0,0))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
        k_esc()
        arrow_left()
        arrow_right()
        pygame.display.update()
main_menu()