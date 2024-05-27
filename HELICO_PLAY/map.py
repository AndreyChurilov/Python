# 0- поле 🟩
# 1 - дерево 🌲
# 2 - река 🌊
# 3 - госпиталь 🏥
# 4 - апгрейд-шоп 🏪
# 5 - огонь🔥

from utils import randbool
from utils import randcell
from utils import randcell2

CELL_TYPES = '🟩🌲🌊🏥🏪🔥'
TREE_BONUS = 100
UPGRADE_COST = 500  
LIVE_COST = 1000  
PENALI_FIRE = 10  #штраф при сгорании дерева

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]  
        self.generate_forest(5,10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop() 
        self.generate_hospital()

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
    def print_map(self, helico, clouds):
        print('⬛️'*(self.w + 2))
        for ri in range(self.h):
            print('⬛️', end = '')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print('🌁', end='')  #ВЫВЕСТИ ОБЛАЧКО
                elif (clouds.cells[ri][ci] == 2):
                    print('⚡', end='')  #ВЫВЕСТИ ГРОЗОВОЕ ОБЛАЧКО
                elif (helico.x == ri and helico.y == ci):
                    print('🚁', end='')  #ВЫВЕСТИ ВЕРТОЛЕТ
                elif ((cell >= 0) and (cell < len(CELL_TYPES)) ):
                    print(CELL_TYPES[cell], end='')  
            print('⬛️')
        print('⬛️'*(self.w + 2))


    #генерация рек l - масимальная блина реки
    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1
    #генерация леса вероятность r из mxr
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r,mxr):
                    self.cells[ri][ci] = 1
    #генерация рандомного дерева
    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1
    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4
    def generate_hospital(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3        
        else:
            self.generate_hospital()

    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]  
        if self.cells[cx][cy] == 1: #если там дерево
            self.cells[cx][cy] = 5   
    def update_fires(self, helico,clouds):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0 #если огонь - обычное поле
                    self.process_helicopter(helico, clouds, True)
        for i in range(5):
            self.add_fire() #добавить новый   

    def process_helicopter(self, helico, clouds, is_fire_penalty = False):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if (c== 2):
            helico.tank = helico.mxtank 
        if (c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if (c == 4 and helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if (c == 3 and helico.score >= LIVE_COST):
            helico.lives += 10
            helico.score -= LIVE_COST    
        if (d == 2):
            helico.lives -= 1  
            if (helico.lives == 0):
                helico.game_over()
        if (is_fire_penalty):
            helico.score -= PENALI_FIRE #теряем очки при сгорании дерева, можно уходить в минус


    def export_data(self):
        return {"cells": self.cells}
    
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)] 










         

    