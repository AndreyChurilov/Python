
#испортировать из библиотеки random
#метод randint и обращаться к нему как rand
from random import randint as rand

def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

#генерация случайной клетки
def randcell(w, h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (th, tw)

#генерация случайной соседней клетки
# 0 - верх, 1 - направо, 2 - низ, 3 - налево
def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1,0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)

