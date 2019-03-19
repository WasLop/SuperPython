import pygame
from pygame.locals import * 
from sys import exit
import time
from random import *

pixel = 20

background = pygame.image.load("./images/fild_mario.png")
background_thwomp_right = pygame.image.load("./images/background_thwomp_right.png")
background_thwomp_left = pygame.image.load("./images/background_thwomp_left.png")

init = pygame.image.load("./images/init.png")

game_over = pygame.image.load("./images/game_over.png")

#==============head texture ============================
head_R = pygame.image.load("./images/head_right.png")
head_L = pygame.image.load("./images/head_left.png")
head_U = pygame.image.load("./images/head_up.png")
head_D = pygame.image.load("./images/head_down.png")

mouth_R = pygame.image.load("./images/mouth_right.png")
mouth_L = pygame.image.load("./images/mouth_left.png")
mouth_U = pygame.image.load("./images/mouth_up.png")
mouth_D = pygame.image.load("./images/mouth_down.png")


#==============tail texture =============================
tail_R = pygame.image.load("./images/tail_right.png")
tail_L = pygame.image.load("./images/tail_left.png")
tail_U = pygame.image.load("./images/tail_up.png")
tail_D = pygame.image.load("./images/tail_down.png")

#==============body texture =============================
#style 1
body1_R = pygame.image.load("./images/body1_right.png")
body1_L = pygame.image.load("./images/body1_left.png")
body1_U = pygame.image.load("./images/body1_up.png")
body1_D = pygame.image.load("./images/body1_down.png")

#style 2
body2_R = pygame.image.load("./images/body2_right.png")
body2_L = pygame.image.load("./images/body2_left.png")
body2_U = pygame.image.load("./images/body2_up.png")
body2_D = pygame.image.load("./images/body2_down.png")

#digestion
digestion_x = pygame.image.load("./images/digestion_x.png")
digestion_y = pygame.image.load("./images/digestion_y.png")


#bendy
bend1 = pygame.image.load("./images/bend1.png")
bend2 = pygame.image.load("./images/bend2.png")
bend3 = pygame.image.load("./images/bend3.png")
bend4 = pygame.image.load("./images/bend4.png")

#bend_digestion
bend_digestion1 = pygame.image.load("./images/bend_digestion1.png")
bend_digestion2 = pygame.image.load("./images/bend_digestion2.png")
bend_digestion3 = pygame.image.load("./images/bend_digestion3.png")
bend_digestion4 = pygame.image.load("./images/bend_digestion4.png")

mushroom_png = pygame.image.load("./images/mushroom.png")
egg_png = pygame.image.load("./images/egg.png")
flower_png = pygame.image.load("./images/flower.png")

thwomp_right = pygame.image.load("./images/thwomp_right.png")
thwomp_left = pygame.image.load("./images/thwomp_left.png")
thwomp_bad_right = pygame.image.load("./images/thwomp_bad_right.png")
thwomp_bad_left = pygame.image.load("./images/thwomp_bad_left.png")

boo_right = pygame.image.load("./images/boo_right.gif")
boo_left = pygame.image.load("./images/boo_left.gif")
boo_right_hidden = pygame.image.load("./images/boo_right.png")
boo_left_hidden = pygame.image.load("./images/boo_left.png")

hull = pygame.image.load("./images/hull_red.png")

bool_U = pygame.image.load("./images/hull_red.png")
bool_D = pygame.image.load("./images/hull_red.png")

