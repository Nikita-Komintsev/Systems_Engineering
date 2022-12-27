from pulp import *
import numpy as np
import matplotlib.pyplot as plt

def cal_intersection(k1, b1, k2, b2):
    x = (b2 - b1) / (k1 - k2)
    y = k1 * (b2 - b1) / (k1 - k2) + b1
    return (x, y)

plt.figure(figsize=(6, 6))
plt.axis([-5, 30, -5, 30])

# оси
x = np.arange(0.0, 30)
y = 0 * x
plt.plot(x, y, 'k')
plt.plot(30-1, 0.0, 'k', marker='>')

y = np.arange(0.0, 30)
x = 0 * y
plt.plot(x, y, 'k')
plt.plot(0.0, 30-1, 'k', marker='^')


# шаг 1. Строим Д
d = np.linspace(-0, 60, 1000)
x,y = np.meshgrid(d,d)
plt.imshow( ((y<=16.5) & (y>=0) & (x<=22) & (x>=0) & (2*y<=44-x) & (y>=11-2*x)).astype(int) ,
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);

plt.scatter(0, 16.5, color='red')
plt.annotate("A(0,16.5)", (0+1, 16.5+1))

plt.scatter(11, 16.5, color='blue')
plt.annotate("B", (11+1, 16.5+1))

plt.scatter(22, 11, color='blue')
plt.annotate("C", (22+1, 11+1))

plt.scatter(22, 0, color='blue')
plt.annotate("D", (22+1, 0+1))

plt.scatter(5.5, 0, color='blue')
plt.annotate("E", (5.5+1, 0+1))

plt.scatter(0, 11, color='blue')
plt.annotate("F", (0+1, 11+1))

x = np.linspace(-5, 100, 1000)
# y <= 16.5
y1 = (x*0) + 0
# 2y<=44-x
y2 = (44-x)/2
# y >= 23 - 2*x
y3 = (11 - 2*x)
# x <= 22
yy = np.linspace(-5, 30, 1000)
xx = (yy*0) + 0


plt.plot(x, 16.5*np.ones_like(y1), label=r'$y\leq 16.5$')
plt.plot(x, y2, label=r'$2y\leq44-x$')
plt.plot(x, y3, label=r'$y\geq 11 - 2*x$')
plt.plot(22*np.ones_like(xx), yy, label=r'$x\leq 22$')
plt.xlim(-5, 35)
plt.ylim(-5, 35)
plt.legend(loc="upper right")
plt.xlabel(r'$x1$')
plt.ylabel(r'$x2$')
plt.title("Оптимизация второго критерия")
plt.grid()

## Вектор
# plt.arrow(0, 0, -3, 1, width = 0.3)
#
# x_perp = [0, 1]
# y_perp = [0, 3]
# slope, intercept = np.polyfit(x_perp, y_perp, 1)
# x = np.linspace(0, 20)
# plt.plot(x, slope * x + intercept, 'yellow')

#решение задачи оптимизации 2-го критерия симплекс-методом
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

problem = pulp.LpProblem('0',LpMaximize)
problem += (-3)*x1 + 1*x2, "Функция цели"
problem += x1 + 2*x2 <= 44,"1"
problem += 2*x1 + x2 >= 11, "2"
problem += x1 + 0*x2 <= 22, "3"
problem += 0*x1+x2 <= 16.5, "4"

problem.solve(PULP_CBC_CMD(msg=0))
print ("Оптимизация 2-го критерия\n Точка A с координатами:")
for variable in problem.variables():
     print(" ", variable.name, "=", variable.varValue)
print("  f*2(x)=:", value(problem.objective))


# шаг 2. Строим Д2
plt.figure(figsize=(6, 6))
plt.axis([-5, 30, -5, 30])

# оси
x = np.arange(0.0, 30)
y = 0 * x
plt.plot(x, y, 'k')
plt.plot(30-1, 0.0, 'k', marker='>')

y = np.arange(0.0, 30)
x = 0 * y
plt.plot(x, y, 'k')
plt.plot(0.0, 30-1, 'k', marker='^')

#построение Д2
d = np.linspace(0,80,1000)
x,y = np.meshgrid(d,d)
plt.imshow(((y<=16.5) & (y>=0) & (x<=22) & (x>=0) & (2*y<=44-x) & (y>=11-2*x) & (y>=3*x+16.5-2)).astype(int),
                extent=(x.min(),x.max(),y.min(),y.max()), origin="lower", cmap="Greys", alpha=0.3)


plt.scatter(0, 16.5, color='blue', s=10)
plt.annotate("A", (0+0.1, 16.5+0.1))

# точки пересечения y = 16.6 и -3x+y=16.5 - 2
x_cross, y_cross = cal_intersection(0, 16.6, 3, 14.5)
x_cross = round(x_cross, 5)
y_cross = round(y_cross, 5)

plt.scatter(0.667, 16.5, color='red', s=10)
plt.annotate("G(0.667,16.5)", (x_cross+0.1, y_cross+0.1))

plt.scatter(0, 14.5, color='blue', s=10)
plt.annotate("H", (0+0.1, 14.5+0.1))

x = np.linspace(-5, 100, 1000)
# y <= 16.5
y1 = (x*0) + 0
# 2y<=44-x
y2 = (44-x)/2
# y >= 11 - 2*x
y3 = (11 - 2*x)
# y>=3x+2
y4 = (3*x+14.5)
# x <= 22
yy = np.linspace(-5, 30, 1000)
xx = (yy*0) + 0


