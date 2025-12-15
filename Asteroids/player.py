from circleshape import CircleShape
from shot import Shot
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED
import pygame

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cd = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_cd -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*(-1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt*(1))
        if keys[pygame.K_s]:
            self.move((-1)*dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_RADIUS * dt

    def shoot(self):
        if self.shoot_cd > 0:
            pass
        else:
            self.shoot_cd = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED