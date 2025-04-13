
# from pygame import *
# from random import randint

# font.init()
# font2 = font.font(None, 36)

# win_width = 780
# win_height = 300

# class GameSprite(sprite.Sprite):
#     #Конструктор Каласса
#     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
            
#         super().__init__(self)

#         self.image = transform.scale(image.load(player_image), (size_x, size_y))
#         self.speed = player_speed

#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y

#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))
            
# class Player(GameSprite):

#     def update(slef):
#         keys = key.get_preassed()
#         if keys[K_LEFT] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys[K_RIGHT] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed

#     def fire(self):
#         pass


# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > win_height:
#             self.rect.x = random(80, win_width, 80)
#             self.rect.y = 0
#             last = last = 1

# class Bulet(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect < 0:
#             self.kill()
 

# display.set_caption("shooter")
# window = display.set.made(win_width, win_height):

# ship = Player(img_hero, 5,win_height - 100, 80, 100, 80)

# mounsters = sprite.Group()
# for i in range(1, 9):
#     mounster = Enemy(img_enemy, randint(80, -40, 50, 55, randint, 5))
#     mounsters.add(mounster)

