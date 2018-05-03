'''
Lagrange 插值算法
目标函数：f(x)=sin(x) x in [0, 2*pi]
为便于演示，插值点由程序等步长生成
'''
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import animation

plt.style.use('ggplot')

fig, ax = plt.subplots()
dots, = ax.plot([], [], 'g')

def init():
    ax.set_ylim(-1.2, 1.2)
    #ax.set_xlim(0, np.pi)
    x = np.arange(-np.pi, np.pi, 0.01)
    y = np.sin(x)
    l = ax.plot(x, y, color='black')

def gen_Lagr_Func():
    x = np.arange(1, np.pi, 0.1)
    y = np.sin(x)
    return (x, y)

def get_val(x):
    S = 0
    length = np.size(xv)
    #print(xv)
    for k in range(0, length):
        yk = yv[k]
        fenzi=1
        fenmu=1
        for i in range(0, length):
            if (i==k):
                continue
            fenzi = fenzi * (x-xv[i])
        #print(fenzi)
        for i in range(0, length):
            if (i==k):
                continue
            fenmu = fenmu * (xv[k]-xv[i])
        S =  S+yk*fenzi/fenmu
        #print(fenzi/fenmu)
    return S

'''
延时绘图
参数类型：np.ndim
'''
def draw(xv, yv, L, R):
    xp = np.arange(L, R, 0.1)
    '''#一个点一个点画，但是每个点都是由插值公式计算得出，动画无大意义
    for i in range(0, np.size(xp)):
        yp = get_val(xp[i])
        ax.plot(xp[i], yp, 'bo')
        plt.pause(0.01)
    for i in range(0, np.size(xv)):
        ax.plot(xv[i], yv[i], 'ro')'''
    
    
    yp=[]
    for i in xp:
        yp.append(get_val(i))
    ax.plot(xp, yp, linestyle = '--', color='r')
    for i in range(0, np.size(xv)):
        ax.plot(xv[i], yv[i], 'yo')
    print(xp[0])
    print(yp[0])
        
    
xv, yv = gen_Lagr_Func()
#print(xv, yv)
init()
draw(xv, yv, 0, np.pi+1)
plt.show()

