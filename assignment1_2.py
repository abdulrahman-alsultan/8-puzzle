import queue
from copy import deepcopy
import timeit

q = queue.PriorityQueue()
w = open("output.txt", 'w')

res = []


def write(init):
    count = 0
    for i in range(9):
        w.write(str(init[i]) + ' ')
        count += 1
        if count == 3 or count == 6:
            w.write('\n')
    w.write('\n\n')


def path(init, g):
    for item in res:
        if item[0] == init and item[1] == g:
            print(res.index(item))
            if g == 0:
                write(item[0])
                return
            write(item[0])
            path(item[2], g-1)
            break


def left(tmp):
    if tmp.index(0) == 0 or tmp.index(0) == 3 or tmp.index(0) == 6:
        return False
    index = tmp.index(0)
    tmp[index], tmp[index-1] = tmp[index-1], tmp[index]
    return True


def right(tmp):
    if tmp.index(0) == 2 or tmp.index(0) == 5 or tmp.index(0) == 8:
        return False
    index = tmp.index(0)
    tmp[index], tmp[index+1] = tmp[index+1], tmp[index]
    return True


def up(tmp):
    if tmp.index(0) <= 2:
        return False
    index = tmp.index(0)
    tmp[index], tmp[index - 3] = tmp[index - 3], tmp[index]
    return True


def down(tmp):
    if tmp.index(0) >= 6:
        return False
    index = tmp.index(0)
    tmp[index], tmp[index + 3] = tmp[index + 3], tmp[index]
    return True


def reach_to_goal(init, Goal):
    if init == Goal:
        return True
    return False


def calculate_f(g, init, Goal):
    h = 0
    for i in range(9):
        if init[i] != Goal[i] and init[i] != 0:
            h += 1
    return h+g


f = open("input.txt", 'r')
lines = []
with open("input.txt") as file_in:
    for line in file_in:
        lines.append(line)

timer = timeit.default_timer()
initial = lines[0].split(' ')
goal = lines[2].split(' ')


initial = [int(i) for i in initial]
goal = [int(i) for i in goal]
g = 0
q.put((calculate_f(g, initial, goal), initial, g))
res.append((initial, g, []))
while q:
    p = q.get()
    copy1 = deepcopy(p[1])
    copy2 = deepcopy(p[1])
    copy3 = deepcopy(p[1])
    copy4 = deepcopy(p[1])
    g = p[2] + 1
    if reach_to_goal(p[1], goal):
        stop = timeit.default_timer()
        w.write(str(stop-timer)+"\n")
        write(p[1])
        w.write("\nAI can solve it\n")
        path(p[1], g-1)
        break

    if right(copy4):
        q.put((calculate_f(g, copy4, goal), copy4, g))
        res.append((copy4, g, p[1]))
    if down(copy2):
        q.put((calculate_f(g, copy2, goal), copy2, g))
        res.append((copy2, g, p[1]))
    if up(copy1):
        q.put((calculate_f(g, copy1, goal), copy1, g))
        res.append((copy1, g, p[1]))
    if left(copy3):
        q.put((calculate_f(g, copy3, goal), copy3, g))
        res.append((copy3, g, p[1]))

