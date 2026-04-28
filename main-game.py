# This is going to be my first attempt at making the main game, wish me luck.
import pygame
import sys
import math

# Mandatory start
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1600, 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bunker Game")

# Loading of images
# Still having to adjust paths (from main folder)
player_img = pygame.image.load("reference material/images/player2.1.png").convert_alpha()
terrain_img = pygame.image.load("reference material/images/terrain.png").convert_alpha()
blast_img = pygame.image.load("reference material/images/blast-radius.png").convert_alpha()

# Colors
GREEN = (34, 139, 34)
BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
RED = (200, 0, 0)
OFFWHITE = (255, 255, 205, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

class Worm:
    def __init__(self, x, y, imgWorm):
        self.x = x
        self.y = y
        self.width = 44
        self.height = 99
        self.footing = ((self.x + self.width // 2) + 39, (self.y + self.height) + 20)
        self.imgWorm = imgWorm
        self.vel_y = 0
        self.mirror = False
        # self.on_ground = False

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.mirror = True
            self.footing = ((self.x + self.width // 2) + 39, (self.y + self.height) + 20)
            
            yCount = 0
            for yCount in range(6):
                if self.check_collision(self.footing[0] - 1, self.footing[1] - yCount) == False:
                    self.x -= 1
                    self.y -= yCount
                    break
                elif self.check_collision(self.footing[0] - 1, self.footing[1] - yCount) == True:
                    yCount += 1
            
            yCount = 0
            for yCount in range(6):
                if self.check_collision(self.footing[0] - 1, self.footing[1] - yCount) == False:
                    self.x -= 1
                    self.y -= yCount
                    break
                elif self.check_collision(self.footing[0] - 1, self.footing[1] - yCount) == True:
                    yCount += 1
            

        if keys[pygame.K_RIGHT]:
            self.mirror = False
            self.footing = ((self.x + self.width // 2) + 39, (self.y + self.height) + 20)

            yCount = 0
            for yCount in range(6):
                if self.check_collision(self.footing[0] + 1, self.footing[1] - yCount) == False:
                    self.x += 1
                    self.y -= yCount
                    break
                elif self.check_collision(self.footing[0] + 1, self.footing[1] - yCount) == True:
                    yCount += 1
            
            yCount = 0
            for yCount in range(6):
                if self.check_collision(self.footing[0] + 1, self.footing[1] - yCount) == False:
                    self.x += 1
                    self.y -= yCount
                    break
                elif self.check_collision(self.footing[0] + 1, self.footing[1] - yCount) == True:
                    yCount += 1

    def apply_gravity(self):
        # if not self.on_ground:
        #     self.vel_y += 0.5
        #     self.y += self.vel_y
        self.footing = ((self.x + self.width // 2) + 39, (self.y + self.height) + 20)

        if (self.check_collision(self.footing[0], self.footing[1] + 1 + self.vel_y)):
            self.vel_y = 0
        else:
            self.vel_y += 0.5
            self.y += self.vel_y
            
    def check_collision(self, posX, posY):
        if terrain.checkPixelTerrain((posX, posY)):
            return True
        return False

    def draw(self):
        if self.mirror:
            screen.blit(pygame.transform.flip(self.imgWorm, True, False), (self.x, self.y))
        else:
            screen.blit(self.imgWorm, (self.x, self.y))

class Terrain:
    def __init__(self, imgTerrain):
        self.imgTerrain = imgTerrain
        self.position = (0, 900)
        self.mask = pygame.mask.from_surface(imgTerrain)

    def checkPixelTerrain(self, maskPos):

        mask_x = maskPos[0] - self.position[0]
        mask_y = maskPos[1] - self.position[1]

        if 0 <= mask_x < self.mask.get_size()[0] and 0 <= mask_y < self.mask.get_size()[1]:
            return self.mask.get_at((mask_x, mask_y)) == 1
        return False

    def destroyTerrain(self, pos, imgBlast):
        # pygame.draw.circle(screen, (255, 255, 205, 0), (pos[0], pos[1]), 20)
        blast_mask = pygame.mask.from_surface(imgBlast)
        blast_offset = (pos[0] - self.position[0] - imgBlast.get_width() // 2, pos[1] - self.position[1] - imgBlast.get_height() // 2)
        self.mask.erase(blast_mask, blast_offset)
        # Update the terrain image to reflect the destroyed area
        for x in range(imgBlast.get_width()):
            for y in range(imgBlast.get_height()):
                if blast_mask.get_at((x, y)) == 1:
                    terrain_x = blast_offset[0] + x
                    terrain_y = blast_offset[1] + y
                    if 0 <= terrain_x < self.mask.get_size()[0] and 0 <= terrain_y < self.mask.get_size()[1]:
                        self.imgTerrain.set_at((terrain_x, terrain_y), (255, 255, 205, 255))

    def draw(self):
        screen.blit(self.imgTerrain, self.position)


class Projectile:
    def __init__(self, x, y, imgBlast, angle, power):
        self.x = x
        self.y = y
        self.imgBlast = imgBlast
        self.vel_x = math.cos(angle) * power
        self.vel_y = -math.sin(angle) * power
        self.radius = 4
        self.active = True
    
    def update(self):
        if not self.active:
            return
        self.vel_y += 0.3  # gravity
        self.x += self.vel_x
        self.y += self.vel_y

        # Collision with terrain
        if 0 <= int(self.x) < WIDTH and 0 <= int(self.y) < HEIGHT:
            if terrain.checkPixelTerrain((int(self.x), int(self.y))):
                self.explode((int(self.x), int(self.y)))
        else:
            self.active = False

    def explode(self, pos):
        terrain.destroyTerrain(pos, self.imgBlast)
        self.active = False

    def draw(self):
        if self.active:
            pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)


terrain = Terrain(terrain_img)

worms = [Worm(200, 200, player_img), Worm(600, 200, player_img)]
current_worm = 0
projectiles = []

while True:
    # Main Game loop
    # Starting by spawning two example worms
    screen.fill((OFFWHITE))
    terrain.draw()

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                angle = 0
                power = 0
                
                worm = worms[current_worm]
                if worm.mirror == False:
                    angle = math.radians(45)
                    power = 8
                elif worm.mirror == True:
                    angle = math.radians(135)
                    power = 8

                projectiles.append(Projectile(worm.x, worm.y, blast_img, angle, power))
    
    worm = worms[current_worm]
    worm.move(keys)
    worm.apply_gravity()
    worm.draw()
    for p in projectiles:
        p.update()
        p.draw()

    pygame.display.flip()
    clock.tick(60)