#snake object
class SnakeClass (object):
    def __init__(self, head):
        self.head = head
        self.head_tex = head_R
        self.body = []
        self.body_tex = []
        tail = head[0] -pixel, head[1]
        self.tail = tail
        self.tail_tex = tail_R
        self.size = pixel,pixel
        self.special = False
        self.help_special = False

    def moviment_mouth(self, Food, close_mouth):
        if self.head[0] + pixel == Food.pos[0] and self.head[1] == Food.pos[1]:
            if self.head_tex == head_R:
                self.head_tex = mouth_R
            elif self.head_tex == head_D:
                self.head_tex = mouth_D
            elif self.head_tex == head_U:
                self.head_tex = mouth_U
            close_mouth = False
        elif self.head[0] - pixel == Food.pos[0] and self.head[1] == Food.pos[1]:
            if self.head_tex == head_L:
                self.head_tex = mouth_L
            elif self.head_tex == head_D:
                self.head_tex = mouth_D
            elif self.head_tex == head_U:
                self.head_tex = mouth_U
            close_mouth = False
        elif self.head[1] + pixel == Food.pos[1] and self.head[0] == Food.pos[0]:
            if self.head_tex == head_D:
                self.head_tex = mouth_D
            elif self.head_tex == head_R:
                self.head_tex = mouth_R
            elif self.head_tex == head_L:
                self.head_tex = mouth_L
            close_mouth = False
        elif self.head[1] - pixel == Food.pos[1] and self.head[0] == Food.pos[0]:
            if self.head_tex == head_U:
                self.head_tex = mouth_U
            elif self.head_tex == head_L:
                self.head_tex = mouth_L
            elif self.head_tex == head_R:
                self.head_tex = mouth_R
            close_mouth = False

        if close_mouth:
            if self.head_tex == mouth_R:
                self.head_tex = head_R
            elif self.head_tex == mouth_L:
                self.head_tex = head_L
            elif self.head_tex == mouth_D:
                self.head_tex = head_D
            elif self.head_tex == mouth_U:
                self.head_tex = head_U
        return close_mouth
    
    def eat(self,pos_prev):

        new_body = self.tail
        self.tail = pos_prev
        self.body.append(new_body)
        self.body_tex.append(body2_U)

    
    def direction(self,head):
        pos_prev = head
        tail = head
        if len(self.body) >= 1:
            cont = 1
            help_pos = pos_prev
            tail = self.body[0]
            pos_prev = self.body[0]
            self.body[0]= head

            while cont < len(self.body):
                help_pos = self.body[cont]
                self.body[cont] = pos_prev
                pos_prev = help_pos
                tail = pos_prev
                cont += 1

        self.tail = tail

    def texture_adapter(self,help_body):
        help_tex_body = help_body

        if len(self.body) > 0:
            pos_prev = self.body[0]
            if len(self.body) == 1:

                if self.body[0][0] < self.head[0]:
                    if self.body[0][0] > self.tail[0]:
                        if help_body:
                            self.body_tex[0] = body1_R
                            help_tex_body = False
                        else:
                            self.body_tex[0] = body2_R
                            help_tex_body = True

                        self.tail_tex = tail_R
                    elif self.body[0][1] > self.tail[1]:
                        self.body_tex[0] = bend4
                        self.tail_tex = tail_D
                    elif self.body[0][1] < self.tail[1]:
                        self.body_tex[0] = bend1
                        self.tail_tex = tail_U
                elif self.body[0][0] > self.head[0]:
                    if self.body[0][0] < self.tail[0]:
                        if help_body:
                            self.body_tex[0] = body1_L
                            help_tex_body = False
                        else:
                            self.body_tex[0] = body2_L
                            help_tex_body = True

                        self.tail_tex = tail_L
                    elif self.body[0][1] > self.tail[1]:
                        self.body_tex[0] = bend3
                        self.tail_tex = tail_D
                    elif self.body[0][1] < self.tail[1]:
                        self.body_tex[0] = bend2
                        self.tail_tex = tail_U
                elif self.body[0][1] < self.head[1]:
                    if self.body[0][1] > self.tail[1]:
                        if help_body:
                            self.body_tex[0] = body1_D
                            help_tex_body = False
                        else:
                            self.body_tex[0] = body2_D
                            help_tex_body = True

                        self.tail_tex = tail_D
                    elif self.body[0][0] > self.tail[0]:
                        self.body_tex[0] = bend2
                        self.tail_tex = tail_R
                    elif self.body[0][0] < self.tail[0]:
                        self.body_tex[0] = bend1
                        self.tail_tex = tail_L
                elif self.body[0][1] > self.head[1]:
                    if self.body[0][1] < self.tail[1]:
                        if help_body:
                            self.body_tex[0] = body1_U
                            help_tex_body = False
                        else:
                            self.body_tex[0] = body2_U
                            help_tex_body = True

                        self.tail_tex = tail_U
                    elif self.body[0][0] > self.tail[0]:
                        self.body_tex[0] = bend3
                        self.tail_tex = tail_R
                    elif self.body[0][0] < self.tail[0]:
                        self.body_tex[0] = bend4
                        self.tail_tex = tail_L

            elif len(self.body) > 1:
                cont = 0

                if self.body[0][0] < self.head[0]:
                    if self.body[0][0] > self.body[1][0]:
                        if help_body:
                            self.body_tex[0] = body1_R
                            help_tex_body = False
                            help_body = False
                        else:
                            self.body_tex[0] = body2_R
                            help_tex_body = True
                            help_body = True

                    elif self.body[0][1] > self.body[1][1]:
                        self.body_tex[0] = bend4

                    elif self.body[0][1] < self.body[1][1]:
                        self.body_tex[0] = bend1

                elif self.body[0][0] > self.head[0]:
                    if self.body[0][0] < self.body[1][0]:
                        if help_body:
                            self.body_tex[0] = body1_L
                            help_tex_body = False
                            help_body = False
                        else:
                            self.body_tex[0] = body2_L
                            help_tex_body = True
                            help_body = True


                    elif self.body[0][1] > self.body[1][1]:
                        self.body_tex[0] = bend3

                    elif self.body[0][1] < self.body[1][1]:
                        self.body_tex[0] = bend2

                elif self.body[0][1] < self.head[1]:
                    if self.body[0][1] > self.body[1][1]:
                        if help_body:
                            self.body_tex[0] = body1_D
                            help_tex_body = False
                            help_body = False
                        else:
                            self.body_tex[0] = body2_D
                            help_tex_body = True
                            help_body = True

                    elif self.body[0][0] > self.body[1][0]:
                        self.body_tex[0] = bend2

                    elif self.body[0][0] < self.body[1][0]:
                        self.body_tex[0] = bend1

                elif self.body[0][1] > self.head[1]:
                    if self.body[0][1] < self.body[1][1]:
                        if help_body:
                            self.body_tex[0] = body1_U
                            help_tex_body = False
                            help_body = False

                        else:
                            self.body_tex[0] = body2_U
                            help_tex_body = True
                            help_body = True

                    elif self.body[0][0] > self.body[1][0]:
                        self.body_tex[0] = bend3

                    elif self.body[0][0] < self.body[1][0]:
                        self.body_tex[0] = bend4

                for pos in self.body:
                    if cont < (len(self.body) - 1):
                        if pos[0] < pos_prev[0]:
                            if pos[0] > self.body[cont+1][0]:
                                if help_body:
                                    self.body_tex[cont] = body1_R
                                    help_body = False
                                else:
                                    self.body_tex[cont] = body2_R
                                    help_body = True

                            elif pos[1] < self.body[cont+1][1]:
                                self.body_tex[cont] = bend1

                            elif pos[1] > self.body[cont+1][1]:
                                self.body_tex[cont] = bend4

                        elif pos[0] > pos_prev[0]:
                            if pos[0] < self.body[cont+1][0]:
                                if help_body:
                                    self.body_tex[cont] = body1_L
                                    help_body = False
                                else:
                                    self.body_tex[cont] = body2_L
                                    help_body = True

                            elif pos[1] < self.body[cont+1][1]:
                                self.body_tex[cont] = bend2
                                self.tail_tex = tail_U

                            elif pos[1] > self.body[cont+1][1]:
                                self.body_tex[cont] = bend3

                        elif pos[1] < pos_prev[1]:
                            if pos[1] > self.body[cont+1][1]:
                                if help_body:
                                    self.body_tex[cont] = body1_D
                                    help_body = False
                                else:
                                    self.body_tex[cont] = body2_D
                                    help_body = True

                            elif pos[0] < self.body[cont+1][0]:
                                self.body_tex[cont] = bend1

                            elif pos[0] > self.body[cont+1][0]:
                                self.body_tex[cont] = bend2

                        elif pos[1] > pos_prev[1]:
                            if pos[1] < self.body[cont+1][1]:
                                if help_body:
                                    self.body_tex[cont] = body1_U
                                    help_body = False
                                else:
                                    self.body_tex[cont] = body2_U
                                    help_body = True

                            elif pos[0] < self.body[cont+1][0]:
                                self.body_tex[cont] = bend4

                            elif pos[0] > self.body[cont+1][0]:
                                self.body_tex[cont] = bend3

                    else:
                        if pos[0] < pos_prev[0]:
                            if pos[0] > self.tail[0]:
                                if help_body:
                                    self.body_tex[cont] = body1_R
                                    help_body = False
                                else:
                                    self.body_tex[cont] = body2_R
                                    help_body = True
                                self.tail_tex = tail_R
                            elif pos[1] < self.tail[1]:
                                self.body_tex[cont] = bend1
                                self.tail_tex = tail_U

                            elif pos[1] > self.tail[1]:
                                self.body_tex[cont] = bend4
                                self.tail_tex = tail_D
                        elif pos[0] > pos_prev[0]:
                            if pos[0] < self.tail[0]:
                                if help_body:
                                    self.body_tex[cont] = body1_L
                                    help_body = False
                                else:
                                    self.body_tex[cont] = body2_L
                                    help_body = True
                                self.tail_tex = tail_L
                            elif pos[1] < self.tail[1]:
                                self.body_tex[cont] = bend2
                                self.tail_tex = tail_U

                            elif pos[1] > self.tail[1]:
                                self.body_tex[cont] = bend3
                                self.tail_tex = tail_D

                        elif pos[1] < pos_prev[1]:
                            if pos[1] > self.tail[1]:
                                if help_body:
                                    self.body_tex[cont] = body1_D
                                    help_body = False
                                else:
                                    self.body_tex[cont] = body2_D
                                    help_body = True
                                self.tail_tex = tail_D
                            elif pos[0] < self.tail[0]:
                                self.body_tex[cont] = bend1
                                self.tail_tex = tail_L

                            elif pos[0] > self.tail[0]:
                                self.body_tex[cont] = bend2
                                self.tail_tex = tail_R

                        elif pos[1] > pos_prev[1]:
                            if pos[1] < self.tail[1]:
                                if help_body:
                                    self.body_tex[cont] = body1_U
                                    help_body = False
                                else:
                                    self.body_tex[cont] = body2_U
                                    help_body = True
                                self.tail_tex = tail_U
                            elif pos[0] < self.tail[0]:
                                self.body_tex[cont] = bend4
                                self.tail_tex = tail_L

                            elif pos[0] > self.tail[0]:
                                self.body_tex[cont] = bend3
                                self.tail_tex = tail_R

                    pos_prev = pos
                    cont += 1


        else:
            if self.tail[0] > self.head[0]:
                self.tail_tex = tail_L
            elif self.tail[0] < self.head[0]:
                self.tail_tex = tail_R
            elif self.tail[1] > self.head[1]:
                self.tail_tex = tail_U
            elif self.tail[1] < self.head[1]:
                self.tail_tex = tail_D

        return help_tex_body

    def digestion(self,food_lista):
        cont = 0
        cont_food = 0


        while True:
            if cont_food < len(food_lista) and cont < len(self.body):
                if self.body[cont] == food_lista[cont_food]:

                    if self.body_tex[cont] == body1_R or self.body_tex[cont] == body2_R or self.body_tex[cont] == body1_L or self.body_tex[cont] == body2_L:
                        self.body_tex[cont] = digestion_x
                    elif self.body_tex[cont] == body1_U or self.body_tex[cont] == body2_U or self.body_tex[cont] == body1_D or self.body_tex[cont] == body2_D:
                        self.body_tex[cont] = digestion_y
                    elif self.body_tex[cont] == bend1:
                        self.body_tex[cont] = bend_digestion1
                    elif self.body_tex[cont] == bend2:
                        self.body_tex[cont] = bend_digestion2
                    elif self.body_tex[cont] == bend3:
                        self.body_tex[cont] = bend_digestion3
                    elif self.body_tex[cont] == bend4:
                        self.body_tex[cont] = bend_digestion4
                    cont_food += 1
                    cont = 0
            else:
                break
            cont += 1

    def walk(self, pos_prev, help_walk):
        if pos_prev != self.head:
            x,y = self.head

            if pos_prev[0] < self.head[0]:
                if help_walk:
                    pos_prev = self.head
                    x += pixel
            elif pos_prev[0] > self.head[0]:
                if help_walk:
                    pos_prev = self.head
                    x -= pixel
            elif pos_prev[1] < self.head[1]:
                if help_walk:
                    pos_prev = self.head
                    y += pixel
            elif pos_prev[1] > self.head[1]:
                if help_walk:
                    pos_prev = self.head
                    y -= pixel

            self.head = x,y
            self.direction(pos_prev)

    def prinr(self,help_pos_x, help_pos_y):
        screen.blit(self.head_tex, ((self.head[0] - help_pos_x), (self.head[1] - help_pos_y)))
        cont_body = 0
        for vertebra in self.body:
            screen.blit(self.body_tex[cont_body], vertebra)
            cont_body += 1
        screen.blit(self.tail_tex, self.tail)

    def special_test (self):
        global head_R
        global head_L
        global head_U
        global head_D
        global mouth_R
        global mouth_L
        global mouth_U
        global mouth_D
        global tail_R
        global tail_L
        global tail_U
        global tail_D
        global body1_R
        global body1_L
        global body1_U
        global body1_D
        global body2_R
        global body2_L
        global body2_U
        global body2_D
        global digestion_x
        global digestion_y
        global bend1
        global bend2
        global bend3
        global bend4
        global bend_digestion1
        global bend_digestion2
        global bend_digestion3
        global bend_digestion4

        if self.special and self.help_special:
            self.help_special = False        
            head_R = pygame.image.load("./images/head_piton_right.png")
            head_L = pygame.image.load("./images/head_piton_left.png")
            head_U = pygame.image.load("./images/head_piton_up.png")
            head_D = pygame.image.load("./images/head_piton_down.png")
            mouth_R = pygame.image.load("./images/mouth_piton_right.png")
            mouth_L = pygame.image.load("./images/mouth_piton_left.png")
            mouth_U = pygame.image.load("./images/mouth_piton_up.png")
            mouth_D = pygame.image.load("./images/mouth_piton_down.png")
            tail_R = pygame.image.load("./images/tail_piton_right.png")
            tail_L = pygame.image.load("./images/tail_piton_left.png")
            tail_U = pygame.image.load("./images/tail_piton_up.png")
            tail_D = pygame.image.load("./images/tail_piton_down.png")

            body1_R = pygame.image.load("./images/body1_piton_right.png")
            body1_L = pygame.image.load("./images/body1_piton_left.png")
            body1_U = pygame.image.load("./images/body1_piton_up.png")
            body1_D = pygame.image.load("./images/body1_piton_down.png")

            body2_R = pygame.image.load("./images/body2_piton_right.png")
            body2_L = pygame.image.load("./images/body2_piton_left.png")
            body2_U = pygame.image.load("./images/body2_piton_up.png")
            body2_D = pygame.image.load("./images/body2_Piton_down.png")

            digestion_x = pygame.image.load("./images/digestion_piton_x.png")
            digestion_y = pygame.image.load("./images/digestion_piton_y.png")


            bend1 = pygame.image.load("./images/bend1_piton.png")
            bend2 = pygame.image.load("./images/bend2_piton.png")
            bend3 = pygame.image.load("./images/bend3_piton.png")
            bend4 = pygame.image.load("./images/bend4_piton.png")

            bend_digestion1 = pygame.image.load("./images/bend_digestion1_piton.png")
            bend_digestion2 = pygame.image.load("./images/bend_digestion2_piton.png")
            bend_digestion3 = pygame.image.load("./images/bend_digestion3_piton.png")
            bend_digestion4 = pygame.image.load("./images/bend_digestion4_piton.png")

            if len(self.body) > 0:
                if self.head[0] > self.body[0][0]:
                    self.head_tex = head_R
                elif self.head[0] < self.body[0][0]:
                    self.head_tex = head_L
                elif self.head[1] < self.body[0][1]:
                    self.head_tex = head_U
                elif self.head[1] > self.body[0][1]:
                    self.head_tex = head_D
            
        elif not self.special and not self.help_special:
            self.help_special = True
            
            head_R = pygame.image.load("./images/head_right.png")
            head_L = pygame.image.load("./images/head_left.png")
            head_U = pygame.image.load("./images/head_up.png")
            head_D = pygame.image.load("./images/head_down.png")

            mouth_R = pygame.image.load("./images/mouth_right.png")
            mouth_L = pygame.image.load("./images/mouth_left.png")
            mouth_U = pygame.image.load("./images/mouth_up.png")
            mouth_D = pygame.image.load("./images/mouth_down.png")

            tail_R = pygame.image.load("./images/tail_right.png")
            tail_L = pygame.image.load("./images/tail_left.png")
            tail_U = pygame.image.load("./images/tail_up.png")
            tail_D = pygame.image.load("./images/tail_down.png")

            body1_R = pygame.image.load("./images/body1_right.png")
            body1_L = pygame.image.load("./images/body1_left.png")
            body1_U = pygame.image.load("./images/body1_up.png")
            body1_D = pygame.image.load("./images/body1_down.png")

            body2_R = pygame.image.load("./images/body2_right.png")
            body2_L = pygame.image.load("./images/body2_left.png")
            body2_U = pygame.image.load("./images/body2_up.png")
            body2_D = pygame.image.load("./images/body2_down.png")
            digestion_x = pygame.image.load("./images/digestion_x.png")
            digestion_y = pygame.image.load("./images/digestion_y.png")

            bend1 = pygame.image.load("./images/bend1.png")
            bend2 = pygame.image.load("./images/bend2.png")
            bend3 = pygame.image.load("./images/bend3.png")
            bend4 = pygame.image.load("./images/bend4.png")
            
            bend_digestion1 = pygame.image.load("./images/bend_digestion1.png")
            bend_digestion2 = pygame.image.load("./images/bend_digestion2.png")
            bend_digestion3 = pygame.image.load("./images/bend_digestion3.png")
            bend_digestion4 = pygame.image.load("./images/bend_digestion4.png")

            if len(self.body) > 0:
                if self.head[0] > self.body[0][0]:
                    self.head_tex = head_R
                elif self.head[0] < self.body[0][0]:
                    self.head_tex = head_L
                elif self.head[1] < self.body[0][1]:
                    self.head_tex = head_U
                elif self.head[1] > self.body[0][1]:
                    self.head_tex = head_D
            else:
                self.head_tex = head_R
