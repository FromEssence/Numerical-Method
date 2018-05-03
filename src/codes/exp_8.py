'''
@brief: 自适应法计算积分
@author: Tang
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math

#print(plt.style.available)
plt.style.use("ggplot")
fig,ax = plt.subplots()
err = 0.00001

'''
@brief: get f(x) = sin(x)/x
'''
def func(x): 
    if(x==0):
        return 1.0
    else:
        return math.sin(x)/x

'''
@brief: Runge自适应求积分
@err: 求解误差
'''
def calculus(err):
    '''初始区间数，求解积分区间'''
    n = 1
    a, b = 0, 6
    h = float(b-a)
    e = err/h
    T0 = 0.5*h*(func(float(a))+func(float(b)))#积分值
    stack = [[a,b,1,T0]] #待二分的区间
    now = [[a,b,1,T0]] #目前的区间状况
    cal = T0 #最终积分值
    yield now
    cnt = 0
    while(len(stack) != 0):
        cnt = cnt+1
        #取出栈顶
        top = stack[-1]
        cal -= top[3]
        #pop
        stack.pop()
        now.remove(top)
        T0 = top[3]
        h = float(top[1]-top[0])
        T1 = 0.5*T0 + 0.5*h*func(top[0]+h*0.5)
        cal += T1
        if math.fabs(T1-T0)<e*h:
            '''
            可以用左右区间的梯形和近似整个区间
            '''
            now.append([top[0],top[1],2,T1])
                       
        else:
            '''
            继续划分
            '''
            #now.append([top[0],top[1],2,T1])
            tmp = 0.5*(0.5*h)*(func(top[0])+func((top[0]+top[1])/2))
            stack.append([top[0],(top[0]+top[1])/2,1,tmp])
            now.append([top[0],(top[0]+top[1])/2,1,tmp])
            tmp = 0.5*(0.5*h)*(func(top[1])+func((top[0]+top[1])/2))        
            stack.append([(top[0]+top[1])/2,top[1],1,tmp])
            now.append([(top[0]+top[1])/2,top[1],1,tmp])
        '''
        为了加快画图速度，每计算50次画一张
        '''
        if(cnt>50): 
            yield now
            cnt = 0
    print(cal)
    yield now


def update(data):
    calculus = 0;
    plt.cla()
    plt.grid(False)
    tmpx = [0 + float(6) /100 * each for each in range(101)]
    ax.spines['bottom'].set_position(('data', 0))  #调整坐标轴位置
    ax.spines['left'].set_position(('data',0)) 
    plt.plot(tmpx, [func(each) for each in tmpx], linestyle = '-', color='black') #待积分曲线
    
    for d in data:
        n = d[2] #子区间数
        calculus += d[3]
        for rang in range(n):
            tmpx = [d[0] + float(d[1]-d[0])/n * rang, d[0] + float(d[1]-d[0])/n * rang, d[0] + float(d[1]-d[0])/n * (rang+1), d[0] + float(d[1]-d[0])/n * (rang+1)]
            tmpy = [0, func(tmpx[1]), func(tmpx[2]), 0]
            c = ['skyblue', 'lightpink', 'orange', 'firebrick']
            
            plt.fill(tmpx, tmpy, color=c[rang%4])
    
    ax.text(5, 1, "Calculus:(%.5f)" % (calculus) , bbox=dict(facecolor='red', alpha=0.5))
    return 0


ani = animation.FuncAnimation(fig, update, frames = calculus(err), interval=1, repeat=False)
plt.show()


ani.save('E:/exp_8.gif', writer='imagemagick', fps=3)





    
