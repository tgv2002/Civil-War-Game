from config import *
from fixedObstacle import *
from movingObstacle import *
from Bonus import *
import pygame
import sys
import math
pygame.init()


width = WIDTH
height = HEIGHT
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(CAPTION)


heart_width = 40
heart_height = 30
shield_width = 45
shield_height = 40

tree_x = []
rock_x = []
tree_y = []
rock_y = []

# adding background music
pygame.mixer.init()
collide = pygame.mixer.Sound('./music/Collisions.wav')
music = pygame.mixer.music.load('./music/Music.mp3')
pygame.mixer.music.play(-1)

check_shield1 = 0
check_shield2 = 0
check_heart1 = 0
check_heart2 = 0
leftCount = 0
rightCount = 0
winner = -1
upCount = 0
downCount = 0

leftCount_2 = 0
rightCount_2 = 0
upCount_2 = 0
downCount_2 = 0
flag_2 = 0

flag = 0
player1_x = width // 2
player1_y = height - 125
player1_vel = PLAYER1_VEL

player2_x = width // 2
player2_y = 12
player2_vel = PLAYER2_VEL

# setting flag array auch that we get points,
# only once, for crossing an obstacle
flag_fixed = [0, 0, 0, 0, 0]
flag_moving = [0, 0, 0, 0, 0]
player1_width = 32
player1_height = 48
player2_width = 32
player2_height = 48
player1 = True
player2 = False
ctr = 0
c = 0
d = 0
score_1 = 0
score_2 = 0
prev = 3
prev2 = 0

clock = pygame.time.Clock()