class FoodClass (object):
    def __init__(self,text, pos, points):
        self.pos = pos
        self.help_pos = False
        self.size = (pixel,pixel)
        self.text = text
        self.points = points
    
    def spawn (self, Snake):
        if self.help_pos:
            while self.help_pos:
                self.pos = ((randint(20, (760 / pixel))) * pixel, 40+((randint(0, (520 / pixel))) * pixel))
                if self.pos != Snake.head and self.pos != Snake.tail:
                    for pos in Snake.body:
                        if self.pos == pos:
                            break
                    else:
                        self.help_pos = False

    def print (self):
        screen.blit(self.text, self.pos)

def test_collision(Snake,Thwomp_right,Thwomp_left):

    if Snake.head[1] >= 80 and Snake.head[1] < 580:
        if Snake.head == Snake.tail:
            return False
        else:
            for vertebra in Snake.body:
                if Snake.head == vertebra:
                    return False
            else:
                return True
    elif Snake.head[0] >=20 and Snake.head[0] < 780 and Snake.head[1] >=40 and Snake.head[1] < 80:
        if Snake.head == Snake.tail:
            return False
        else:
            for vertebra in Snake.body:
                if Snake.head == vertebra:
                    return False
            else:
                return True

    else:
        return False

class Score_class (object):
    def __init__(self):
        self.points = 0
        self.top_50 = self.points
        self.help_decrement = 0
        self.pos = 775
        self.Special = False

    def increment(self,valor):
        self.points += valor

    def decrement(self,valor):
        self.points -= valor

    def veloity (self, velocity):
        if self.points - self.top_50 >= 50:
            self.top_50 += 50
            velocity -= 0.02
        return velocity

    def print (self,label, y):
        screen.blit(label, (self.pos, y))

