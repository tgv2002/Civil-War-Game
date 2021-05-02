import pygame

CAPTION = '     CIVIL WAR'
THANOS = './img/finalthanos.png'
SHIP = './img/evil_ship.png'
ROCK = './img/rockk.png'
INTRO = './img/introimg.jpg'
HEART = './img/realheart.png'
SHIELD = './img/actualshield.png'
window = pygame.display.set_mode((1860, 1080))
WIDTH = 1860
HEIGHT = 1080

BONUS_1 = 'IRON MAN wins 15 bonus points if he acquires an arc-reactor(his heart).'
BONUS_2 = 'CAP wins 15 bonus points if he acquires the shield made of vibranium,'

tree = pygame.image.load(THANOS)
rock = pygame.image.load(ROCK)
intro_img = pygame.image.load(INTRO)
ship = pygame.image.load(SHIP)
heart = pygame.image.load(HEART)
shield = pygame.image.load(SHIELD)
shield = pygame.transform.scale(shield, (45, 40))
tree = pygame.transform.scale(tree, (58, 70))
heart = pygame.transform.scale(heart, (40, 30))
intro_img = pygame.transform.scale(intro_img, (WIDTH, HEIGHT))
ship = pygame.transform.scale(ship, (100, 87))
rock = pygame.transform.scale(rock, (75, 70))


path_left = [pygame.image.load('./img/tile004.png'),
             pygame.image.load('./img/tile005.png'),
             pygame.image.load('./img/tile006.png'),
             pygame.image.load('./img/tile007.png')]
path_right = [pygame.image.load('./img/tile008.png'),
              pygame.image.load('./img/tile009.png'),
              pygame.image.load('./img/tile010.png'),
              pygame.image.load('./img/tile011.png')]
path_up = [pygame.image.load('./img/tile012.png'),
           pygame.image.load('./img/tile013.png'),
           pygame.image.load('./img/tile014.png'),
           pygame.image.load('./img/tile015.png')]
path_down = [pygame.image.load('./img/tile000.png'),
             pygame.image.load('./img/tile001.png'),
             pygame.image.load('./img/tile002.png'),
             pygame.image.load('./img/tile003.png')]

path2_left = [pygame.image.load('./img/tile2004.png'),
              pygame.image.load('./img/tile2005.png'),
              pygame.image.load('./img/tile2006.png'),
              pygame.image.load('./img/tile2007.png')]
path2_right = [pygame.image.load('./img/tile2008.png'),
               pygame.image.load('./img/tile2009.png'),
               pygame.image.load('./img/tile2010.png'),
               pygame.image.load('./img/tile2011.png')]
path2_up = [pygame.image.load('./img/tile2012.png'),
            pygame.image.load('./img/tile2013.png'),
            pygame.image.load('./img/tile2014.png'),
            pygame.image.load('./img/tile2015.png')]
path2_down = [pygame.image.load('./img/tile2000.png'),
              pygame.image.load('./img/tile2001.png'),
              pygame.image.load('./img/tile2002.png'),
              pygame.image.load('./img/tile2003.png')]



PLAYER1_VEL = 10
PLAYER2_VEL = 10
INIT_SPEED = 23

WHITE = (255, 255, 255)
GOLD = (255, 223, 0)
GAME_BLUE = (0, 0, 250)
GAME_YELLOW = (255, 215, 0)
VIOLET = (128, 0, 126)
DARK_BLUE = (0, 0, 128)
LIGHT_RED = (255, 80, 80)
GREEN = (0, 128, 128)
RED = (255, 0, 0)
YELLOW = (248, 230, 4)
ORANGE = (255, 79, 0)
MARVEL = (253, 0, 0)

COMIC = 'comicsans'
ARIAL = 'arial'
FONTSIZE_3 = 160
FONTSIZE_2 = 26
FONTSIZE_1 = 220
SIZE_11 = 80
SIZE_10 = 100
SIZE_5 = 65


BOTH_1 = 'NOBODY WINS!'
BOTH_2 = "It's"
BOTH_3 = 'a'
BOTH_4 = 'DRAW!'
BOTH_5 = 'NOBODY WON OR LOST'
BOTH_6 = 'ATLEAST,WE DID IT TOGETHER'

WIN_21 = 'Player 2'
WIN_22 = 'aka'
WIN_23 = 'CAPTAIN AMERICA'
WIN_24 = 'wins'
WIN_25 = 'I CAN DO THIS ALL DAY'

DIE_11 = 'Player 1'
DIE_12 = 'aka'
DIE_13 = 'IRON MAN'
DIE_14 = 'died'
DIE_15 = 'OOPS! MULTIPLE FRACTURES DETECTED'


WIN_11 = 'Player 1'
WIN_12 = 'aka'
WIN_13 = 'IRON MAN'
WIN_14 = 'wins'
WIN_15 = "I'AM IRON MAN"
