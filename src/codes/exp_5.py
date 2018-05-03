'''
Newton差商插值法
实验发现：当插值点过多时，插值多项式次数过高，在[0, 1]附近急剧偏离
'''
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

fig, ax = plt.subplots()

def init():
    ax.set_ylim(-1.2, 1.2)
    #ax.set_xlim(0, 4*np.pi)
    x = np.linspace(0, 2*np.pi)
    y = np.sin(x)
    l = ax.plot(x, y, color='black')
    
def gen_inser_Points():
    xt = np.arange(1, 2*np.pi, 0.1)
    yt = np.sin(xt)
    return (xt, yt, np.size(xt))

def cal_coe(n, xt, yt):
    a = []
    '''
    print(n)
    print(np.size(a))
    print(np.size(yt))'''
    
    for i in range(0, n):
        #print(i)
        a.append(yt[i])
    for k in range(1, n):
        for j in range(n-1, k-1, -1):
            a[j] = (a[j]-a[j-1]) / (xt[j]-xt[j-k])
    return a

def Newton(val, xt, a, n):
    res = a[n-1]
    
    for i in range(n-2, -1, -1):
        res = res*(val-xt[i])+a[i]
    return res

def draw(xt, yt, L, R, a, n):    
    xp = np.linspace(L, R, 100)
    yp = []
    for val in xp:
        yp.append(Newton(val, xt, a, n))
    ax.plot(xp, yp, linestyle = '--', color='r')
    for i in range(0, np.size(xt)):
        ax.plot(xt[i], yt[i], 'yo')

xt, yt, n = gen_inser_Points()
a = cal_coe(n, xt, yt)
init()
draw(xt, yt, 0, 2*np.pi, a, n)
plt.show()