class Thwomp_class (object):
    def __init__(self, text,pos_x):
        self.text = text
        self.pos = (pos_x,40)

    def cair (self,pos_x, Snake):
        cont = float(self.pos[1])
        if Snake.head[1] < 80:
            return  False
        else:
            while self.pos[1] < Snake.head[1] - 39:
                cont += 2
                self.pos = pos_x, cont
                if pos_x == 0:
                    screen.blit(background_thwomp_left, (0, 40))
                    Snake.prinr(5,0)
                else:
                    screen.blit(background_thwomp_right, (780, 40))
                    Snake.prinr(0,0)
                screen.blit(self.text,self.pos)
                pygame.display.update()

            return False

    def bad (self,pos_x):
        if self.pos[0] == 780:
            if pos_x > 690:
                self.text = thwomp_bad_right
            else:
                self. text = thwomp_right
        else:
            if pos_x < 100:
                self.text = thwomp_bad_left
            else:
                self. text = thwomp_left

class killers_class (object):
    def __init__(self, tex):
        self.pos = (0,800)
        self.tex = tex
        self.timer = 0

    def hidden (self, Snake):
        if Snake.head[0] >= self.pos[0]:
            if Snake.head_tex == head_L or Snake.head_tex == mouth_L:
                self.tex = boo_right_hidden
            else:
                if Snake.head[1] >= self.pos[1]:
                    if Snake.head_tex == head_U or Snake.head_tex == mouth_U:
                        self.tex = boo_right_hidden
                    else:
                        self.tex = boo_right
                elif Snake.head[1] <= self.pos[1]:
                    if Snake.head_tex == head_D or Snake.head_tex == mouth_D:
                        self.tex = boo_right_hidden
                    else:
                        self.tex = boo_right
                else:
                    self.tex = boo_right

        elif Snake.head[0] <= self.pos[0]:
            if Snake.head_tex == head_R or Snake.head_tex == mouth_R:
                self.tex = boo_left_hidden
            else:
                if Snake.head[1] >= self.pos[1]:
                    if Snake.head_tex == head_U or Snake.head_tex == mouth_U:
                        self.tex = boo_left_hidden
                    else:
                        self.tex = boo_left
                elif Snake.head[1] <= self.pos[1]:
                    if Snake.head_tex == head_D or Snake.head_tex == mouth_D:
                        self.tex = boo_left_hidden
                    else:
                        self.tex = boo_left
                else:
                    self.tex = boo_left

    def spawn (self,Snake):
        help_pos = True

        while help_pos:
            self.pos = ((randint(20, (760 / pixel))) * pixel, 40 + ((randint(0, (520 / pixel))) * pixel))
            if self.pos != Snake.head and self.pos != Snake.tail:
                for pos in Snake.body:
                    if self.pos == pos:
                        break
                else:
                    help_pos = False

    def kill (self, Snake):
        if Snake.head == self.pos:
            return False
        else:
            return True

    def print(self):
        screen.blit(self.tex,self.pos)



