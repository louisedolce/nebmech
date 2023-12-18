import math as m
import mathplotlib.piplot as plt

R = 6400
x = [R + 10000]
y = [0]
vx = [0]
vy = [15]
g0 = 10**-2
gM = g0*R**2
h = 0.1

def fvx(vx, x, vy, y):
    r = (x[-1]**2 + y[-1]**2)**0.5
    return(gM*x[-1]/(r)**3)
def fx(vx, x, vy, y):
    return(vx)
def fvy(vx, x, vy, y):
    r = (x[-1]**2 + y[-1]**2)**0.5
    return(gM*y[-1]/(r)**3)
def fy(vx, x, vy, y):
    return(vy)

def fk1(vx, x, vy, y, a):
    if a == 1: # выбор одной из наших 4х функций
        return fvx(vx, x, vy, y)
    elif a == 2:
        return fx(vx, x, vy, y)
    elif a == 3:
        return fvy(vx, x, vy, y)
    elif a == 4:
        return fy(vx, x, vy, y)

def fk2(vx, x, vy, y, a):
    if a == 1:
        return fvx(0, x[-1]+h/2*fk1(vx, x, vy, y, 2), 0, y[-1]+h/2*fk1(vx, x, vy, y, 4))
    elif a == 2:
        return fx(vx[-1]+h/2*fk1(vx, x, vy, y, 1), 0, 0, 0)
    elif a == 3:
        return fvy(0, x[-1]+h/2*fk1(vx, x, vy, y, 2), 0, y[-1]+h/2*fk1(vx, x, vy, y, 4))
    elif a == 4:
        return fy(0, 0, vy[-1]+h/2*fk1(vx, x, vy, y, 3), 0)

def fk3(vx, x, vy, y, a):
    if a == 1:
        return fvx(0, x[-1]+h/2*fk2(vx, x, vy, y, 2), 0, y[-1]+h/2*fk2(vx, x, vy, y, 4))
    elif a == 2:
        return fx(vx[-1]+h/2*fk1(vx, x, vy, y, 1), 0, 0, 0)
    elif a == 3:
        return fvy(0, x[-1]+h/2*fk2(vx, x, vy, y, 2), 0, y[-1]+h/2*fk2(vx, x, vy, y, 4))
    elif a == 4:
        return fy(0, 0, vy[-1]+h/2*fk2(vx, x, vy, y, 3), 0)

def fk4(vx, x, vy, y, a):
    if a == 1:
        return fvx(0, x[-1]+h*fk3(vx, x, vy, y, 2), 0, y[-1]+h*fk3(vx, x, vy, y, 4))
    elif a == 2:
        return fx(vx[-1]+h/2*fk1(vx, x, vy, y, 1), 0, 0, 0)
    elif a == 3:
        return fvy(0, x[-1]+h*fk3(vx, x, vy, y, 2), 0, y[-1]+h*fk3(vx, x, vy, y, 4))
    elif a == 4:
        return fy(0, 0, vy[-1]+h*fk3(vx, x, vy, y, 3), 0)

for t in range(30*60*60*24): #количество секунд в месяце
    summ_vx = vx[-1] + h/6*(fk1(vx, x, vy, y, 1) + 2*fk2(vx, x, vy, y, 1) + 2*fk3(vx, x, vy, y, 1) + fk4(vx, x, vy, y, 1))
    vx.append(summ_vx)
    summ_x = x[-1] + h/6*(fk1(vx, x, vy, y, 2) + 2*fk2(vx, x, vy, y, 2) + 2*fk3(vx, x, vy, y, 2) + fk4(vx, x, vy, y, 2))
    x.append(summ_x)
    summ_vy = vy[-1] + h/6*(fk1(vx, x, vy, y, 3) + 2 * fk2(vx, x, vy, y, 3) + 2 * fk3(vx, x, vy, y, 3) + fk4(vx, x, vy, y, 3))
    vy.append(summ_vy)
    summ_y = y[-1] + h/6*(fk1(vx, x, vy, y, 4) + 2 * fk2(vx, x, vy, y, 4) + 2 * fk3(vx, x, vy, y, 4) + fk4(vx, x, vy, y, 4))
    y.append(summ_y)

plt.scatter(x, y)
plt.show()