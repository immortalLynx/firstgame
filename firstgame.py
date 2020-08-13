import pygame

pygame.init()

canvasWidth = 500
win = pygame.display.set_mode((canvasWidth, 500))

pygame.display.set_caption("Cubes Game")

walkRight = []
for i in range(1, 7):
    walkRight.append(pygame.image.load('./img/pygame_right_' + str(i) + '.png'))

walkLeft = []
for i in range(1, 7):
    walkLeft.append(pygame.image.load('./img/pygame_left_' + str(i) + '.png'))

playerStand = pygame.image.load('./img/pygame_idle.png')
bg = pygame.image.load('./img/pygame_bg.jpg')

clock = pygame.time.Clock()

x = 50
y = 425
width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False

animCount = 0
lastMove = "right"
class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def drawWindow():
    global animCount

    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0
    
    if left:
        win.blit(walkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x,y))
        animCount += 1
    else:
        win.blit(playerStand, (x,y))

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

run = True
bullets = []

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if  bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width // 2), round(y + height // 2),
            5, (255,0,0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < canvasWidth - width - 5:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2 
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
    drawWindow()

pygame.quit()

