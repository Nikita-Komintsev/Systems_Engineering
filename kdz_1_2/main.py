from tkinter import *
from copy import deepcopy
from tkinter import messagebox as mb
from tkinter.ttk import Notebook
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import sys

my_Font = ('URW Gothic L','12','bold')

def main_matrix(tab_1, values, values_f2):
    matrix_Q = [["x1", "(1, 8)", "(4, 5)", "(2, 4)", "(8, 12)"],
                ["x2", "(8, 2)", "(5, 6)", "(3, 3)", "(10, 9)"],
                ["x3", "(3, 1)", "(4, 2)", "(5, 3)", "(13, 4)"],
                ["x4", "(5, 5)", "(2, 3)", "(8, 4)", "(4, 6)"],
                ["x5", "(2, 6)", "(5, 7)", "(3, 8)", "(9, 10)"],
                ["x6", "(9, 4)", "(6, 5)", "(4, 6)", "(11,13)"],
                ["x7", "(4, 10)", "(5, 6)", "(6, 5)", "(14,11)"],
                ["x8", "(6. 8)", "(7, 9)", "(8, 7)", "(9, 9)"]]

    Label(tab_1, text="Матрица Q : ", height=5, font=my_Font).pack()
    columns = (" ", "z1", "z2", "z3", "z4")
    tree = ttk.Treeview(tab_1, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    for value in matrix_Q:
        tree.insert("", END, values=value)

    Label(tab_1, text="Матрица f1 : ", height=5, font=my_Font).pack()
    columns = (" ", "z1", "z2", "z3", "z4")
    tree = ttk.Treeview(tab_1, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    for value in values:
        tree.insert("", END, values=value)

    Label(tab_1, text="Матрица f2 : ", height=5, font=my_Font).pack()
    columns = (" ", "z1", "z2", "z3", "z4")
    tree = ttk.Treeview(tab_1, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    for value in values_f2:
        tree.insert("", END, values=value)


def gurvitz(tab_4, values, values_int, values_f2, values_int_f2):
    Label(tab_4, text="α = 0.6", height=4, font=my_Font).pack()

    # FOR f1
    Label(tab_4, text="для f1: ", font=my_Font).pack()
    copy_values = deepcopy(values)
    min_el = []
    i = 0
    for line in values_int:
        min_el.append(min(line))
        copy_values[i].append(min(line))
        i += 1

    max_el = []
    i = 0
    for line in values_int:
        max_el.append(max(line))
        copy_values[i].append(max(line))
        i += 1

    t = 0
    i = 0
    Ci = []
    for el in range(0, len(min_el)):
        t = round(0.6 * min_el[el] + (1 - 0.6) * max_el[el], 2)
        Ci.append(t)
        copy_values[i].append(t)
        i += 1

    maxim = max(Ci)

    columns = (" ", "z1", "z2", "z3", "z4", "min", "max", "C")
    tree = ttk.Treeview(tab_4, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.column("#7", stretch=NO, width=80, anchor='c')
    tree.column("#8", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("min", text="min")
    tree.heading("max", text="max")
    tree.heading("C", text="C")
    tree.tag_configure('my_tag', background='lightgreen')

    x_opt = []
    for value in copy_values:
        if value[-1] == maxim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt.append(value[0])
        else:
            tree.insert("", END, values=value)

    # FOR f2
    Label(tab_4, text="для f2: ", font=my_Font).pack()
    copy_values = deepcopy(values_f2)
    min_el = []
    i = 0
    for line in values_int_f2:
        min_el.append(min(line))
        copy_values[i].append(min(line))
        i += 1

    max_el = []
    i = 0
    for line in values_int_f2:
        max_el.append(max(line))
        copy_values[i].append(max(line))
        i += 1

    t = 0
    i = 0
    Ci = []
    for el in range(0, len(min_el)):
        t = round(0.6 * min_el[el] + (1 - 0.6) * max_el[el], 2)
        Ci.append(t)
        copy_values[i].append(t)
        i += 1

    maxim = max(Ci)

    columns = (" ", "z1", "z2", "z3", "z4", "min", "max", "C")
    tree = ttk.Treeview(tab_4, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.column("#7", stretch=NO, width=80, anchor='c')
    tree.column("#8", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("min", text="min")
    tree.heading("max", text="max")
    tree.heading("C", text="C")
    tree.tag_configure('my_tag', background='lightgreen')

    x_opt_f2 = []
    for value in copy_values:
        if value[-1] == maxim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt_f2.append(value[0])
        else:
            tree.insert("", END, values=value)

    Label(tab_4, text="Оптимальное решение по критерию Гурвица для f1: " + str(x_opt) + " для f2: " + str(x_opt_f2),
          height=5, font=my_Font).pack()
    return x_opt, x_opt_f2


def wald(tab_2, values, values_int, values_f2, values_int_f2):
    # FOR f1
    Label(tab_2, text="для f1: ", font=my_Font).pack()
    copy_values = deepcopy(values)
    min_el = []
    i = 0
    for line in values_int:
        min_el.append(min(line))
        copy_values[i].append(min(line))
        i += 1
    maxim = max(min_el)

    columns = (" ", "z1", "z2", "z3", "z4", "min")
    tree = ttk.Treeview(tab_2, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("min", text="min")
    tree.tag_configure('my_tag', background='lightgreen')
    x_opt = []
    for value in copy_values:
        if value[-1] == maxim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt.append(value[0])
        else:
            tree.insert("", END, values=value)

    # FOR f2
    Label(tab_2, text="для f2: ", font=my_Font).pack()
    copy_values = deepcopy(values_f2)
    min_el = []
    i = 0
    for line in values_int_f2:
        min_el.append(min(line))
        copy_values[i].append(min(line))
        i += 1
    maxim = max(min_el)

    columns = (" ", "z1", "z2", "z3", "z4", "min")
    tree = ttk.Treeview(tab_2, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("min", text="min")
    tree.tag_configure('my_tag', background='lightgreen')
    x_opt_f2 = []
    for value in copy_values:
        if value[-1] == maxim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt_f2.append(value[0])
        else:
            tree.insert("", END, values=value)
    Label(tab_2, text="Оптимальное решение по критерию Вальда для f1: " + str(x_opt) + " для f2: " + str(x_opt_f2),
          height=5, font=my_Font).pack()

    return x_opt, x_opt_f2


def savage(tab_3, values, values_int, values_f2, values_int_f2):
    Label(tab_3, text="Матрица рисков Q → R : ", height=5, font=my_Font).pack()

    ##### FOR f1
    Label(tab_3, text="для f1: ", font=my_Font).pack()
    matrix_r_x = [['x1', 8, 3, 6, 6], ['x2', 1, 2, 5, 4], ['x3', 6, 3, 3, 1], ['x4', 4, 5, 0, 10],
                  ['x5', 7, 2, 5, 5], ['x6', 0, 1, 4, 3], ['x7', 5, 2, 2, 0], ['x8', 3, 0, 0, 5]]
    matrix_r = [[8, 3, 6, 6], [1, 2, 5, 4], [6, 3, 3, 1], [4, 5, 0, 10],
                [7, 2, 5, 5], [0, 1, 4, 3], [5, 2, 2, 0], [3, 0, 0, 5]]
    max_el = []
    i = 0
    for line in matrix_r:
        max_el.append(max(line))
        matrix_r_x[i].append(max(line))
        i += 1

    minim = min(max_el)

    columns = (" ", "z1", "z2", "z3", "z4", "max")
    tree = ttk.Treeview(tab_3, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("max", text="max")
    tree.tag_configure('my_tag', background='lightgreen')
    x_opt = []
    for value in matrix_r_x:
        if value[-1] == minim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt.append(value[0])
        else:
            tree.insert("", END, values=value)

    ##### FOR f2
    Label(tab_3, text="для f2: ", font=my_Font).pack()
    matrix_r_x = [['x1', 2, 4, 4, 1], ['x2', 8, 3, 5, 4], ['x3', 9, 7, 5, 9], ['x4', 5, 6, 4, 7],
                  ['x5', 4, 2, 0, 3], ['x6', 6, 4, 2, 0], ['x7', 0, 3, 3, 2], ['x8', 2, 0, 1, 4]]
    matrix_r = [[2, 4, 4, 1], [8, 3, 5, 4], [9, 7, 5, 9], [5, 6, 4, 7],
                [4, 2, 0, 3], [6, 4, 2, 0], [0, 3, 3, 2], [2, 0, 1, 4]]
    max_el = []
    i = 0
    for line in matrix_r:
        max_el.append(max(line))
        matrix_r_x[i].append(max(line))
        i += 1

    minim = min(max_el)

    columns = (" ", "z1", "z2", "z3", "z4", "max")
    tree = ttk.Treeview(tab_3, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("max", text="max")
    tree.tag_configure('my_tag', background='lightgreen')
    x_opt_f2 = []
    for value in matrix_r_x:
        if value[-1] == minim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt_f2.append(value[0])
        else:
            tree.insert("", END, values=value)

    Label(tab_3, text="Оптимальное решение по критерию Сэвиджа для f1: " + str(x_opt) + " для f2: " + str(x_opt_f2),
          height=5, font=my_Font).pack()
    return x_opt, x_opt_f2


def laplas(tab_5, values, values_int, values_f2, values_int_f2):
    # FOR f1
    Label(tab_5, text="для f1: ", font=my_Font).pack()
    copy_values = deepcopy(values)

    sred_el = []
    i = 0
    for line in values_int:
        t = round((line[0] + line[1] + line[2] + line[3]) / 4, 2)
        sred_el.append(t)
        copy_values[i].append(t)
        i += 1
    maxim = max(sred_el)

    columns = (" ", "z1", "z2", "z3", "z4", "sred")
    tree = ttk.Treeview(tab_5, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("sred", text="Среднее")
    tree.tag_configure('my_tag', background='lightgreen')
    x_opt = []
    for value in copy_values:
        if value[-1] == maxim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt.append(value[0])
        else:
            tree.insert("", END, values=value)

    # FOR f2
    Label(tab_5, text="для f2: ", font=my_Font).pack()
    copy_values = deepcopy(values_f2)

    sred_el = []
    i = 0
    for line in values_int_f2:
        t = round((line[0] + line[1] + line[2] + line[3]) / 4, 2)
        sred_el.append(t)
        copy_values[i].append(t)
        i += 1
    maxim = max(sred_el)

    columns = (" ", "z1", "z2", "z3", "z4", "sred")
    tree = ttk.Treeview(tab_5, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("sred", text="Среднее")
    tree.tag_configure('my_tag', background='lightgreen')
    x_opt_f2 = []
    for value in copy_values:
        if value[-1] == maxim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt_f2.append(value[0])
        else:
            tree.insert("", END, values=value)

    Label(tab_5, text="Оптимальное решение по критерию Лапласа для f1: " + str(x_opt) + " для f2: " + str(x_opt_f2),
          height=5, font=my_Font).pack()
    return x_opt, x_opt_f2


def golosovanie(tab_6, opt_wald, opt_savage, opt_gurvitz, opt_laplas, opt_wald_f2, opt_savage_f2, opt_gurvitz_f2,
                opt_laplas_f2):
    Label(tab_6, text="для f1: ", font=my_Font).pack()

    columns = (" ", "Вальд", "Сэвидж", "Гурвиц", "Лаплас", "sum")
    tree = ttk.Treeview(tab_6, columns=columns, show="headings")

    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text="\\\\\\\\\\")
    tree.heading("Вальд", text="Вальд\n")
    tree.heading("Сэвидж", text="Сэвидж\n")
    tree.heading("Гурвиц", text="Гурвиц\n")
    tree.heading("Лаплас", text="Лаплас\n")
    tree.heading("sum", text="Σ")
    values = [["x1", "", "", "", ""], ["x2", "", "", "", ""], ["x3", "", "", "", ""],
              ["x4", "", "", "", ""], ["x5", "", "", "", ""], ["x6", "", "", "", ""],
              ["x7", "", "", "", ""], ["x8", "", "", "", ""]]

    for val in values:
        if 'x1' in opt_wald and val[0] == 'x1':
            val[1] = '+'
        if 'x2' in opt_wald and val[0] == 'x2':
            val[1] = '+'
        if 'x3' in opt_wald and val[0] == 'x3':
            val[1] = '+'
        if 'x4' in opt_wald and val[0] == 'x4':
            val[1] = '+'
        if 'x5' in opt_wald and val[0] == 'x5':
            val[1] = '+'
        if 'x6' in opt_wald and val[0] == 'x6':
            val[1] = '+'
        if 'x7' in opt_wald and val[0] == 'x7':
            val[1] = '+'
        if 'x8' in opt_wald and val[0] == 'x8':
            val[1] = '+'
        if 'x1' in opt_savage and val[0] == 'x1':
            val[2] = '+'
        if 'x2' in opt_savage and val[0] == 'x2':
            val[2] = '+'
        if 'x3' in opt_savage and val[0] == 'x3':
            val[2] = '+'
        if 'x4' in opt_savage and val[0] == 'x4':
            val[2] = '+'
        if 'x5' in opt_savage and val[0] == 'x5':
            val[2] = '+'
        if 'x6' in opt_savage and val[0] == 'x6':
            val[2] = '+'
        if 'x7' in opt_savage and val[0] == 'x7':
            val[2] = '+'
        if 'x8' in opt_savage and val[0] == 'x8':
            val[2] = '+'
        if 'x1' in opt_gurvitz and val[0] == 'x1':
            val[3] = '+'
        if 'x2' in opt_gurvitz and val[0] == 'x2':
            val[3] = '+'
        if 'x3' in opt_gurvitz and val[0] == 'x3':
            val[3] = '+'
        if 'x4' in opt_gurvitz and val[0] == 'x4':
            val[3] = '+'
        if 'x5' in opt_gurvitz and val[0] == 'x5':
            val[3] = '+'
        if 'x6' in opt_gurvitz and val[0] == 'x6':
            val[3] = '+'
        if 'x7' in opt_gurvitz and val[0] == 'x7':
            val[3] = '+'
        if 'x8' in opt_gurvitz and val[0] == 'x8':
            val[3] = '+'
        if 'x1' in opt_laplas and val[0] == 'x1':
            val[4] = '+'
        if 'x2' in opt_laplas and val[0] == 'x2':
            val[4] = '+'
        if 'x3' in opt_laplas and val[0] == 'x3':
            val[4] = '+'
        if 'x4' in opt_laplas and val[0] == 'x4':
            val[4] = '+'
        if 'x5' in opt_laplas and val[0] == 'x5':
            val[4] = '+'
        if 'x6' in opt_laplas and val[0] == 'x6':
            val[4] = '+'
        if 'x7' in opt_laplas and val[0] == 'x7':
            val[4] = '+'
        if 'x8' in opt_laplas and val[0] == 'x8':
            val[4] = '+'

    i = 0
    max_sum = []
    for line in values:
        summ = 0
        for el in line:
            if el == "+":
                summ += 1
        max_sum.append(summ)
        values[i].append(str(summ))
        i += 1

    maxim = max(max_sum)

    tree.tag_configure('my_tag', background="lightgreen")

    x_opt = []
    for value in values:
        if value[-1] == str(maxim):
            tree.insert("", END, values=value, tags='my_tag')
            x_opt.append(value[0])
        else:
            tree.insert("", END, values=value)

    Label(tab_6, text="Оптимальное решение для f1: " + str(x_opt), height=5, font=my_Font).pack(fill=BOTH)

    ######### FOR f2
    Label(tab_6, text="для f2: ", font=my_Font).pack()
    columns = (" ", "Вальд", "Сэвидж", "Гурвиц", "Лаплас", "sum")
    tree = ttk.Treeview(tab_6, columns=columns, show="headings")

    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text="\\\\\\\\\\")
    tree.heading("Вальд", text="Вальд\n")
    tree.heading("Сэвидж", text="Сэвидж\n")
    tree.heading("Гурвиц", text="Гурвиц\n")
    tree.heading("Лаплас", text="Лаплас\n")
    tree.heading("sum", text="Σ")
    values = [["x1", "", "", "", ""], ["x2", "", "", "", ""], ["x3", "", "", "", ""],
              ["x4", "", "", "", ""], ["x5", "", "", "", ""], ["x6", "", "", "", ""],
              ["x7", "", "", "", ""], ["x8", "", "", "", ""]]

    for val in values:
        if 'x1' in opt_wald_f2 and val[0] == 'x1':
            val[1] = '+'
        if 'x2' in opt_wald_f2 and val[0] == 'x2':
            val[1] = '+'
        if 'x3' in opt_wald_f2 and val[0] == 'x3':
            val[1] = '+'
        if 'x4' in opt_wald_f2 and val[0] == 'x4':
            val[1] = '+'
        if 'x5' in opt_wald_f2 and val[0] == 'x5':
            val[1] = '+'
        if 'x6' in opt_wald_f2 and val[0] == 'x6':
            val[1] = '+'
        if 'x7' in opt_wald_f2 and val[0] == 'x7':
            val[1] = '+'
        if 'x8' in opt_wald_f2 and val[0] == 'x8':
            val[1] = '+'
        if 'x1' in opt_savage_f2 and val[0] == 'x1':
            val[2] = '+'
        if 'x2' in opt_savage_f2 and val[0] == 'x2':
            val[2] = '+'
        if 'x3' in opt_savage_f2 and val[0] == 'x3':
            val[2] = '+'
        if 'x4' in opt_savage_f2 and val[0] == 'x4':
            val[2] = '+'
        if 'x5' in opt_savage_f2 and val[0] == 'x5':
            val[2] = '+'
        if 'x6' in opt_savage_f2 and val[0] == 'x6':
            val[2] = '+'
        if 'x7' in opt_savage_f2 and val[0] == 'x7':
            val[2] = '+'
        if 'x8' in opt_savage_f2 and val[0] == 'x8':
            val[2] = '+'
        if 'x1' in opt_gurvitz_f2 and val[0] == 'x1':
            val[3] = '+'
        if 'x2' in opt_gurvitz_f2 and val[0] == 'x2':
            val[3] = '+'
        if 'x3' in opt_gurvitz_f2 and val[0] == 'x3':
            val[3] = '+'
        if 'x4' in opt_gurvitz_f2 and val[0] == 'x4':
            val[3] = '+'
        if 'x5' in opt_gurvitz_f2 and val[0] == 'x5':
            val[3] = '+'
        if 'x6' in opt_gurvitz_f2 and val[0] == 'x6':
            val[3] = '+'
        if 'x7' in opt_gurvitz_f2 and val[0] == 'x7':
            val[3] = '+'
        if 'x8' in opt_gurvitz_f2 and val[0] == 'x8':
            val[3] = '+'
        if 'x1' in opt_laplas_f2 and val[0] == 'x1':
            val[4] = '+'
        if 'x2' in opt_laplas_f2 and val[0] == 'x2':
            val[4] = '+'
        if 'x3' in opt_laplas_f2 and val[0] == 'x3':
            val[4] = '+'
        if 'x4' in opt_laplas_f2 and val[0] == 'x4':
            val[4] = '+'
        if 'x5' in opt_laplas_f2 and val[0] == 'x5':
            val[4] = '+'
        if 'x6' in opt_laplas_f2 and val[0] == 'x6':
            val[4] = '+'
        if 'x7' in opt_laplas_f2 and val[0] == 'x7':
            val[4] = '+'
        if 'x8' in opt_laplas_f2 and val[0] == 'x8':
            val[4] = '+'

    i = 0
    max_sum = []
    for line in values:
        summ = 0
        for el in line:
            if el == "+":
                summ += 1
        max_sum.append(summ)
        values[i].append(str(summ))
        i += 1

    maxim = max(max_sum)

    tree.tag_configure('my_tag', background="lightgreen")

    x_opt_f2 = []
    for value in values:
        if value[-1] == str(maxim):
            tree.insert("", END, values=value, tags='my_tag')
            x_opt_f2.append(value[0])
        else:
            tree.insert("", END, values=value)
    Label(tab_6, text="Оптимальное решение для f2: " + str(x_opt_f2), height=5, font=my_Font).pack()

    return x_opt, x_opt_f2


def vector_maksimin(tab_7):
    Label(tab_7, text="Множество точек крайнего пессимизма ", height=5, font=my_Font).pack()

    columns = (" ", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8")
    tree = ttk.Treeview(tab_7, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.column("#7", stretch=NO, width=80, anchor='c')
    tree.column("#8", stretch=NO, width=80, anchor='c')
    tree.column("#9", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("x1", text="x1")
    tree.heading("x2", text="x2")
    tree.heading("x3", text="x3")
    tree.heading("x4", text="x4")
    tree.heading("x5", text="x5")
    tree.heading("x6", text="x6")
    tree.heading("x7", text="x7")
    tree.heading("x8", text="x8")

    values = [["v1", 1, 3, 3, 2, 2, 4, 4, 6], ["v2", 4, 2, 1, 3, 6, 4, 5, 7]]
    for value in values:
        tree.insert("", END, values=value)

    # сетка
    fig, ax = plt.subplots(figsize=(10, 8))

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))

    # массив точек
    mass = [["v1", 1, 4], ["v2", 3, 2], ["v3", 3, 1], ["v4", 2, 3], ["v5", 2, 6], ["v6", 4, 4], ["v7", 4, 5],
            ["v8", 6, 7]]

    mas_count = []
    mass_effective = []
    mass_optim = []
    for i in range(0, 8):
        count = 0
        x_current = mass[i][1]
        y_current = mass[i][2]
        # Построение конусов доминирования
        # plt.vlines(x=x_current, ymin=y_current, ymax=y_current+4, colors='k')
        # plt.hlines(y=y_current, xmin=x_current, xmax=x_current+4, colors='k')
        for j in range(1, len(mass)):
            if mass[j][1] > x_current and mass[j][2] > y_current:
                count += 1
            else:
                if (mass[j][1] > x_current and mass[j][2] == y_current) or (mass[j][2] > y_current and mass[j][1] == x_current):
                    count += 1
        mas_count.append([i + 1, count])

    # отрисовка точек по цветам
    for i in range(len(mass)):
        if mas_count[i][1] == 0:
            plt.plot(mass[i][1], mass[i][2], 'ro')
            plt.text(mass[i][1] + 0.1, mass[i][2], mass[i][0])

            mass_effective.append(mass[i][0])
            mass_optim.append(mass[i][0].replace("v", "x"))
        else:
            plt.plot(mass[i][1], mass[i][2], 'ko')
            plt.text(mass[i][1] + 0.1, mass[i][2], mass[i][0])

    Label(tab_7, text="Множество эффективных решений Vp = { " + str(mass_effective) + " }", height=5, font=my_Font).pack()
    Label(tab_7, text="Множество оптимальных проектов Xp = { " + str(mass_optim) + " }", height=5, font=my_Font).pack()

    plt.grid()
    # plt.show()
    return mass_optim


def minimaks_sozhalenie(tab_8):
    Label(tab_8, text="Множество идеальных точек W(Z) ", height=5, font=my_Font).pack(anchor='nw')

    columns = (" ", "z1", "z2", "z3", "z4")
    tree = ttk.Treeview(tab_8, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.pack(side=LEFT)
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")

    values = [["w1", 9, 7, 8, 14], ["w2", 10, 9, 8, 13]]
    for value in values:
        tree.insert("", END, values=value)

    Label(tab_8, text="Векторные риски U(x,z) ", height=5, font=my_Font).pack(anchor='n')

    columns = (" ", "z1", "z2", "z3", "z4")
    tree = ttk.Treeview(tab_8, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.pack(anchor='center')
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")

    values = [["x1", "(8, 2)", "(3, 4)", "(6, 4)", "(6, 1)"],
              ["x2", "(1, 8)", "(2, 3)", "(5, 5)", "(4, 4)"],
              ["x3", "(6, 9)", "(3, 7)", "(3, 5)", "(1, 9)"],
              ["x4", "(4, 5)", "(5, 6)", "(0, 4)", "(10, 7)"],
              ["x5", "(7, 4)", "(2, 2)", "(5, 0)", "(5, 3)"],
              ["x6", "(0, 6)", "(1, 4)", "(4, 2)", "(3, 0)"],
              ["x7", "(5, 0)", "(2, 3)", "(2, 3)", "(0, 2)"],
              ["x8", "(3, 2)", "(0, 0)", "(0, 1)", "(5, 4)"], ]
    for value in values:
        tree.insert("", END, values=value)

    Label(tab_8, text="Множество точек крайнего пессимизма V(X)", height=5, font=my_Font).pack()

    columns = (" ", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8")
    tree = ttk.Treeview(tab_8, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.column("#7", stretch=NO, width=80, anchor='c')
    tree.column("#8", stretch=NO, width=80, anchor='c')
    tree.column("#9", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text=" ")
    tree.heading("x1", text="x1")
    tree.heading("x2", text="x2")
    tree.heading("x3", text="x3")
    tree.heading("x4", text="x4")
    tree.heading("x5", text="x5")
    tree.heading("x6", text="x6")
    tree.heading("x7", text="x7")
    tree.heading("x8", text="x8")

    values = [["v1", 8, 5, 6, 10, 7, 4, 5, 5], ["v2", 4, 8, 9, 7, 4, 6, 3, 4]]
    for value in values:
        tree.insert("", END, values=value)

    # сетка
    fig, ax = plt.subplots(figsize=(10, 8))

    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)

    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))

    # массив точек
    mass = [["v1", 8, 4], ["v2", 5, 8], ["v3", 6, 9], ["v4", 10, 7],
            ["v5", 7, 4], ["v6", 4, 6], ["v7", 5, 3], ["v8", 5, 4]]

    mas_count = []
    mass_effective = []
    mass_optim = []
    for i in range(0, 8):
        count = 0
        x_current = mass[i][1]
        y_current = mass[i][2]
        # # Построение обратных конусов доминирования
        # plt.vlines(x=x_current, ymin=y_current, ymax=y_current - 4, colors='k')
        # plt.hlines(y=y_current, xmin=x_current, xmax=x_current - 4, colors='k')
        for j in range(0, len(mass)):
            if mass[j][1] < x_current and mass[j][2] < y_current:# and (mass[j][1] != x_current or mass[j][2] != y_current):
                count += 1
            else:
                if (mass[j][1] < x_current and mass[j][2] == y_current) or (mass[j][2] < y_current and mass[j][1] == x_current):
                    count += 1

        mas_count.append([i + 1, count])

    # отрисовка точек по цветам
    for i in range(len(mass)):
        if mas_count[i][1] == 0:
            plt.plot(mass[i][1], mass[i][2], 'ro')
            plt.text(mass[i][1] + 0.1, mass[i][2], mass[i][0])

            mass_effective.append(mass[i][0])
            mass_optim.append(mass[i][0].replace("v", "x"))
        else:
            plt.plot(mass[i][1], mass[i][2], 'ko')
            plt.text(mass[i][1] + 0.1, mass[i][2], mass[i][0])

    Label(tab_8, text="Vp = { " + str(mass_effective) + " }", height=5, font=my_Font).pack()
    Label(tab_8, text="Xp = { " + str(mass_optim) + " }", height=5, font=my_Font).pack()

    plt.grid()
    return mass_optim


def final_matrix(tab_9, opt_maximin, opt_minimaks_sozh, opt_f1, opt_f2):
    Label(tab_9, text="Итоговая матрица Голосования", height=5, font=my_Font).pack()

    columns = (" ", "максимин", "сожаление", "f1", "f2", "sum")
    tree = ttk.Treeview(tab_9, columns=columns, show="headings")

    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=220, anchor='c')
    tree.column("#3", stretch=NO, width=220, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack()
    tree.heading(" ", text="\\\\\\\\\\")
    tree.heading("максимин", text="Векторный максимин\n")
    tree.heading("сожаление", text="Минимаксное сожаление\n")
    tree.heading("f1", text="f1\n")
    tree.heading("f2", text="f2\n")
    tree.heading("sum", text="Σ")
    values = [["x1", "", "", "", ""], ["x2", "", "", "", ""], ["x3", "", "", "", ""],
              ["x4", "", "", "", ""], ["x5", "", "", "", ""], ["x6", "", "", "", ""],
              ["x7", "", "", "", ""], ["x8", "", "", "", ""]]

    for val in values:
        if 'x1' in opt_maximin and val[0] == 'x1':
            val[1] = '+'
        if 'x2' in opt_maximin and val[0] == 'x2':
            val[1] = '+'
        if 'x3' in opt_maximin and val[0] == 'x3':
            val[1] = '+'
        if 'x4' in opt_maximin and val[0] == 'x4':
            val[1] = '+'
        if 'x5' in opt_maximin and val[0] == 'x5':
            val[1] = '+'
        if 'x6' in opt_maximin and val[0] == 'x6':
            val[1] = '+'
        if 'x7' in opt_maximin and val[0] == 'x7':
            val[1] = '+'
        if 'x8' in opt_maximin and val[0] == 'x8':
            val[1] = '+'
        if 'x1' in opt_minimaks_sozh and val[0] == 'x1':
            val[2] = '+'
        if 'x2' in opt_minimaks_sozh and val[0] == 'x2':
            val[2] = '+'
        if 'x3' in opt_minimaks_sozh and val[0] == 'x3':
            val[2] = '+'
        if 'x4' in opt_minimaks_sozh and val[0] == 'x4':
            val[2] = '+'
        if 'x5' in opt_minimaks_sozh and val[0] == 'x5':
            val[2] = '+'
        if 'x6' in opt_minimaks_sozh and val[0] == 'x6':
            val[2] = '+'
        if 'x7' in opt_minimaks_sozh and val[0] == 'x7':
            val[2] = '+'
        if 'x8' in opt_minimaks_sozh and val[0] == 'x8':
            val[2] = '+'
        if 'x1' in opt_f1 and val[0] == 'x1':
            val[3] = '+'
        if 'x2' in opt_f1 and val[0] == 'x2':
            val[3] = '+'
        if 'x3' in opt_f1 and val[0] == 'x3':
            val[3] = '+'
        if 'x4' in opt_f1 and val[0] == 'x4':
            val[3] = '+'
        if 'x5' in opt_f1 and val[0] == 'x5':
            val[3] = '+'
        if 'x6' in opt_f1 and val[0] == 'x6':
            val[3] = '+'
        if 'x7' in opt_f1 and val[0] == 'x7':
            val[3] = '+'
        if 'x8' in opt_f1 and val[0] == 'x8':
            val[3] = '+'
        if 'x1' in opt_f2 and val[0] == 'x1':
            val[4] = '+'
        if 'x2' in opt_f2 and val[0] == 'x2':
            val[4] = '+'
        if 'x3' in opt_f2 and val[0] == 'x3':
            val[4] = '+'
        if 'x4' in opt_f2 and val[0] == 'x4':
            val[4] = '+'
        if 'x5' in opt_f2 and val[0] == 'x5':
            val[4] = '+'
        if 'x6' in opt_f2 and val[0] == 'x6':
            val[4] = '+'
        if 'x7' in opt_f2 and val[0] == 'x7':
            val[4] = '+'
        if 'x8' in opt_f2 and val[0] == 'x8':
            val[4] = '+'

    i = 0
    max_sum = []
    for line in values:
        summ = 0
        for el in line:
            if el == "+":
                summ += 1
        max_sum.append(summ)
        values[i].append(str(summ))
        i += 1

    maxim = max(max_sum)

    tree.tag_configure('my_tag', background="lightgreen")

    x_opt = []
    for value in values:
        if value[-1] == str(maxim):
            tree.insert("", END, values=value, tags='my_tag')
            x_opt.append(value[0])
        else:
            tree.insert("", END, values=value)

    Label(tab_9, text="Окончательное оптимальное решение : " + str(x_opt), height=5, font=my_Font).pack(fill=BOTH)


class Window:
    def __init__(self, width, height, title="Window"):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title(title)

        ttk.Style().configure('.', font=my_Font)
        ttk.Style().configure("Treeview.Heading", font=my_Font)

        self.tabs_control = Notebook(self.root, height=100, width=30, padding=(10, 20, 10, 20))
        self.tabs_control.enable_traversal()

        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="Матрица")

        self.tab_2 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_2, text="Критерий Вальда")

        self.tab_3 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_3, text="Критерий Сэвиджа")

        self.tab_4 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_4, text="Критерий Гурвица")

        self.tab_5 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_5, text="Критерий Лапласа")

        self.tab_6 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_6, text="Матрица Голосования")

        self.tab_7 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_7, text="Векторный максимин")

        self.tab_8 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_8, text="Минимаксное сожаление")

        self.tab_9 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_9, text="Итоговая матрица")

    def run(self):
        self.solve_kdz()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def solve_kdz(self):
        self.draw_menu()
        self.tabs_control.pack(fill=BOTH, expand=1)

        values = [["x1", 1, 4, 2, 8], ["x2", 8, 5, 3, 10], ["x3", 3, 4, 5, 13], ["x4", 5, 2, 8, 4],
                  ["x5", 2, 5, 3, 9], ["x6", 9, 6, 4, 11], ["x7", 4, 5, 6, 14], ["x8", 6, 7, 8, 9]]
        values_int = [[1, 4, 2, 8], [8, 5, 3, 10], [3, 4, 5, 13], [5, 2, 8, 4],
                      [2, 5, 3, 9], [9, 6, 4, 11], [4, 5, 6, 14], [6, 7, 8, 9]]

        values_f2 = [["x1", 8, 5, 4, 12], ["x2", 2, 6, 3, 9], ["x3", 1, 2, 3, 4], ["x4", 5, 3, 4, 6],
                     ["x5", 6, 7, 8, 10], ["x6", 4, 5, 6, 13], ["x7", 10, 6, 5, 11], ["x8", 8, 9, 7, 9]]

        values_int_f2 = [[8, 5, 4, 12], [2, 6, 3, 9], [1, 2, 3, 4], [5, 3, 4, 6],
                         [6, 7, 8, 10], [4, 5, 6, 13], [10, 6, 5, 11], [8, 9, 7, 9]]

        # Матрица
        main_matrix(self.tab_1, values, values_f2)

        # Вальд
        opt_wald, opt_wald_f2 = wald(self.tab_2, values, values_int, values_f2, values_int_f2)

        # Сэвидж
        opt_savage, opt_savage_f2 = savage(self.tab_3, values, values_int, values_f2, values_int_f2)

        # Гурвиц
        opt_gurvitz, opt_gurvitz_f2 = gurvitz(self.tab_4, values, values_int, values_f2, values_int_f2)

        # Лаплас
        opt_laplas, opt_laplas_f2 = laplas(self.tab_5, values, values_int, values_f2, values_int_f2)

        # Голосование
        opt_f1, opt_f2 = golosovanie(self.tab_6, opt_wald, opt_savage, opt_gurvitz, opt_laplas, opt_wald_f2, opt_savage_f2,
                    opt_gurvitz_f2, opt_laplas_f2)
        print(opt_f1, opt_f2)

        # Векторный максимин
        opt_maximin = vector_maksimin(self.tab_7)
        print(opt_maximin)

        # Манимакскное сожаление
        opt_minimaks_sozh = minimaks_sozhalenie(self.tab_8)
        print(opt_minimaks_sozh)

        final_matrix(self.tab_9, opt_maximin, opt_minimaks_sozh, opt_f1, opt_f2)

        # Показать графики
        plt.show()

    def draw_menu(self):
        menu_bar = Menu(self.root)

        self.root.configure(menu=menu_bar)


if __name__ == "__main__":
    window = Window(800, 500, "KDZ 1")
    window.run()
