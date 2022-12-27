from pulp import *
from sympy import *
from sympy import symbols, solve, parse_expr, simplify,Symbol
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))

def maximizationАFun(c1,c2,a1,a2,a0,b1,b2,b0,d1,d2,d0,e1,e2,e0,f1,f2,f0):
    x1 = pulp.LpVariable("x1", lowBound=0)
    x2 = pulp.LpVariable("x2", lowBound=0)

    problem = pulp.LpProblem('0', LpMaximize)
    problem += c1 * x1 + c2 * x2, "Функция цели"
    problem += a1*x1 + a2*x2 >= a0, "1" #1 критерий
    problem += b1*x1 + b2 * x2 <= b0, "2" #2 критерий
    problem += d1 * x1 + d2 * x2 <= d0, "3"#3 критерий
    problem += e1*x1 + e2 * x2 <= e0, "4" #4 критерий
    problem += f1 * 1 + f2 * x2 <= f0, "5"  # 5 критерий

    problem.solve(PULP_CBC_CMD(msg=0))
    # for variable in problem.variables():
    #     print (variable.name, "=", variable.varValue)
    # print ("f(x)=:",value(problem.objective))
    return round(value(problem.objective),2)

def manimizationFun(c1,c2,a1,a2,a0,b1,b2,b0,d1,d2,d0,e1,e2,e0,f1,f2,f0):
    x1 = pulp.LpVariable("x1", lowBound=0)
    x2 = pulp.LpVariable("x2", lowBound=0)

    problem = pulp.LpProblem('0', LpMinimize)
    problem += c1 * x1 + c2 * x2, "Функция цели"
    problem += a1*x1 + a2*x2 >= a0, "1" #1 критерий
    problem += b1*x1 + b2 * x2 <= b0, "2" #2 критерий
    problem += d1 * x1 + d2 * x2 <= d0, "3"#3 критерий
    problem += e1*x1 + e2 * x2 <= e0, "4" #4 критерий
    problem += f1 * 1 + f2 * x2 <= f0, "5"  # 5 критерий

    problem.solve(PULP_CBC_CMD(msg=0))
    # for variable in problem.variables():
    #     print (variable.name, "=", variable.varValue)
    # print ("f(x)=:",value(problem.objective))
    koordinats=[];
    for variable in problem.variables():
        koordinats.append(round(variable.varValue,2))
    return koordinats

def perfectPoiint():
    f1=round(maximizationАFun(1,1,1,1,22,1,-2,11,-3,2,22,1,0,44,0,1,33),2)
    f2=round(maximizationАFun(-3,1,1,1,22,1,-2,11,-3,2,22,1,0,44,0,1,33),2)
    f3 = round(maximizationАFun(1,-3, 1, 1, 22, 1, -2, 11, -3, 2, 22, 1, 0, 44, 0, 1, 33),2)
    return [f1,f2,f3]

def distanceValue(x1,x2):
    f1,f2,f3=perfectPoiint();
    return ((x1+x2-f1)*(x1+x2-f1)+(-3*x1+x2-f2)*(-3*x1+x2-f2)+(x1-3*x2-f3))

def gradientValues(x1,x2):
    a1=round(22*x1-10*x2-142.26,2)
    a2=round(22*x2-10*x1-118.82,2)
    return [a1,a2]

def map_operations(formula_str):
    return formula_str.replace("^","**").replace("=","-")

if __name__ == '__main__':
    e=1
    F=perfectPoiint()
    n=11
    prev_x0=[2*n,n]
    prevDistance=distanceValue(2*n,n)
    i=1
    while(1>0):
        a1,a2=gradientValues(prev_x0[0],prev_x0[1])
        X1_=manimizationFun(a1,a2,1,1,22,1,-2,11,-3,2,22,1,0,44,0,1,33)
        X1=[]
        #print(X1_)
        lamda=symbols('lamda')
        p=(diff((prev_x0[0]+lamda*(X1_[0]-prev_x0[0])+prev_x0[1]+lamda*(X1_[1]-prev_x0[1])-F[0])*(prev_x0[0]+lamda*(X1_[0]-prev_x0[0])+(prev_x0[1]+lamda*(X1_[1]-prev_x0[1]))-F[0])+
                   +(-3*(prev_x0[0]+lamda*(X1_[0]-prev_x0[0]))+prev_x0[1]+lamda*(X1_[1]-prev_x0[1])-F[1])*(-3*(prev_x0[0]+lamda*(X1_[0]-prev_x0[0]))+(prev_x0[1]+lamda*(X1_[1]-prev_x0[1]))-F[1])+
                   +(prev_x0[0]+lamda*(X1_[0]-prev_x0[0])-3*(prev_x0[1]+lamda*(X1_[1]-prev_x0[1]))-F[2])*(prev_x0[0]+lamda*(X1_[0]-prev_x0[0])-3*(prev_x0[1]+lamda*(X1_[1]-prev_x0[1]))-F[2])))
        #print(p)

        lamda=Symbol('lamda')

        lamda=(solve(p,lamda))
        lamda=lamda[0]

        #print(lamda)
        X1 = [prev_x0[0] + lamda * (X1_[0] - prev_x0[0]), prev_x0[1] + lamda * (X1_[1] - prev_x0[1])]
        currentP=distanceValue(X1[0],X1[1])
        if(abs(prevDistance-currentP)<e):
            print("Координаты точки:")
            print(X1[0],X1[1])
            # print("Значение расстояния:")
            # print(currentP)
            print("Значение лямбды:")
            print(lamda)
            print("Номер иттерации")
            print(i)
            break
        else:
            i+=1
            # plt.plot(X1[0], X1[1], 'bo', markersize=2.)
            prev_x0=[X1[0],X1[1]]
            prevDistance=currentP
    #print(distanceValue(X1[0],X1[1]))