plt.plot(x, 16.5*np.ones_like(y1), label=r'$y\leq 16.5$')
plt.plot(x, y2, label=r'$2y\leq44-x$')
plt.plot(x, y3, label=r'$y\geq 11 - 2*x$')
plt.plot(22*np.ones_like(xx), yy, label=r'$x\leq 22$')
plt.plot(x, y4, label=r'$y\geq3*x+14.5$')
plt.xlim(-5, 35)
plt.ylim(-5, 35)
plt.legend(loc="upper right")
plt.xlabel(r'$x1$')
plt.ylabel(r'$x2$')
plt.title("Оптимизация первого критерия")

##Вектор
# plt.arrow(0, 0, 1, 1, width = 0.3)
#
# x_perp = [0, 1]
# y_perp = [0, 1]
# slope, intercept = np.polyfit(x_perp, y_perp, 1)
# x = np.linspace(-20, 0)
# plt.plot(x, -slope * x + intercept, 'yellow')

#решение задачи оптимизации 1-го критерия симплекс-методом
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

problem = pulp.LpProblem('0',LpMaximize)
problem += x1 + x2, "Функция цели"
problem += x1 + 2*x2 <= 44,"1"
problem += 2*x1 + x2 >= 11, "2"
problem += x1 + 0*x2 <= 22, "3"
problem += 0*x1+x2 <= 16.5, "4"
problem += (-3)*x1+x2 >= 14.5, "5"


problem.solve(PULP_CBC_CMD(msg=0))
print("\nОптимизация 1-го критерия\n Точка G с координатами:")
for variable in problem.variables():
     print (" ",variable.name, "=", variable.varValue)
print("  f*1(x)=:",value(problem.objective))

plt.grid()

# шаг 3. Строим Д3
plt.figure(figsize=(6, 6))
plt.axis([-5, 30, -5, 30])

# оси
x = np.arange(0.0, 30)
y = 0 * x
plt.plot(x, y, 'k')
plt.plot(30-1, 0.0, 'k', marker='>')

y = np.arange(0.0, 30)
x = 0 * y
plt.plot(x, y, 'k')
plt.plot(0.0, 30-1, 'k', marker='^')

#построение Д3
d = np.linspace(0,80,1000)
x,y = np.meshgrid(d,d)
plt.imshow(((y<=16.5) & (y>=0) & (x<=22) & (x>=0) & (2*y<=44-x) & (y>=11-2*x) & (y>=3*x+14.5) & (y>=14.17-x)).astype(int),
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha=0.3)


plt.scatter(0, 16.5, color='blue', s=10)
plt.annotate("A", (0+0.1, 16.5+0.1))

# точки пересечения y = 16.6 и -3x+y=16.5 - 2
x_cross, y_cross = cal_intersection(0, 16.6, 3, 14.5)
x_cross = round(x_cross, 5)
y_cross = round(y_cross, 5)

plt.scatter(0.667, 16.5, color='blue', s=10)
plt.annotate("G", (x_cross+0.1, y_cross+0.1))

plt.scatter(0, 14.5, color='red', s=10)
plt.annotate("H(0,14.5)", (0+0.1, 14.5+0.1))

x = np.linspace(-5, 100, 1000)
# y <= 16.5
y1 = (x*0) + 0
# 2y<=44-x
y2 = (44-x)/2
# y >= 11 - 2*x
y3 = (11 - 2*x)
# y>=3x+2
y4 = (3*x+14.5)
# y=14.17-x
y5 = (14.17 - x)
# x <= 22
yy = np.linspace(-5, 30, 1000)
xx = (yy*0) + 0


plt.plot(x, 16.5*np.ones_like(y1), label=r'$y\leq 16.5$')
plt.plot(x, y2, label=r'$2y\leq44-x$')
plt.plot(x, y3, label=r'$y\geq 11 - 2*x$')
plt.plot(22*np.ones_like(xx), yy, label=r'$x\leq 22$')
plt.plot(x, y4, label=r'$y\geq3*x+14.5$')
plt.plot(x, y5, label=r'$y\geq14.17-x$')
plt.xlim(-5, 35)
plt.ylim(-5, 35)
plt.legend(loc="upper right")
plt.xlabel(r'$x1$')
plt.ylabel(r'$x2$')
plt.title("Оптимизация третьего критерия")

# ## Вектор3
plt.arrow(0, 0, 1, -3, width = 0.3)
x1 = 0
y1 = 0
x2 = 1
y2 = -3
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
perp = lambda x: -(1 / k) * (x - x1) + y1
x = np.linspace(0, 20)
plt.plot(x, perp(x))

#решение задачи оптимизации 3-го критерия симплекс-методом
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

problem = pulp.LpProblem('0',LpMaximize)
problem += x1 + (-3)*x2, "Функция цели"
problem += x1 + 2*x2 <= 44,"1"
problem += 2*x1 + x2 >= 11, "2"
problem += x1 + 0*x2 <= 22, "3"
problem += 0*x1+x2 <= 16.5, "4"
problem += (-3)*x1+x2 >= 14.5, "5"
problem += x1+x2 >= 14.17, "6"


problem.solve(PULP_CBC_CMD(msg=0))
print("\nОптимизация 3-го критерия\n Точка H с координатами:")
for variable in problem.variables():
     print (" ",variable.name, "=", variable.varValue)
print("  f*3(x)=:",value(problem.objective))


plt.grid()
plt.show()
