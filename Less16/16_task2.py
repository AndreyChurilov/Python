# Создайте класс Черепашка, который хранит позиции x и y черепашки, 
# а также s - количество клеточек, на которое она перемещается за ход /скорость/


class turtle: 
    def __init__(self, x, y, s): 
        self.x = x 
        self.y = y 
        self.s = s 
    
    def go_up(self): 
        self.y += self.s 
    
    def go_down(self): 
        self.y -= self.s 
    
    def go_left(self): 
        self.x -= self.s 
    
    def go_right(self): 
        self.x += self.s 
 
    def evolve(self): 
        self.s += 1 
 
    def degrade(self): 
        if (self.s - 1) <= 0: 
            raise ValueError("Ошибка: скорость черепашки должна быть положительной!") 
        else: 
            self.s -= 1 
 
    def count_moves(self, x2, y2): 
        inc_x = abs(x2 - self.x) 
        inc_y = abs(y2 - self.y) 
        return inc_x//self.s + inc_y//self.s
 
x_start = 10
y_start = 20
s_start = 2 

# создать объект
Rafael = turtle(x_start, y_start, s_start) 
 
# координаты куда 
x_end = 20
y_end = 40
 
# минимальное количество ходов: на примере выше по оси x: 5 действий + 10 действий
min_cnt = Rafael.count_moves(x_end, y_end) 
print(f"Минимальное кол-во действий: {min_cnt}")






