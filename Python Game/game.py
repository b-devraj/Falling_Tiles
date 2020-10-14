import pygame
import random

pygame.init()

#gameboard details
WIDTH = 800
HEIGHT = 600

#colours/Font

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACK_COLOUR = (0, 0, 0)
myFont = pygame.font.SysFont("monospace", 35)

#player details
player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

#Enemy details
en_size = 50
en_pos = [random.randint(0, WIDTH-en_size), 0]
en_list = [en_pos]

#Game Speed/Score
SPEED = 0
SCORE = 0


screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

game_over = False


clock = pygame.time.Clock()

def set_level():
    global SPEED
    if SCORE < 20:
        SPEED = 6
    elif SCORE < 40:
        SPEED = 8
    elif SCORE < 60:
        SPEED = 10
    elif SCORE < 80:
        SPEED = 15
    else:
        SPEED = 20

def drop_enemies(en_list):
    delay = random.random()
    if len(en_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH-en_size)
        y_pos = 0
        en_list.append([x_pos, y_pos])
        
def draw_enemies(en_list):
    for en_pos in en_list:
         pygame.draw.rect(screen, RED , (en_pos[0], en_pos[1], en_size, en_size))
         
def update_en_pos(en_list):
    global SCORE
    for idx, en_pos in enumerate(en_list):
        if en_pos[1] >= 0 and en_pos[1] < HEIGHT:
            en_pos[1] += SPEED
    
        else:
            en_list.pop(idx)
            SCORE += 1  
            
        
def collision_check(en_list, player_pos):
    for enemy_pos in en_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False
        

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + en_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + en_size)):
            return True
        
    return False
        
    

while not game_over:
    
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
                
            player_pos = [x, y]
            
    
    screen.fill(BACK_COLOUR) #takes in RBG value to show game
    

        
    if detect_collision(player_pos, en_pos):
        game_over = True
        break
    
    set_level()
    drop_enemies(en_list)
    update_en_pos(en_list)
    
    text = "Score:" + str(SCORE)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))
    
    
    if collision_check(en_list, player_pos):
        game_over = True
        break
    
    draw_enemies(en_list)  
    pygame.draw.rect(screen, BLUE , (player_pos[0], player_pos[1], player_size, player_size))
    
    clock.tick(30)
    
    pygame.display.update()

print(SCORE)
pygame.quit()