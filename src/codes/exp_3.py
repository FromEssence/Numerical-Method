"""
求解f(x, y)=1/(x**2+y**2+2)的最大值点
方法：最陡爬山法
初始点: (1, 1, 0.25)
创新：每次搜索时的步长：
        初始步长foot，若新点的函数值小于原值，则foot减半
"""
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d 
from matplotlib import animation

plt.style.use('ggplot')

fig = plt.figure()
ax = Axes3D(fig)
#dots, = ax.plot([], [], [], 'ro')
#print ('\n'.join(['%s:%s' % item for item in mplot3d.art3d.Line3D.__dict__.items()]))

def init():
    X = np.arange(-2, 2, 0.15)
    Y = np.arange(-2, 2, 0.15)
    X, Y = np.meshgrid(X, Y) #网格化数据
    Z = 1/(X**2 + Y**2+2)
    
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, antialiased=False, alpha=1.0, cmap='winter')
def cal_f(xx, yy):
    return 1/(xx**2 + yy**2+2)

def gen_dots(err):
    newdot = [[],[],[]]
    newdot[0].append(1.0)
    newdot[1].append(1.0)
    newdot[2].append(0.25)
    #print (type(newdot[0]))
    step = 1 #初始步长: 1
    #def fun():
    while(True):
        yield newdot
        #计算梯度
        gradX = -2*newdot[0][-1]/np.square(newdot[0][-1]**2+newdot[1][-1]**2+2)
        gradY = -2*newdot[1][-1]/np.square(newdot[0][-1]**2+newdot[1][-1]**2+2)
        if(np.fabs(gradX)<err and np.fabs(gradY)<err):
            break
        newdot[0].append(newdot[0][-1]*(1+step*gradX))
        newdot[1].append(newdot[1][-1]*(1+step*gradY))
        oldV = newdot[2][-1]
        newdot[2].append(cal_f(newdot[0][-1], newdot[1][-1]))
        if(oldV > newdot[2][-1]):
            step = step*0.5
    ax.text(newdot[0][-1], newdot[1][-1], newdot[2][-1], "(%.3f, %.3f, %.3f)" %(newdot[0][-1],newdot[1][-1],newdot[2][-1]) , bbox=dict(facecolor='red', alpha=0.5))
    print("over")
    yield newdot

def update_dots(newd):
    return ax.plot(newd[0], newd[1], newd[2], 'ro')
            
ani = animation.FuncAnimation(fig, update_dots, frames = gen_dots(0.01), interval=1000, init_func = init)
#plt.show()

ani.save('E:/exp_3.gif', writer='imagemagick', fps=3)
