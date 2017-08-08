import pygame
import os, sys
import random

if getattr(sys, 'frozen', False):
    src_dir = sys._MEIPASS
else:
    src_dir = os.path.join(os.path.abspath("."))
    
class SHOT(object):
    shot_list = []
    class_counter = 0

    def __init__(self, x, y, pera=False):
        SHOT.shot_list.append(self)
        self.id = SHOT.class_counter
        SHOT.class_counter += 1
        self.x = x
        self.y = y
        self.x2 = x
        self.y2 = y
        self.x3 = x
        self.y3 = y
        self.pera = pera
        self.rect = pygame.Rect(self.x, self.y, 10, 21)
        self.rect2 = pygame.Rect(self.x, self.y, 10, 21)
        self.rect3 = pygame.Rect(self.x, self.y, 10, 21)
        effect = pygame.mixer.Sound('{src_dir}\\swoosh.wav'.format(src_dir=src_dir))
        effect.play()

    def increment(self):
        if self.pera:
            screen.blit(pygame.image.load('{src_dir}\\Bullet_small.png'.format(src_dir=src_dir)),
                        (self.x2, self.y2, 20, 20))
            self.rect2 = pygame.Rect(self.x2, self.y2, 10, 21)
            screen.blit(pygame.image.load('{src_dir}\\Bullet_small.png'.format(src_dir=src_dir)),
                        (self.x3, self.y3, 20, 20))
            self.rect3 = pygame.Rect(self.x3, self.y3, 10, 21)
            self.y2 -= 15
            self.y3 -= 15
            self.x2 -= 3
            self.x3 += 3
        screen.blit(pygame.image.load('{src_dir}\\Bullet_small.png'.format(src_dir=src_dir)),
                    (self.x, self.y, 20, 20))
        self.rect = pygame.Rect(self.x, self.y, 10, 21)
        self.y -= 15
        if self.y < 0:
            for broj, shot in enumerate(SHOT.shot_list):
                if shot.id == self.id:
                    del SHOT.shot_list[broj]
            del self
        
            
    def delete(self):
        for broj, shot in enumerate(SHOT.shot_list):
            if shot.id == self.id:
                del SHOT.shot_list[broj] 
        del self

class BUG(object):
    bug_list = []
    class_counter = 0

    def __init__(self, x, y, howfast, level, r=False):
        rnd = [True, False]
        BUG.bug_list.append(self)
        self.id = BUG.class_counter
        BUG.class_counter += 1
        self.x = x
        self.y = y
        self.howfast = howfast
        self.level = level
        self.right = random.choice(rnd)
        if self.right == True:
            self.left = False
        else:
            self.left = True
        self.start_x = x
        self.r = r
        self.count = 1
        

    def increment(self):
        if self.r:
            if self.count == 1:
                screen.blit(pygame.image.load('{src_dir}\\bug1600.png'.format(src_dir=src_dir)), (self.x, self.y, 20, 20))
                self.rect = pygame.Rect(self.x, self.y, 65, 65)
            else:
                screen.blit(pygame.image.load('{src_dir}\\bug1600_small.png'.format(src_dir=src_dir)),
                            (self.x, self.y, 20, 20))
                self.rect = pygame.Rect(self.x, self.y, 45, 45)
        else:
            screen.blit(pygame.image.load('{src_dir}\\bad-bug.png'.format(src_dir=src_dir)), (self.x, self.y, 20, 20))
            self.rect = pygame.Rect(self.x, self.y, 44, 40)
        if self.level >= 4:
            self.y += 3
        elif self.level >= 6:
            self.y += 4
        elif self.level >= 8:
            self.y += 5
        else:
            self.y += 2
        if self.level >= 2:
            if self.x >= 770:
                self.right = False
                self.left = True
            elif self.x <= 1:
                self.right = True
                self.left = False
            if self.right:
                self.x += self.howfast
            if self.left:
                self.x -= self.howfast
        if self.y > 600:
            for broj, bug in enumerate(BUG.bug_list):
                if bug.id == self.id:
                    del BUG.bug_list[broj]
            del self

    def delete(self):
        for broj, bug in enumerate(BUG.bug_list):
            if bug.id == self.id:
                del BUG.bug_list[broj]
        del self

    def count_bug(self):
        self.count += 1
        if self.count > 5:
            for broj, bug in enumerate(BUG.bug_list):
                if bug.id == self.id:
                    del BUG.bug_list[broj]
            del self





