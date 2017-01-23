#coding:utf-8
#蒙提霍尔验证
import random

def MontyHall(Dselect,Dchange):
    Dcar = random.randint(1,3)
    if Dcar == Dselect and Dchange == 0:
        return 1
    elif Dcar!=Dselect and Dchange == 0:
        return 0
    elif Dcar == Dselect and Dchange ==1:
        return 0
    else:
        return 1

#不确定是否改变选择
n = 10000
win = 0
for i in range(n):
    Dselect = random.randint(1,3)
    Dchange = random.randint(0,1)
    win = win + MontyHall(Dselect,Dchange)
print float(win)/float(n)

#确定不改变选择
n = 10000
win = 0
for i in range(n):
    Dselect = random.randint(1,3)
    Dchange = 0
    win = win + MontyHall(Dselect,Dchange)
print float(win)/float(n)

#确定改变选择
n = 10000
win = 0
for i in range(n):
    Dselect = random.randint(1,3)
    Dchange = 1
    win = win + MontyHall(Dselect,Dchange)
print float(win)/float(n)