pygame.init() 

screen = pygame.display.set_mode((800, 600), 0, 32)

while True:

    pointer = (320,260)
    play = True
    while play:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if pointer == (320,260):
                        pointer = (320, 350)
                    else:
                        pointer = (320, 260)
                elif event.key == K_DOWN:
                    if pointer == (320,260):
                        pointer = (320, 350)
                    else:
                        pointer = (320, 260)
                elif event.key == K_RETURN:
                    if pointer == (320,260):
                        play = False
                    else:
                        pointer = (320, 260)
                        pygame.quit()
                        exit()
        screen.blit(init, (0, 0))
        pygame.draw.polygon(screen,(0,0,0),(pointer, (pointer[0],pointer[1] + 40),(pointer[0] + 40,pointer[1] + 20)),0)
        pygame.display.update()

    myfont = pygame.font.SysFont("Rosewood Std Regular", 30)

    vel = 0.2
    collision = True
    percent_food = 50
    help_x = True
    help_y = True
    x, y = 400, 300
    pos_prev = 0, 0
    head = (x, y)
    open_m = False

    Mushroom = FoodClass(mushroom_png,((randint(20, (760 / pixel))) * pixel, 40+((randint(0, (520 / pixel))) * pixel)),10)
    Flower = FoodClass(flower_png,(0,800),25)
    Egg = FoodClass(egg_png,(0,800),50)
    Snake = SnakeClass(head)
    Score = Score_class()
    steps = 0
    help_tex_body = True
    help_eat = False
    help_food = False
    pos_food = []
    help_pos_x = 0
    help_pos_y = 0
    prev_score = Score.points
    Thwomp_left = Thwomp_class(thwomp_left,0)
    Thwomp_right = Thwomp_class(thwomp_right,780)
    Boo = killers_class(boo_left)
    list_hulls = []

    while collision:
        time.sleep(vel)

        if (not open_m):
            close_mouth = True

        help_walk = True

        if len(str(Score.points)) > len(str(prev_score)):
            Score.pos -= 11
        screen.blit(background, (0, 0))
        prev_score = Score.points
        label = myfont.render(str(Score.points), 1, (0, 0, 0))
        Score.print(label,6)

        #pygame.draw.rect(screen, Mouse.color, (Mouse.pos, Mouse.size))
        Mushroom.print()
        Flower.print()
        Egg.print()
        Boo.hidden(Snake)
        Thwomp_left.bad(Snake.head[0])
        Thwomp_right.bad(Snake.head[0])

        help_tex_body = Snake.texture_adapter(help_tex_body)
        if len(pos_food) > 0:
            Snake.digestion(pos_food)

        if len (list_hulls) > 0:
            for Hull in list_hulls:
                screen.blit(Hull.tex, Hull.pos)

        Snake.prinr(help_pos_x,help_pos_y)
        Boo.print()

        screen.blit(Thwomp_left.text,Thwomp_left.pos)
        screen.blit(Thwomp_right.text,Thwomp_right.pos)

        if Snake.head[0] == 780:
            collision = Thwomp_right.cair(780,Snake)
        elif Snake.head[0] == 0:
            collision = Thwomp_left.cair(0,Snake)

        Mushroom.help_pos = Mushroom.spawn(Snake)
        if 3 < percent_food <= 10 :
            percent_food = 100
            Egg.points = 25
            Egg.help_pos = Flower.help_pos = Egg.spawn(Snake)
            steps +=1

        elif percent_food < 4:
            percent_food = 100
            Flower.points = 50
            Egg.help_pos = Flower.help_pos = Flower.spawn(Snake)
            steps +=1
        elif 10 < percent_food < 21:
            percent_food = 100
            if Boo.timer == 0:
                Boo.timer +=1
            Boo.spawn(Snake)

        if help_eat:

            Snake.eat(pos_prev)
            help_eat = False


        pos_prev = Snake.tail
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT and help_x or event.key == K_a:
                    x -= pixel
                    head = Snake.head
                    Snake.head = x,y
                    Snake.head_tex = head_L

                    help_pos_x = 5
                    help_pos_y = 0
                    help_y = True
                    help_x = False
                    help_walk = False
                    break

                elif event.key == K_RIGHT and help_x or event.key == K_d:

                    x += pixel
                    head = Snake.head
                    Snake.head = x,y
                    Snake.head_tex = head_R

                    help_pos_x = 0
                    help_pos_y = 0
                    help_y = True
                    help_x = False
                    help_walk = False
                    break

                elif event.key == K_UP and help_y or event.key == K_w:
                    y -= pixel
                    head = Snake.head
                    Snake.head = x,y
                    Snake.head_tex = head_U

                    help_pos_y = 5
                    help_pos_x = 0
                    help_y = False
                    help_x = True
                    help_walk = False
                    break

                elif event.key == K_DOWN and help_y or event.key == K_s:
                    y += pixel
                    head = Snake.head
                    Snake.head = x,y
                    Snake.head_tex = head_D

                    help_pos_y = 0
                    help_pos_x = 0
                    help_y = False
                    help_x = True
                    help_walk = False
                    break
                elif event.key == K_SPACE and Snake.special:

                    if Snake.head_tex == head_R or Snake.head_tex == mouth_R:
                        print("cu")
                        Snake.head_tex = mouth_R
                    if Snake.head_tex == head_L or Snake.head_tex == mouth_L:
                        Snake.head_tex = mouth_L
                    if Snake.head_tex == head_U or Snake.head_tex == mouth_U:
                        Snake.head_tex = mouth_U
                    if Snake.head_tex == head_D or Snake.head_tex == mouth_D:
                        Snake.head_tex = mouth_D
                    open_m = True
                    close_mouth = False
                    break
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    open_m = False

        pygame.display.update()
        Snake.walk(head, help_walk)
        close_mouth = Snake.moviment_mouth(Mushroom, close_mouth)
        close_mouth = Snake.moviment_mouth(Flower, close_mouth)
        close_mouth = Snake.moviment_mouth(Egg, close_mouth)
        x,y = Snake.head
        if Snake.head == Mushroom.pos:
            Score.increment(Mushroom.points)
            Mushroom.help_pos = True
            Flower.help_pos = Egg.help_pos = True
            Flower.pos = (0,800)
            Egg.pos = (0,800)
            percent_food = randint(0, 100)
            Mushroom.points = 10
            pos_food.append(Mushroom.pos)
            steps = 0

        elif Snake.head == Egg.pos:
            Score.increment(Egg.points)
            pos_food.append(Egg.pos)
            Egg.pos = (0,800)
            percent_food = 100
            Flower.help_pos = Egg.help_pos = True
            steps = 0

        elif Snake.head == Flower.pos:
            Snake.special = True
            Score.increment(Flower.points)
            pos_food.append(Flower.pos)
            Flower.pos = (0, 800)
            percent_food = 100
            Flower.help_pos = Egg.help_pos = True
            steps = 0
            if Snake.special:
                vel += 0.04
        elif steps == 50:
            Egg.pos = Flower.pos = (0,800)
            steps = 0

        if len(pos_food) > 0:
            if Snake.tail == pos_food[0]:
                help_eat = True
                if 0 <= randint(0, 100) <= 15:
                    Hull = killers_class(hull)
                    Hull.pos = pos_food[0]
                    list_hulls.append(Hull)
                del(pos_food[0])

        if Boo.timer == 100:
            Boo.timer = 0
            Boo.pos = (0,800)

        i_coll = 0
        if collision:
            while collision:
                if i_coll == 0:
                    collision = test_collision(Snake,Thwomp_right,Thwomp_left)
                elif i_coll == 1:
                    collision = Boo.kill(Snake)
                elif i_coll == 2:
                    if len (list_hulls) > 0:
                        cont_hull = 0
                        for Hull in list_hulls:
                            collision = Hull.kill(Snake)
                            if not collision and open_m:
                                collision = True
                                del (list_hulls[cont_hull])
                            if not collision:
                                break
                            cont_hull +=1
                else:
                    break
                i_coll += 1
            else:
                if Snake.special and not collision:
                    time.sleep(0.2)
                    Snake.special = False
                    collision = True
                    if Snake.head == Boo.pos:
                        Boo.pos = (0,800)
                    else:
                        cont_hull = 0
                        for Hull in list_hulls:
                            if Snake.head == Hull.pos and not open_m:
                                del(list_hulls[cont_hull])

                                break

                            cont_hull +=1

        pygame.display.update()

        if Score.help_decrement == 10:
            if Mushroom.points > 2:
                Mushroom.points -=1
            if Egg.points > 5:
                Egg.points -= 3
            if Flower.points > 10:
                Flower.points -= 5
            Score.help_decrement = 0
        if Boo.timer > 0:
            Boo.timer += 1

        if steps > 0:
            steps +=1
        Score.help_decrement +=1
        if vel > 0.08:
            vel = Score.veloity(vel)

        Snake.special_test()

    myfont = pygame.font.SysFont("Rosewood Std Regular", 100)
    label = myfont.render("Score: " + str(Score.points), 1, (0, 0, 0))
    Score.pos = 250
    game_over_while = True
    while game_over_while:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    game_over_while = False

        screen.blit(game_over, (150, 100))
        Score.print(label,400)
        pygame.display.update()