class PERA(object):
    pera_list = []
    class_counter = 0

    def __init__(self):

        PERA.pera_list.append(self)
        self.id = PERA.class_counter
        PERA.class_counter += 1
        self.x = random.randrange(1, 730)
        self.y = 5

    def increment(self):
        screen.blit(pygame.image.load('{src_dir}\\pera.png'.format(src_dir=src_dir)), (self.x, self.y, 20, 20))
        self.rect = pygame.Rect(self.x, self.y, 50, 67)
        self.y += 3
        if self.y > 600:
            for broj, pera in enumerate(PERA.pera_list):
                if pera.id == self.id:
                    del PERA.pera_list[broj]
            del self

    def delete(self):
        for broj, pera in enumerate(PERA.pera_list):
            if pera.id == self.id:
                del PERA.pera_list[broj]
        del self

def start():
    screen.fill((37, 37, 38))
    texts("Welcome! ", "Press SPACE to play", 150, 200)
    texts("Controls - ", "Press 's' to shot the bug, '<' to move left, '>' to move right", 10, 350)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_SPACE]:
            break
        pygame.display.update()
        clock.tick(15)

def crash(Count):
    screen.fill((37, 37, 38))
    pygame.mixer.music.load('{src_dir}\\Failure-trumpet-melody.mp3'.format(src_dir=src_dir))
    pygame.mixer.music.play(0)
    screen.blit(pygame.image.load('{src_dir}\\bedbug1_01.png'.format(src_dir=src_dir)), (1, 1, 20, 20))
    texts("Press SPACE to play again. Your Score: ", Count, 1, 1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_SPACE]:
            for shot in SHOT.shot_list:
                shot.delete()
            for bug in BUG.bug_list:
                bug.delete()
            break

        pygame.display.update()
        clock.tick(15)

def texts(name, score, x, y):
   font=pygame.font.Font('{src_dir}\\Kayak Sans Bold.otf'.format(src_dir=src_dir),30)
   text=font.render(name + str(score), 1,(255,255,255))
   screen.blit(text, (x, y))

pygame.init()
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
start()