def player1_wins(num):
    # screen displayed when player 1 wins
    window.fill(MARVEL)
    font_4 = pygame.font.SysFont(COMIC, SIZE_10, True)
    text_1_1 = font_4.render(WIN_11, 1, WHITE)
    text_1_2 = font_4.render(WIN_12, 1, WHITE)
    text_1_3 = font_4.render(WIN_13, 1, WHITE)
    text_1_4 = font_4.render(WIN_14, 1, WHITE)

    window.blit(text_1_1, (width // 2.56, 200))
    window.blit(text_1_2, (width // 2.56, 300))
    window.blit(text_1_3, (width // 2.56, 400))
    window.blit(text_1_4, (width // 2.56, 500))

    window.blit(path_down[0], (width // 2.81, 750))
    font_5 = pygame.font.SysFont(COMIC, SIZE_11, True)
    text_2 = font_5.render(WIN_15, 1, GOLD)
    window.blit(text_2, (width // 2.81 + 58, 750))
    pygame.display.update()
    pygame.time.Clock().tick(0.15)


def player1_died():
    # screen displayed when player 1 hits an obstacle
    window.fill(MARVEL)
    font_4 = pygame.font.SysFont(COMIC, SIZE_10, True)
    text_1_1 = font_4.render(DIE_11, 1, WHITE)
    text_1_2 = font_4.render(DIE_12, 1, WHITE)
    text_1_3 = font_4.render(DIE_13, 1, WHITE)
    text_1_4 = font_4.render(DIE_14, 1, WHITE)

    window.blit(text_1_1, (width // 2.56, 200))
    window.blit(text_1_2, (width // 2.56, 300))
    window.blit(text_1_3, (width // 2.56, 400))
    window.blit(text_1_4, (width // 2.56, 500))

    window.blit(path_down[0], (width // 2.81, 750))
    font_5 = pygame.font.SysFont(COMIC, SIZE_5, True)
    text_2 = font_5.render(DIE_15, 1, GOLD)
    window.blit(text_2, (width // 2.81 + 58, 750))
    pygame.display.update()
    pygame.time.Clock().tick(0.25)


def player2_wins():
    # screen displayed when player 2 wins
    window.fill(MARVEL)
    font_6 = pygame.font.SysFont(COMIC, SIZE_10, True)
    text_2_1 = font_6.render(WIN_21, 1, WHITE)
    text_2_2 = font_6.render(WIN_22, 1, WHITE)
    text_2_3 = font_6.render(WIN_23, 1, WHITE)
    text_2_4 = font_6.render(WIN_24, 1, WHITE)

    window.blit(text_2_1, (width // 2.72, 200))
    window.blit(text_2_2, (width // 2.72, 300))
    window.blit(text_2_3, (width // 2.72, 400))
    window.blit(text_2_4, (width // 2.72, 500))

    window.blit(path2_down[0], (width // 2.89, 750))
    font_5 = pygame.font.SysFont(COMIC, SIZE_11, True)
    text_2 = font_5.render(WIN_25, 1, DARK_BLUE)
    window.blit(text_2, (width // 2.89 + 58, 750))
    pygame.display.update()
    pygame.time.Clock().tick(0.15)


def player1_Position(val):
    # function that determines the position of player
    # in accordance with arrow keys selected
    # for player 1
    global prev
    if val == -1:
        if prev == 3:
            window.blit(path_up[0], (player1_x, player1_y))
        if prev == 2:
            window.blit(path_right[0], (player1_x, player1_y))
        if prev == 1:
            window.blit(path_left[0], (player1_x, player1_y))
        if prev == 0:
            window.blit(path_down[0], (player1_x, player1_y))

    if val == 1:  # left
        global leftCount
        window.blit(path_left[leftCount % 4], (player1_x, player1_y))
        leftCount += 1
        if leftCount == 4:
            leftCount = 0
        prev = 1

    if val == 2:  # right
        global rightCount
        window.blit(path_right[rightCount % 4], (player1_x, player1_y))
        rightCount += 1
        if rightCount == 4:
            rightCount = 0
        prev = 2

    if val == 3:  # up
        global upCount
        window.blit(path_up[upCount % 4], (player1_x, player1_y))
        upCount += 1
        if upCount == 4:
            upCount = 0
        prev = 3

    if val == 0:  # down
        global downCount
        window.blit(path_down[downCount % 4], (player1_x, player1_y))
        downCount += 1
        if downCount == 4:
            downCount = 0
        prev = 0


def player2_Position(val):
    # sets right image for moving player 2
    # with respect to arrow keys
    global prev2
    if val == -1:
        if prev2 == 3:
            window.blit(path2_up[0], (player2_x, player2_y))
        if prev2 == 2:
            window.blit(path2_right[0], (player2_x, player2_y))
        if prev2 == 1:
            window.blit(path2_left[0], (player2_x, player2_y))
        if prev2 == 0:
            window.blit(path2_down[0], (player2_x, player2_y))

    if val == 1:  # left
        global leftCount_2
        window.blit(path2_left[leftCount_2 % 4], (player2_x, player2_y))
        leftCount_2 += 1
        if leftCount_2 == 4:
            leftCount_2 = 0
        prev2 = 1

    if val == 2:  # right
        global rightCount_2
        window.blit(path2_right[rightCount_2 % 4], (player2_x,
                    player2_y))
        rightCount_2 += 1
        if rightCount_2 == 4:
            rightCount_2 = 0
        prev2 = 2

    if val == 3:  # up
        global upCount_2
        window.blit(path2_up[upCount_2 % 4], (player2_x, player2_y))
        upCount_2 += 1
        if upCount_2 == 4:
            upCount_2 = 0
        prev2 = 3

    if val == 0:  # down
        global downCount_2
        window.blit(path2_down[downCount_2 % 4], (player2_x, player2_y))
        downCount_2 += 1
        if downCount_2 == 4:
            downCount_2 = 0
        prev2 = 0


def bothLose():
    # if both the players die or have equal scores
    # this screen is displayed
    window.fill(MARVEL)
    font_10 = pygame.font.SysFont(COMIC, SIZE_10, True)
    text_3_1 = font_10.render(BOTH_1, 1, WHITE)
    text_3_2 = font_10.render(BOTH_2, 1, WHITE)
    text_3_3 = font_10.render(BOTH_3, 1, WHITE)
    text_3_4 = font_10.render(BOTH_4, 1, WHITE)

    window.blit(text_3_1, (width // 2.56, 100))
    window.blit(text_3_2, (width // 2.56, 200))
    window.blit(text_3_3, (width // 2.56, 300))
    window.blit(text_3_4, (width // 2.56, 400))

    window.blit(path_right[0], (width // 2.81, 650))

    font_11 = pygame.font.SysFont(COMIC, SIZE_11, True)
    text_3 = font_11.render(BOTH_5, 1, GOLD)
    window.blit(text_3, (width // 2.81 + 58, 650))
    font_12 = pygame.font.SysFont(COMIC, 80, True)
    text_4 = font_12.render(BOTH_6, 1, DARK_BLUE)
    window.blit(text_4, (width // 2.81, 750))
    window.blit(path2_left[0], (width // 1.09, 750))
    pygame.display.update()
    pygame.time.Clock().tick(0.12)

run = True
window.fill(GAME_BLUE)

# storing locations of fixed obstacles

for i in range(0, height, (height - 420) // 5 + 60):
    ctr += 1
    if ctr == 10:
        ctr = 0
    for j in range(0, width, 320):
        if ctr % 2 == 1 and i != 0 and i != 960:
            c += 1
            if c == 10:
                c = 0
            if c % 2 == 1:
                tree_x.append(j)
                tree_y.append(i)
            else:
                rock_x.append(j)
                rock_y.append(i)
        elif i != 0 and i != 960:
            d += 1
            if d == 10:
                d = 0
            if d % 2 == 1:
                tree_x.append(j + 160)
                tree_y.append(i)
            else:
                rock_x.append(j + 160)
                rock_y.append(i)

shipImg_1 = movingObstacle()
shipImg_2 = movingObstacle()
shipImg_3 = movingObstacle()
shipImg_4 = movingObstacle()
shipImg_5 = movingObstacle()

# initializing positions of moving obstacles

shipImg_1.y = 80
shipImg_2.y = 80 + 192 * 1
shipImg_3.y = 80 + 192 * 2
shipImg_4.y = 80 + 192 * 3
shipImg_5.y = 80 + 192 * 4

shipImg_1.x = 0
shipImg_2.x = 80 + 192 * 3
shipImg_3.x = 80 + 192 * 1
shipImg_4.x = 80 + 192 * 4
shipImg_5.x = 80 + 192 * 2


def displayText_1(score_1):

    # displayed when player 1 is playing

    start = font_1.render('START', 1, RED)
    end = font_2.render('END', 1, GREEN)
    score_count = font_3.render('Score : ' + str(score_1), 1, VIOLET)

    window.blit(start, (width // 1.9, height - 110))
    window.blit(end, (width // 1.2, 10))
    window.blit(score_count, (50, 13))


def displayText_2(score_2):

    # displayed when player 2 is playing

    start = font_1.render('START', 1, RED)
    end = font_2.render('END', 1, GREEN)
    score_count = font_3.render('Score : ' + str(score_2), 1, VIOLET)
    window.blit(end, (width // 1.9, height - 110))
    window.blit(start, (width // 1.2, 10))
    window.blit(score_count, (50, 13))
Shield_1 = Bonus()
Heart_1 = Bonus()
Shield_2 = Bonus()
Heart_2 = Bonus()

# assigning variables such that it increases speed
# for winner of current level , in next level

win_1 = 0
win_2 = 0
vis_shield1 = 1
vis_shield2 = 1
vis_heart1 = 1
vis_heart2 = 1
count = 0

# main menu of game


def intro_game():
    intro = True
    window.blit(intro_img, (0, 0))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                intro = False
        font_intro = pygame.font.SysFont(COMIC, FONTSIZE_1, True)
        text_intro1 = font_intro.render('CIVIL', 1, RED)
        text_intro2 = font_intro.render('WAR', 1, RED)
        font_intro2 = pygame.font.SysFont(ARIAL, FONTSIZE_2, True)
        text_intro3 = \
            font_intro2.render('Ready to take part in the Civil War?',
                               1, YELLOW)
        text_intro4 = \
            font_intro2.render(
                'If TONY/CAP reach the opposite end of the river, ',
                1,
                YELLOW
            )
        text_intro5 = \
            font_intro2.render(
                'without encountering any obstacle ,and obtains a ',
                1,
                YELLOW
            )
        text_intro6 = \
            font_intro2.render(
                'score higher than the other player,he wins! ',
                1,
                YELLOW
            )
        text_intro7 = \
            font_intro2.render(
                'He loses one point for every second he wastes. ',
                1,
                YELLOW
            )
        text_intro7_1 = \
            font_intro2.render(
                'If he wastes more than 50 seconds, he dies. ',
                1,
                YELLOW
            )
        text_intro8 = \
            font_intro2.render(
                'He wins 5 points if he crosses the deadly trees/rocks, ',
                1,
                YELLOW
            )
        text_intro9 = \
            font_intro2.render(
                'and 10 if he crosses the fast-moving pirate ship. ',
                1,
                YELLOW
            )
        text_intro10 = \
            font_intro2.render(
                BONUS_1,
                1,
                YELLOW
            )
        text_intro11 = \
            font_intro2.render(
                BONUS_2,
                1,
                YELLOW
            )
        text_intro12 = \
            font_intro2.render(
                "(made by Tony Stark's father,of course). ",
                1,
                YELLOW
            )
        font_intro3 = pygame.font.SysFont(COMIC, FONTSIZE_3, True)
        text_intro13 = font_intro3.render('Hit', 1, ORANGE)
        text_intro14 = font_intro3.render('ENTER!', 1, ORANGE)
        text_intro15 = font_intro3.render('Let the', 1, ORANGE)
        text_intro16 = font_intro3.render('WAR', 1, ORANGE)
        text_intro17 = font_intro3.render('BEGIN!', 1, ORANGE)

        window.blit(intro_img, (0, 0))
        window.blit(text_intro1, (0, 60))
        window.blit(text_intro2, (30, 200))
        window.blit(text_intro3, (30, 380))
        window.blit(text_intro4, (30, 440))
        window.blit(text_intro5, (30, 500))
        window.blit(text_intro6, (30, 560))
        window.blit(text_intro7, (30, 620))
        window.blit(text_intro7_1, (30, 680))
        window.blit(text_intro8, (30, 740))
        window.blit(text_intro9, (30, 800))
        window.blit(text_intro10, (30, 860))
        window.blit(text_intro11, (30, 920))
        window.blit(text_intro12, (30, 980))
        window.blit(text_intro13, (width // 1.4, 500))
        window.blit(text_intro14, (width // 1.4, 600))
        window.blit(text_intro15, (width // 1.4, 700))
        window.blit(text_intro16, (width // 1.4, 800))
        window.blit(text_intro17, (width // 1.4, 900))

        press = pygame.key.get_pressed()

        if press[pygame.K_RETURN]:
            intro = False

        pygame.display.update()


intro_game()
# game loop
while run:

    if pygame.time.get_ticks() // 1000 > count:
        count = pygame.time.get_ticks() // 1000
        # player loses if he wastes 50 seconds or more
        if score_1 < -49:
            player1_died()
            player1 = False
            player2 = True
            score_1 = 1000
            player1_x = width // 2
            player1_y = height - 125
        if score_2 < -49:
            score_2 = 1000
            player1 = True
            player2 = False
            player1_x = width // 2
            player1_y = height - 125

            player2_x = width // 2
            player2_y = 12
            if score_1 != 1000 and score_2 < score_1:
                player1_wins(1)
                winner = 1
                win_1 += 2
            if score_2 == 1000 and score_1 != 1000:
                player1_wins(2)
                winner = 1
                win_1 += 2
            if score_2 != 1000 and score_1 < score_2:
                player2_wins()
                winner = 2
                win_2 += 2
            if score_1 == 1000 and score_2 != 1000:
                player2_wins()
                winner = 2
                win_2 += 2
            if score_1 == score_2 and score_1 != 1000:
                bothLose()
            if score_1 == score_2 and score_1 == 1000:
                bothLose()
            # resetting values at end of round
            vis_shield1 = 1
            vis_shield2 = 1
            vis_heart1 = 1
            vis_heart2 = 1
            check_shield1 = 0
            check_shield2 = 0
            check_heart1 = 0
            check_heart2 = 0
            score_1 = 0
            score_2 = 0
            for k in range(len(flag_fixed)):
                flag_fixed[k] = 0
            for k in range(len(flag_moving)):
                flag_moving[k] = 0

        if player1:
            score_1 = score_1 - 1
        else:
            score_2 = score_2 - 1

    font_1 = pygame.font.SysFont('comicsans', 60, True)
    font_2 = pygame.font.SysFont('comicsans', 60, True)
    font_3 = pygame.font.SysFont('comicsans', 50, True)
    flag = 0
    flag_2 = 0
    clock.tick(26)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(GAME_BLUE)
    # setting game screen
    for i in range(0, height, (height - 420) // 5 + 60):
        pygame.draw.rect(window, GAME_YELLOW, (0, i, width, 60))

    if player1:
        Heart_1.setHeart(90, 90, vis_heart1)
        Heart_2.setHeart(width - 200, height - 200, vis_heart2)
    else:
        Shield_1.setShield(90, 90, vis_shield1)
        Shield_2.setShield(width - 200, height - 200, vis_shield2)
    # increasing score by 15, only once, for obtaining a bonus
    if(player2_x <= Shield_1.x + shield_width):
        if(player2_x >= Shield_1.x - player2_width):
            if(player2_y <= Shield_1.y + shield_height):
                if(player2_y >= Shield_1.y - player2_height):
                    vis_shield1 = 0
                    if check_shield1 == 0:
                        score_2 += 15
                        check_shield1 = 1
    if(player2_x <= Shield_2.x + shield_width):
        if(player2_x >= Shield_2.x - player2_width):
            if(player2_y <= Shield_2.y + shield_height):
                if(player2_y >= Shield_2.y - player2_height):
                    vis_shield2 = 0
                    if check_shield2 == 0:
                        score_2 += 15
                        check_shield2 = 1
    if(player1_x <= Heart_1.x + heart_width):
        if(player1_x >= Heart_1.x - player1_width):
            if(player1_y <= Heart_1.y + heart_height):
                if(player1_y >= Heart_1.y - player1_height):
                    vis_heart1 = 0
                    if check_heart1 == 0:
                        score_1 += 15
                        check_heart1 = 1

    if(player1_x <= Heart_2.x + heart_width):
        if(player1_x >= Heart_2.x - player1_width):
            if(player1_y <= Heart_2.y + heart_height):
                if(player1_y >= Heart_2.y - player1_height):
                    vis_heart2 = 0
                    if check_heart2 == 0:
                        score_1 += 15
                        check_heart2 = 1

    treeImg = fixedObstacle()
    rockImg = fixedObstacle()

    pressed = pygame.key.get_pressed()
    # assigning arrow keys for player 1
    if pressed[pygame.K_LEFT] and player1_x > player1_vel:
        player1_x -= player1_vel
        player1_Position(1)
        flag = 1

    if pressed[pygame.K_RIGHT]:
        if player1_x < width - 35 - player1_width - player1_vel:
            player1_x += player1_vel
            player1_Position(2)
            flag = 1

    if pressed[pygame.K_UP] and player1_y > player1_vel:
        player1_y -= player1_vel
        player1_Position(3)
        flag = 1

    if pressed[pygame.K_DOWN]:
        if player1_y < height - 45 - player1_height - player1_vel:
            player1_y += player1_vel
            player1_Position(0)
            flag = 1

    if flag == 0:
        player1_Position(-1)

    # assigning arrow keys for player 2
    if pressed[pygame.K_a] and player2_x > player2_vel:
        player2_x -= player2_vel
        player2_Position(1)
        flag_2 = 1

    if pressed[pygame.K_d]:
        if player2_x < width - 35 - player2_width - player2_vel:
            player2_x += player2_vel
            player2_Position(2)
            flag_2 = 1

    if pressed[pygame.K_w] and player2_y > player2_vel:
        player2_y -= player2_vel
        player2_Position(3)
        flag_2 = 1

    if pressed[pygame.K_s]:
        if player2_y < height - 45 - player2_height - player2_vel:
            player2_y += player2_vel
            player2_Position(0)
            flag_2 = 1

    if flag_2 == 0:
        player2_Position(-1)
    # setting speeds of moving obstacles
    if run:
        if shipImg_1.x <= width:
            if player1:
                shipImg_1.setShip(
                    shipImg_1.x + INIT_SPEED + win_1,
                    shipImg_1.y
                )
            else:
                shipImg_1.setShip(
                    shipImg_1.x + INIT_SPEED + win_2,
                    shipImg_1.y
                )
        else:
            shipImg_1.x = 0

        if shipImg_2.x <= width:
            if player1:
                shipImg_2.setShip(
                    shipImg_2.x + INIT_SPEED + win_1,
                    shipImg_2.y
                )
            else:
                shipImg_2.setShip(
                    shipImg_2.x + INIT_SPEED + win_2,
                    shipImg_2.y
                )
        else:
            shipImg_2.x = 0

        if shipImg_3.x <= width:
            if player1:
                shipImg_3.setShip(
                    shipImg_3.x + INIT_SPEED + win_1,
                    shipImg_3.y
                )
            else:
                shipImg_3.setShip(
                    shipImg_3.x + INIT_SPEED + win_2,
                    shipImg_3.y
                )
        else:
            shipImg_3.x = 0

        if shipImg_4.x <= width:
            if player1:
                shipImg_4.setShip(
                    shipImg_4.x + INIT_SPEED + win_1,
                    shipImg_4.y
                )
            else:
                shipImg_4.setShip(
                    shipImg_4.x + INIT_SPEED + win_2,
                    shipImg_4.y
                )
        else:
            shipImg_4.x = 0

        if shipImg_5.x <= width:
            if player1:
                shipImg_5.setShip(
                    shipImg_5.x + INIT_SPEED + win_1,
                    shipImg_5.y
                )
            else:
                shipImg_5.setShip(
                    shipImg_5.x + INIT_SPEED + win_2,
                    shipImg_5.y
                )
        else:
            shipImg_5.x = 0
    # setting fixed obstacles
    for i in range(0, height, (height - 420) // 5 + 60):
        ctr += 1
        if ctr == 10:
            ctr = 0
        for j in range(0, width, 320):
            if ctr % 2 == 1 and i != 0 and i != 960:
                c += 1
                if c == 10:
                    c = 0
                if c % 2 == 1:
                    treeImg.setTree(j, i)
                else:
                    rockImg.setRock(j, i)
            elif i != 0 and i != 960:
                d += 1
                if d == 10:
                    d = 0
                if d % 2 == 1:
                    treeImg.setTree(j + 160, i)
                else:
                    rockImg.setRock(j + 160, i)
    # checking for collisions of player 1 with fixed obstacles
    for q in range(0, len(rock_x), 1):
        if player1_x <= tree_x[q] + 55:
            if player1_x >= tree_x[q] - player1_width + 29:
                if player1_y <= tree_y[q] + 50:
                    if player1_y >= tree_y[q] + 20 - player1_height:
                        pygame.mixer.Sound.play(collide)
                        player1_died()
                        player1 = False
                        player2 = True
                        score_1 = 1000
                        player1_x = width // 2
                        player1_y = height - 125

        if player1_x <= rock_x[q] + 55:
            if player1_x >= rock_x[q] - player1_width + 25:
                if player1_y <= rock_y[q] + 55:
                    if player1_y >= rock_y[q] + 12 - player1_height:
                        pygame.mixer.Sound.play(collide)
                        player1_died()
                        player1 = False
                        player2 = True
                        score_1 = 1000
                        player1_x = width // 2
                        player1_y = height - 125
    # checking for collision of player 1 with moving obstacles
    if player1_x <= shipImg_1.x + 100:
        if player1_x >= shipImg_1.x - player1_width:
            if player1_y <= shipImg_1.y + 87:
                if player1_y >= shipImg_1.y - player1_height:
                    pygame.mixer.Sound.play(collide)
                    player1_died()
                    player1 = False
                    player2 = True
                    score_1 = 1000
                    player1_x = width // 2
                    player1_y = height - 125

    if player1_x <= shipImg_2.x + 100:
        if player1_x >= shipImg_2.x - player1_width:
            if player1_y <= shipImg_2.y + 87:
                if player1_y >= shipImg_2.y - player1_height:
                    pygame.mixer.Sound.play(collide)
                    player1_died()
                    player1 = False
                    player2 = True
                    score_1 = 1000
                    player1_x = width // 2
                    player1_y = height - 125

    if player1_x <= shipImg_3.x + 100:
        if player1_x >= shipImg_3.x - player1_width:
            if player1_y <= shipImg_3.y + 87:
                if player1_y >= shipImg_3.y - player1_height:
                    pygame.mixer.Sound.play(collide)
                    player1_died()
                    player1 = False
                    player2 = True
                    score_1 = 1000
                    player1_x = width // 2
                    player1_y = height - 125

    if player1_x <= shipImg_4.x + 100:
        if player1_x >= shipImg_4.x - player1_width:
            if player1_y <= shipImg_4.y + 87:
                if player1_y >= shipImg_4.y - player1_height:
                    pygame.mixer.Sound.play(collide)
                    player1_died()
                    player1 = False
                    player2 = True
                    score_1 = 1000
                    player1_x = width // 2
                    player1_y = height - 125

    if player1_x <= shipImg_5.x + 100:
        if player1_x >= shipImg_5.x - player1_width:
            if player1_y <= shipImg_5.y + 87:
                if player1_y >= shipImg_5.y - player1_height:
                    pygame.mixer.Sound.play(collide)
                    player1_died()
                    player1 = False
                    player2 = True
                    score_1 = 1000
                    player1_x = width // 2
                    player1_y = height - 125
    # checking for collisions of player 2 with fixed obstacles
    for q2 in range(0, len(rock_x), 1):
        if player2_x <= tree_x[q2] + 55:
            if player2_x >= tree_x[q2] - player2_width + 29:
                if player2_y <= tree_y[q2] + 50:
                    if player2_y >= tree_y[q2] + 20 - player2_height:

                        pygame.mixer.Sound.play(collide)
                        score_2 = 1000
                        player1 = True
                        player2 = False

                        player1_x = width // 2
                        player1_y = height - 125

                        player2_x = width // 2
                        player2_y = 12
                        if score_1 != 1000 and score_2 < score_1:
                            winner = 1
                            win_1 += 2
                            player1_wins(4)
                        if score_2 == 1000 and score_1 != 1000:
                            winner = 1
                            win_1 += 2
                            player1_wins(5)

                        if score_2 != 1000 and score_1 < score_2:
                            winner = 2
                            win_2 += 2
                            player2_wins()
                        if score_1 == 1000 and score_2 != 1000:
                            winner = 2
                            win_2 += 2
                            player2_wins()

                        if score_1 == score_2 and score_1 != 1000:
                            bothLose()
                        if score_1 == score_2 and score_1 == 1000:
                            bothLose()

                        score_1 = 0
                        score_2 = 0
                        for k in range(len(flag_fixed)):
                            flag_fixed[k] = 0
                        for k in range(len(flag_moving)):
                            flag_moving[k] = 0
                        vis_shield1 = 1
                        vis_shield2 = 1
                        vis_heart1 = 1
                        vis_heart2 = 1
                        check_shield1 = 0
                        check_shield2 = 0
                        check_heart1 = 0
                        check_heart2 = 0

        if player2_x <= rock_x[q2] + 55:
            if player2_x >= rock_x[q2] - player2_width + 25:
                if player2_y <= rock_y[q2] + 55:
                    if player2_y >= rock_y[q2] + 12 - player2_height:
                        score_2 = 1000
                        pygame.mixer.Sound.play(collide)
                        player1 = True
                        player2 = False
                        player1_x = width // 2
                        player1_y = height - 125

                        player2_x = width // 2
                        player2_y = 12
                        if score_1 != 1000 and score_2 < score_1:
                            player1_wins(6)
                            winner = 1
                            win_1 += 2
                        if score_2 == 1000 and score_1 != 1000:
                            player1_wins(7)
                            winner = 1
                            win_1 += 2

                        if score_2 != 1000 and score_1 < score_2:
                            player2_wins()
                            winner = 2
                            win_2 += 2
                        if score_1 == 1000 and score_2 != 1000:
                            player2_wins()
                            winner = 2
                            win_2 += 2
                        if score_1 == score_2 and score_1 != 1000:
                            bothLose()
                        if score_1 == score_2 and score_1 == 1000:
                            bothLose()

                        score_1 = 0
                        score_2 = 0
                        for k in range(len(flag_fixed)):
                            flag_fixed[k] = 0
                        for k in range(len(flag_moving)):
                            flag_moving[k] = 0
                        check_shield1 = 0
                        check_shield2 = 0
                        check_heart1 = 0
                        check_heart2 = 0
                        vis_shield1 = 1
                        vis_shield2 = 1
                        vis_heart1 = 1
                        vis_heart2 = 1
    # checking for collisions of player 2 with moving obstacles
    if player2_x <= shipImg_1.x + 100:
        if player2_x >= shipImg_1.x - player2_width:
            if player2_y <= shipImg_1.y + 87:
                if player2_y >= shipImg_1.y - player2_height:

                    pygame.mixer.Sound.play(collide)
                    score_2 = 1000
                    player1 = True
                    player2 = False
                    player1_x = width // 2
                    player1_y = height - 125

                    player2_x = width // 2
                    player2_y = 12
                    if score_1 != 1000 and score_2 < score_1:
                        player1_wins(8)
                        winner = 1
                        win_1 += 2
                    if score_2 == 1000 and score_1 != 1000:
                        player1_wins(9)
                        winner = 1
                        win_1 += 2
                    if score_2 != 1000 and score_1 < score_2:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == 1000 and score_2 != 1000:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == score_2 and score_1 != 1000:
                        bothLose()
                    if score_1 == score_2 and score_1 == 1000:
                        bothLose()

                    score_1 = 0
                    score_2 = 0
                    for k in range(len(flag_fixed)):
                        flag_fixed[k] = 0
                    for k in range(len(flag_moving)):
                        flag_moving[k] = 0
                    vis_shield1 = 1
                    vis_shield2 = 1
                    vis_heart1 = 1
                    vis_heart2 = 1
                    check_shield1 = 0
                    check_shield2 = 0
                    check_heart1 = 0
                    check_heart2 = 0

    if player2_x <= shipImg_2.x + 100:
        if player2_x >= shipImg_2.x - player2_width:
            if player2_y <= shipImg_2.y + 87:
                if player2_y >= shipImg_2.y - player2_height:
                    pygame.mixer.Sound.play(collide)
                    score_2 = 1000
                    player2_x = width // 2
                    player2_y = 12
                    player1 = True
                    player2 = False
                    player1_x = width // 2
                    player1_y = height - 125

                    player2_x = width // 2
                    player2_y = 12
                    if score_1 != 1000 and score_2 < score_1:
                        player1_wins(10)
                        winner = 1
                        win_1 += 2
                    if score_2 == 1000 and score_1 != 1000:
                        player1_wins(11)
                        winner = 1
                        win_1 += 2
                    if score_2 != 1000 and score_1 < score_2:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == 1000 and score_2 != 1000:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == score_2 and score_1 != 1000:
                        bothLose()
                    if score_1 == score_2 and score_1 == 1000:
                        bothLose()

                    score_1 = 0
                    score_2 = 0
                    for k in range(len(flag_fixed)):
                        flag_fixed[k] = 0
                    for k in range(len(flag_moving)):
                        flag_moving[k] = 0
                    vis_shield1 = 1
                    vis_shield2 = 1
                    vis_heart1 = 1
                    vis_heart2 = 1
                    check_shield1 = 0
                    check_shield2 = 0
                    check_heart1 = 0
                    check_heart2 = 0

    if player2_x <= shipImg_3.x + 100:
        if player2_x >= shipImg_3.x - player2_width:
            if player2_y <= shipImg_3.y + 87:
                if player2_y >= shipImg_3.y - player2_height:

                    pygame.mixer.Sound.play(collide)
                    score_2 = 1000
                    player2_x = width // 2
                    player2_y = 12
                    player1 = True
                    player2 = False

                    player1_x = width // 2
                    player1_y = height - 125

                    player2_x = width // 2
                    player2_y = 12
                    if score_1 != 1000 and score_2 < score_1:
                        player1_wins(12)
                        winner = 1
                        win_1 += 2
                    if score_2 == 1000 and score_1 != 1000:
                        player1_wins(13)
                        winner = 1
                        win_1 += 2
                    if score_2 != 1000 and score_1 < score_2:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == 1000 and score_2 != 1000:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == score_2 and score_1 != 1000:
                        bothLose()
                    if score_1 == score_2 and score_1 == 1000:
                        bothLose()

                    score_1 = 0
                    score_2 = 0
                    for k in range(len(flag_fixed)):
                        flag_fixed[k] = 0
                    for k in range(len(flag_moving)):
                        flag_moving[k] = 0
                    vis_shield1 = 1
                    vis_shield2 = 1
                    vis_heart1 = 1
                    vis_heart2 = 1
                    check_shield1 = 0
                    check_shield2 = 0
                    check_heart1 = 0
                    check_heart2 = 0

    if player2_x <= shipImg_4.x + 100:
        if player2_x >= shipImg_4.x - player2_width:
            if player2_y <= shipImg_4.y + 87:
                if player2_y >= shipImg_4.y - player2_height:
                    pygame.mixer.Sound.play(collide)
                    score_2 = 1000
                    player2_x = width // 2
                    player2_y = 12
                    player1 = True
                    player2 = False
                    player1_x = width // 2
                    player1_y = height - 125

                    player2_x = width // 2
                    player2_y = 12
                    if score_1 != 1000 and score_2 < score_1:
                        player1_wins(14)
                        winner = 1
                        win_1 += 2
                    if score_2 == 1000 and score_1 != 1000:
                        player1_wins(15)
                        winner = 1
                        win_1 += 2
                    if score_2 != 1000 and score_1 < score_2:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == 1000 and score_2 != 1000:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == score_2 and score_1 != 1000:
                        bothLose()
                    if score_1 == score_2 and score_1 == 1000:
                        bothLose()

                    score_1 = 0
                    score_2 = 0
                    for k in range(len(flag_fixed)):
                        flag_fixed[k] = 0
                    for k in range(len(flag_moving)):
                        flag_moving[k] = 0
                    vis_shield1 = 1
                    vis_shield2 = 1
                    vis_heart1 = 1
                    vis_heart2 = 1
                    check_shield1 = 0
                    check_shield2 = 0
                    check_heart1 = 0
                    check_heart2 = 0

    if player2_x <= shipImg_5.x + 100:
        if player2_x >= shipImg_5.x - player2_width:
            if player2_y <= shipImg_5.y + 87:
                if player2_y >= shipImg_5.y - player2_height:

                    pygame.mixer.Sound.play(collide)
                    score_2 = 1000
                    player2_x = width // 2
                    player2_y = 12
                    player1 = True
                    player2 = False
                    player1_x = width // 2
                    player1_y = height - 125

                    player2_x = width // 2
                    player2_y = 12
                    if score_1 != 1000 and score_2 < score_1:
                        player1_wins(16)
                        winner = 1
                        win_1 += 2
                    if score_2 == 1000 and score_1 != 1000:
                        player1_wins(17)
                        winner = 1
                        win_1 += 2
                    if score_2 != 1000 and score_1 < score_2:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == 1000 and score_2 != 1000:
                        player2_wins()
                        winner = 2
                        win_2 += 2
                    if score_1 == score_2 and score_1 != 1000:
                        bothLose()
                    if score_1 == score_2 and score_1 == 1000:
                        bothLose()

                    score_1 = 0
                    score_2 = 0
                    for k in range(len(flag_fixed)):
                        flag_fixed[k] = 0
                    for k in range(len(flag_moving)):
                        flag_moving[k] = 0
                    vis_shield1 = 1
                    vis_shield2 = 1
                    vis_heart1 = 1
                    vis_heart2 = 1
                    check_shield1 = 0
                    check_shield2 = 0
                    check_heart1 = 0
                    check_heart2 = 0
    # increasing score of player 1 on crossing obstacles
    if player1:

        # moving

        for ctr in range(828, 0, -192):
            if player1_height + player1_y <= ctr:
                if flag_moving[ctr // 192] == 0:
                    score_1 += 10
                    flag_moving[ctr // 192] = 1

        # fixed

        for ctr2 in range(768, 0, -192):
            if player1_height + player1_y <= ctr2:
                if flag_fixed[ctr2 // 192] == 0:
                    score_1 += 5
                    flag_fixed[ctr2 // 192] = 1
    # increasing score of player 2 on crossing obstacles
    if player2:

        # moving

        for ctr3 in range(192, 969, 192):
            if player2_y >= ctr3 and flag_moving[ctr3 // 192] == 0:
                score_2 += 10
                flag_moving[ctr3 // 192] = 1

        # fixed

        for ctr4 in range(252, 969, 192):
            if player2_y >= ctr4 and flag_fixed[ctr4 // 192] == 0:
                score_2 += 5
                flag_fixed[ctr4 // 192] = 1

    if player1_y <= 15 and player1:
        score_1 += 10

    if player2_y >= height - 130 and player2:
        score_2 += 10
    # displaying the corresponding score for the current player
    if player1:
        displayText_1(score_1)
    else:
        displayText_2(score_2)
    # resetting when player 1 reaches the end
    if player1_y <= 15 and player1:
        player1 = False
        player2 = True
        score_2 = 0
        for k in range(len(flag_fixed)):
            flag_fixed[k] = 0
        for k in range(len(flag_moving)):
            flag_moving[k] = 0
    # re-initializing and displaying screen contents after
    # a round is completed (if player 2 wins, here)
    if player2_y >= height - 130 and player2:
        player1 = True
        player2 = False
        player1_x = width // 2
        player1_y = height - 125

        player2_x = width // 2
        player2_y = 12
        if score_1 != 1000 and score_2 < score_1:
            player1_wins(18)
            winner = 1
            win_1 += 2
        if score_2 == 1000 and score_1 != 1000:
            player1_wins(19)
            winner = 1
            win_1 += 2
        if score_2 != 1000 and score_1 < score_2:
            player2_wins()
            winner = 2
            win_2 += 2
        if score_1 == 1000 and score_2 != 1000:
            player2_wins()
            winner = 2
            win_2 += 2
        if score_1 == score_2 and score_1 != 1000:
            bothLose()
        if score_1 == score_2 and score_1 == 1000:
            bothLose()
        score_1 = 0
        score_2 = 0
        for k in range(len(flag_fixed)):
            flag_fixed[k] = 0
        for k in range(len(flag_moving)):
            flag_moving[k] = 0
        vis_shield1 = 1
        vis_shield2 = 1
        vis_heart1 = 1
        vis_heart2 = 1
        check_shield1 = 0
        check_shield2 = 0
        check_heart1 = 0
        check_heart2 = 0
    # updating game screen
    pygame.display.update()
# exit game
pygame.quit()
