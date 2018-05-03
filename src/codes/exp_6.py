import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import tkinter as Tk


fig = plt.figure()
axx = plt.axes(xlim=(0, 45), ylim=(0, 800))

datax = []
datay = []
sline, = axx.plot([], [], lw=4)

datax_l = []
datay_l = []
lline, = axx.plot([], [], lw=2)

arr_h = []
arr_a = []
arr_c = []
arr_d = []
arr_b = []
arr_sss = []
ptn = 0


def init():
    global lline, ptn
    lline.set_data([], [])
    ptn = 0


def init_base():
    global datax, datay
    datax = np.linspace(0, 40, 10)
    # Sampling Point
    datay = datax * datax * 0.5 + 1

    tdatax = np.linspace(0, 50, 100)
    tdatay = tdatax * tdatax * 0.5 + 1
    sline.set_data(tdatax, tdatay)
    return


def init_data_l():
    global datax_l, datay_l, datax, datay
    global arr_a, arr_c, arr_h, arr_d, arr_b, arr_sss
    datax_l = np.linspace(0, 40, 100)
    # gen Corresponding data to make a plot
    arr_a.append(0)
    arr_c.append(0)
    arr_b.append(0)
    arr_d.append(0)
    for i in range(0, 10 - 1):
        arr_h.append(datax[i + 1] - datax[i])
    arr_a.append(2 * (arr_h[0] + arr_h[1]))
    for i in range(2, 9):
        arr_a.append(2 * (arr_h[i] + arr_h[i - 1]) - arr_h[i - 1] * arr_h[i - 1] * 1.0 / arr_a[i - 1])
    for i in range(1, 10):
        arr_c.append((datay[i] - datay[i - 1]) * 1.0 / arr_h[i - 1])
    for i in range(1, 9):
        arr_d.append(6 * (arr_c[i + 1] - arr_c[i]))
    arr_b.append(arr_d[1])
    for i in range(2, 9):
        arr_b.append(arr_d[i] - arr_b[i - 1] * arr_h[i - 1] * 1.0 / arr_a[i])
    # lline.set_data(datax_l, datay_l)
    for i in range(0, 10):
        arr_sss.append(0)
    arr_sss[8] = arr_b[8] * 1.0 / arr_a[8] * 1.0
    for i in range(7, 0, -1):
        arr_sss[i] = 1.0 * (arr_b[i] - arr_h[i] * arr_sss[i + 1]) / arr_a[i]
    arr_sss.append(0)
    arr_sss[0] = 0
    pt = 1
    for ix in datax_l:
        if ix > datax[pt]:
            pt = pt + 1
        ss = arr_c[pt] - arr_sss[pt] * arr_h[pt - 1] * 1.0 / 6 - arr_sss[pt - 1] * arr_h[pt - 1] * 1.0 / 3
        ans = datay[pt - 1] + ss * (ix - datax[pt - 1]) + arr_sss[pt - 1] * (ix - datax[pt - 1]) * (
                ix - datax[pt - 1]) * 1.0 / 2 + (arr_sss[pt] - arr_sss[pt - 1]) * (ix - datax[pt - 1]) * (
                      ix - datax[pt - 1]) * (ix - datax[pt - 1]) * 1.0 / (6 * arr_h[pt - 1])
        datay_l.append(ans)
        # print str(ix)+','+str(ans)


def animate(i):
    global ptn
    global sline, lline
    global datax_l, datay_l
    # print datay_n
    if ptn < len(datax_l):
        lline.set_data(datax_l[0:ptn], datay_l[0:ptn])
    ptn = ptn + 1
    if ptn == len(datax_l):
        init()
    return sline, lline


init_base()
init_data_l()
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(datax_l) + 1, interval=100, repeat=false)
plt.show()

anim.save('E:/projs/exp_6.gif', writer = 'imagemagick' , fps=3)