# Отрисовка
def cal_intersection(k1, b1, k2, b2):
    x = (b2 - b1) / (k1 - k2)
    y = k1 * (b2 - b1) / (k1 - k2) + b1
    return (x, y)



plt.axis([-5, 60, -5, 60])

# оси
x = np.arange(0.0, 60)
y = 0 * x
plt.plot(x, y, 'k')
plt.plot(60, 0.0, 'k', marker='>')

y = np.arange(0.0, 60)
x = 0 * y
plt.plot(x, y, 'k')
plt.plot(0.0, 60, 'k', marker='^')

# d = np.linspace(-0,120,1000)
# x,y = np.meshgrid(d,d)
# plt.imshow( ((y<=3*n) & (y>=0) & (x<=4*n) & (x>=0) & (y>=2*n-x) & (2*y>=x-n) & (2*y<=2*n+3*x) & (y>=gamma1-x) & (3*y<=-gamma3+x)).astype(int) ,
#                 extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);



# точки
# y = 33 и -3*x1 + 2*x2  <= 22
x_cross_A, y_cross_A = cal_intersection(0, 33, 3 / 2, 11)
x_cross_A = round(x_cross_A, 2)
y_cross_A = round(y_cross_A, 2)
plt.plot(x_cross_A, y_cross_A, 'bo', markersize=2.)
plt.text(x_cross_A + 0.1, y_cross_A, "A")
#
# y = 33 и x = 44
x_cross_B = 44
y_cross_B = 33
plt.plot(x_cross_B, y_cross_B, 'bo', markersize=2.)
plt.text(x_cross_B + 0.1, y_cross_B, "B")
#
# x = 44 и x1 - 2*x2  <= 11
x_cross_C = 44
y_cross_C = 16.5
plt.plot(x_cross_C, y_cross_C, 'bo', markersize=2.)
plt.text(x_cross_C + 0.1, y_cross_C, "C")

# x1 + x2  >= 22 и  x1 - 2*x2  <= 11
x_cross_D, y_cross_D = cal_intersection(-1, 22, 0.5, -5.5)
x_cross_D = round(x_cross_D, 2)
y_cross_D = round(y_cross_D, 2)
plt.plot(x_cross_D, y_cross_D, 'bo', markersize=2.)
plt.text(x_cross_D + 0.1, y_cross_D, "D")

# # x1 + x2  >= 22 и  -3*x1 + 2*x2  <= 22
x_cross_E, y_cross_E = cal_intersection(-1, 22, 3 / 2, 11)
x_cross_E = round(x_cross_E, 2)
y_cross_E = round(y_cross_E, 2)
plt.plot(x_cross_E, y_cross_E, 'bo', markersize=2.)
plt.text(x_cross_E + 0.1, y_cross_E, "E")

# прямые по точкам
# A-B
x = [x_cross_A, x_cross_B]
y = [y_cross_A, y_cross_B]
plt.plot(x, y, 'k', label="y = 33")
# B-C
x = [x_cross_B, x_cross_C]
y = [y_cross_B, y_cross_C]
plt.plot(x, y, 'blue', label="x = 44")
# C-D
x = [x_cross_C, x_cross_D]
y = [y_cross_C, y_cross_D]
plt.plot(x, y, 'cyan', label="x - 2y = 11")
# D-E
x = [x_cross_D, x_cross_E]
y = [y_cross_D, y_cross_E]
plt.plot(x, y, 'magenta', label="x + y = 22")
# E-A
x = [x_cross_E, x_cross_A]
y = [y_cross_E, y_cross_A]
plt.plot(x, y, 'yellow', label=" -3x + 2y = 22")

# идеальная точка
plt.plot(X1[0], X1[1], 'ro', markersize=2.)


# legend
plt.legend(loc="upper right")
plt.xlabel(r'$x1$')
plt.ylabel(r'$x2$')

plt.grid()
plt.show()