def main_loop():
    Stefan = True
    Stefan_count = 0
    time_elapsed_since_last_action_stefan = 0
    Malko = True
    Malko_count = 0
    time_elapsed_since_last_action_malko = 0
    create_pera = True
    pera_game = False
    x = 300
    y = 520
    speed = 100
    fx = 5
    fy = 5
    f1x = 732
    f1y = 5
    f2x = 5
    f2y = 5
    right_fx = True
    left_fx = False
    right_f1x = True
    left_f1x = False
    right_f2x = True
    left_f2x = False
    how_fast = 3
    time_elapsed_since_last_action = 0
    time_elapsed_since_last_action_pera = 0
    time_elapsed = 0
    l = 1
    Count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    if pera_game:
                        SHOT(x+25, y, pera=True)
                    else:
                        SHOT(x+25, y)
                        

        screen.fill((37, 37, 38))

        if x > 740:
            x = 740
        if x < 1:
            x = 1
        player_rect = pygame.Rect(x, y, 60, 67)
        
        if fx >= 400:
            right_fx = False
            left_fx = True
        elif fx <= 1:
            right_fx = True
            left_fx = False
        if right_fx:
            fx += how_fast
        if left_fx:
            fx -= how_fast
    
        if f1x >= 732:
            right_f1x = False
            left_f1x = True
        elif f1x <= 380:
            right_f1x = True
            left_f1x = False
        if right_f1x:
            f1x += how_fast
        if left_f1x:
            f1x -= how_fast
    
        if f2x >= 732:
            right_f2x = False
            left_f2x = True
        elif f2x <= 1:
            right_f2x = True
            left_f2x = False
        if right_f2x:
            f2x += how_fast
        if left_f2x:
            f2x -= how_fast
    
        pressed = pygame.key.get_pressed()
        
    
        if pressed[pygame.K_LEFT]:
            x -= 4
    
        if pressed[pygame.K_RIGHT]:
            x += 4

        
    
        dt = clock.tick()
        time_elapsed += dt
    
        if time_elapsed > 1200:
            how_fast += 1
            time_elapsed = 0
            l += 1
        # create bug
        time_elapsed_since_last_action += dt
        time_elapsed_since_last_action_pera += dt
        if time_elapsed_since_last_action > 300:
            seconds = [301, 302, 303, 304, 305]
            if time_elapsed_since_last_action in seconds:
                if Malko:
                    BUG(fx, 15, how_fast, l)
                if Stefan:
                    BUG(f1x, 15, how_fast, l)
                if l > 2: ###############################################################################
                    BUG(f2x, 15, how_fast, l, r=True)
                time_elapsed_since_last_action = 0
        if create_pera:
            if l > 1:
                if time_elapsed_since_last_action_pera > 600:
                    seconds = [601, 602, 603]
                    if time_elapsed_since_last_action_pera in seconds:
                        PERA()
                    time_elapsed_since_last_action_pera = 0

        # player
        if pera_game:
            screen.blit(pygame.image.load('{src_dir}\Pera.png'.format(src_dir=src_dir)), (x, y, 20, 20))
        else:
            screen.blit(pygame.image.load('{src_dir}\Nidza.png'.format(src_dir=src_dir)), (x, y, 20, 20))
        # comp
        if Malko:
            screen.blit(pygame.image.load('{src_dir}\Malko.png'.format(src_dir=src_dir)), (fx, fy, 20, 20))
            malko_rect = pygame.Rect(fx, fy, 60, 87)
        if Stefan:
            screen.blit(pygame.image.load('{src_dir}\Stefan.png'.format(src_dir=src_dir)), (f1x, f1y, 20, 20))
            stefan_rect = pygame.Rect(f1x, f1y, 60, 67)
        if l >= 3:
            screen.blit(pygame.image.load('{src_dir}\Robert.png'.format(src_dir=src_dir)), (f2x, f2y, 20, 20))

        for pera in PERA.pera_list:
            pera.increment()

        for shot in SHOT.shot_list:
            shot.increment()
        for bug in BUG.bug_list:
            bug.increment()
        for shot in SHOT.shot_list:
            for bug in BUG.bug_list:
                if shot.rect.colliderect(bug.rect):
                    if bug.r == True:
                        effect = pygame.mixer.Sound('{src_dir}\smashed-bug.wav'.format(src_dir=src_dir))
                        effect.play()
                        bug.count_bug()
                        shot.delete()
                        if bug.count > 5:
                            Count += 1
                        
                    else:
                    # pygame.mixer.music.load('Oops.mp3')
                    # pygame.mixer.music.play(0)
                        effect = pygame.mixer.Sound('{src_dir}\smashed-bug.wav'.format(src_dir=src_dir))
                        effect.play()
                        bug.delete()
                        shot.delete()
                        Count += 1
                if shot.pera:
                    if shot.rect.colliderect(bug.rect) or shot.rect2.colliderect(bug.rect) or shot.rect3.colliderect(bug.rect):
                        if bug.r == True:
                            effect = pygame.mixer.Sound('{src_dir}\smashed-bug.wav'.format(src_dir=src_dir))
                            effect.play()
                            bug.count_bug()
                            shot.delete()
                            if bug.count > 5:
                                Count += 1
                        else:
                            effect = pygame.mixer.Sound('{src_dir}\smashed-bug.wav'.format(src_dir=src_dir))
                            effect.play()
                            bug.delete()
                            shot.delete()
                            
        for shot in SHOT.shot_list:
            if shot.rect.colliderect(malko_rect) or shot.rect2.colliderect(malko_rect) or shot.rect3.colliderect(malko_rect):
                shot.delete()
                Malko_count += 1
        if Malko_count > 7:
            Malko = False
            time_elapsed_since_last_action_malko += dt
            
            if time_elapsed_since_last_action_malko > 300:
                    Malko_count = 0
                    Malko = True
                    time_elapsed_since_last_action_malko = 0

        for shot in SHOT.shot_list:
            if shot.rect.colliderect(stefan_rect) or shot.rect2.colliderect(stefan_rect) or shot.rect3.colliderect(
                    stefan_rect):
                shot.delete()
                Stefan_count += 1
        if Stefan_count > 7:
            Stefan = False
            time_elapsed_since_last_action_stefan += dt

            if time_elapsed_since_last_action_stefan > 300:
                Stefan_count = 0
                Stefan = True
                time_elapsed_since_last_action_stefan = 0

        for bug in BUG.bug_list:
            if bug.rect.colliderect(player_rect):
                crash(Count)
                main_loop()
        for pera in PERA.pera_list:
            if pera.rect.colliderect(player_rect):
                effect = pygame.mixer.Sound('{src_dir}\woohoo.wav'.format(src_dir=src_dir))
                effect.play()
                pera.delete()
                create_pera = False
                pera_game = True

        texts("Level: ", l, 1, 570)
        texts("Score: ", Count, 1, 1)

        pygame.display.flip()
        clock.tick(speed)

main_loop()
