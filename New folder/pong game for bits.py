import pygame
pygame.init()
size = 750, 500
window = pygame.display.set_mode((size))
pygame.display.set_caption("pong game for bits")
img = pygame.image.load("back.gif")
black = (0, 0, 0)
blue = (0, 0, 128)
gray = (192, 192, 192)
red = (200, 0, 0)
class Pad1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.points = 0
class Pad2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.points = 0
class Dot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.speed = 7
        self.dx = 1
        self.dy = 1
pad1 = Pad1()
pad1.rect.x = 25
pad1.rect.y = 225
pad2 = Pad2()
pad2.rect.x = 715
pad2.rect.y = 225
pad_speed = 10
pong = Dot()
pong.rect.x = 375
pong.rect.y = 250
all_sprites = pygame.sprite.Group()
all_sprites.add(pad1, pad2, pong)
def redraw():
    window.fill(gray)
    window.blit(img, (-250, -150))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    title = font.render('PONG GAME FOR BITS', False, black)
    textRect = title.get_rect()
    textRect.center = (750 // 2, 25)
    window.blit(title, textRect)
    p1_score = font.render(str(pad1.points), False, black)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    window.blit(p1_score, p1Rect)
    p2_score = font.render(str(pad2.points), False, black)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    window.blit(p2_score, p2Rect)
    all_sprites.draw(window)
    pygame.display.update()
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        pad1.rect.y += -pad_speed
    if key[pygame.K_s]:
        pad1.rect.y += pad_speed
    if key[pygame.K_UP]:
        pad2.rect.y += -pad_speed
    if key[pygame.K_DOWN]:
        pad2.rect.y += pad_speed
    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy
    if pong.rect.y > 490:
        pong.dy = -1
    if pong.rect.y < 1:
        pong.dy = 1
    if pong.rect.x > 740:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        pad1.points += 1
    if pong.rect.x < 1:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = 1
        pad2.points += 1
    if pad1.rect.colliderect(pong.rect):
        pong.dx = 1
    if pad2.rect.colliderect(pong.rect):
        pong.dx = -1
    redraw()
pygame.quit()