from tkinter import *
from copy import deepcopy
from tkinter import messagebox as mb
# from tkinter.scrolledtext import ScrolledText
# from tkinter import filedialog as fd
from tkinter.ttk import Notebook
from tkinter import ttk


def main_matrix(tab_1, values):
    Label(tab_1, text="Матрица Q : ", height=5).pack()

    columns = (" ", "z1", "z2", "z3", "z4")
    tree = ttk.Treeview(tab_1, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.pack(fill=BOTH, expand=1)
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    for value in values:
        tree.insert("", END, values=value)


def gurvitz(tab_4, values, values_int):
    Label(tab_4, text="α = 0.6", height=5).pack()
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
    tree.pack(fill=BOTH, expand=1)
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
    Label(tab_4, text="Оптимальное решение по критерию Гурвица : " + str(x_opt), height=5).pack()
    return x_opt


def bayes(tab_5, values, values_int):
    Label(tab_5, text="p=[0,1; 0,4; 0,4; 0,1]", height=5).pack()
    p1 = 0.1
    p2 = 0.4
    p3 = 0.4
    p4 = 0.1

    copy_values = deepcopy(values)

    i = 0
    D = []
    for line in values_int:
        t = round(p1 * line[0] + p2 * line[1] + p3 * line[2] + p4 * line[3], 2)
        D.append(t)
        copy_values[i].append(t)
        i += 1
    maxim = max(D)

    columns = (" ", "z1", "z2", "z3", "z4", "D")
    tree = ttk.Treeview(tab_5, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack(fill=BOTH, expand=1)
    tree.heading(" ", text=" ")
    tree.heading("z1", text="z1")
    tree.heading("z2", text="z2")
    tree.heading("z3", text="z3")
    tree.heading("z4", text="z4")
    tree.heading("D", text="D")
    tree.tag_configure('my_tag', background='lightgreen')
    x_opt = []
    for value in copy_values:
        if value[-1] == maxim:
            tree.insert("", END, values=value, tags='my_tag')
            x_opt.append(value[0])
        else:
            tree.insert("", END, values=value)
    Label(tab_5, text="Оптимальное решение по критерию Байеса : " + str(x_opt), height=5).pack()
    return x_opt


def wald(tab_2, values, values_int):
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
    tree.pack(fill=BOTH, expand=1)
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
    Label(tab_2, text="Оптимальное решение по критерию Вальда : " + str(x_opt), height=5).pack()
    return x_opt


def savage(tab_3, values, values_int):
    Label(tab_3, text="Матрица рисков Q → R : ", height=5).pack()
    copy_values = deepcopy(values)
    # max_el_in_col = []
    # mx = 0
    # j = 0
    # for j in range(len(values_int[j])):
    #     mx = values_int[0][j]
    #     for i in range(len(values_int)):
    #         if values_int[i][j] > mx:
    #             mx = values_int[i][j]
    #     max_el_in_col.append(mx)
    #     print(" |%3d| " % mx, end='')
    matrix_r_x = [['x1', 8, 3, 6, 6], ['x2',1, 2, 5, 4], ['x3',6, 3, 3, 1], ['x4',4, 5, 0, 10],
                 ['x5',7, 2, 5, 5], ['x6',0, 1, 4, 3], ['x7',5, 2, 2, 0], ['x8',3, 0, 0, 5]]
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
    tree.pack(fill=BOTH, expand=1)
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
    Label(tab_3, text="Оптимальное решение по критерию Сэвиджа : " + str(x_opt), height=5).pack()
    return x_opt


def laplas(tab_6, values, values_int):
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
    tree = ttk.Treeview(tab_6, columns=columns, show="headings")
    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.pack(fill=BOTH, expand=1)
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
    Label(tab_6, text="Оптимальное решение по критерию Лапласа : " + str(x_opt), height=5).pack()
    return x_opt


def golosovanie(tab_7, opt_wald, opt_savage, opt_gurvitz, opt_bayes, opt_laplas):
    columns = (" ", "Вальд", "Сэвидж", "Гурвиц", "Байес", "Лаплас", "sum")
    tree = ttk.Treeview(tab_7, columns=columns, show="headings")

    tree.column("#1", stretch=NO, width=80, anchor='c')
    tree.column("#2", stretch=NO, width=80, anchor='c')
    tree.column("#3", stretch=NO, width=80, anchor='c')
    tree.column("#4", stretch=NO, width=80, anchor='c')
    tree.column("#5", stretch=NO, width=80, anchor='c')
    tree.column("#6", stretch=NO, width=80, anchor='c')
    tree.column("#7", stretch=NO, width=80, anchor='c')
    tree.pack(fill=BOTH, expand=1)
    tree.heading(" ", text="\\\\\\\\\\")
    tree.heading("Вальд", text="Вальд\n")
    tree.heading("Сэвидж", text="Сэвидж\n")
    tree.heading("Гурвиц", text="Гурвиц\n")
    tree.heading("Байес", text="Байес\n")
    tree.heading("Лаплас", text="Лаплас\n")
    tree.heading("sum", text="Σ")
    values = [["x1", "", "", "", "", ""], ["x2", "", "", "", "", ""], ["x3", "", "", "", "", ""],
              ["x4", "", "", "", "", ""], ["x5", "", "", "", "", ""], ["x6", "", "", "", "", ""],
              ["x7", "", "", "", "", ""], ["x8", "", "", "", "", ""]]

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
        if 'x5' in opt_wald and val[0] == 'x7':
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
        if 'x1' in opt_bayes and val[0] == 'x1':
            val[4] = '+'
        if 'x2' in opt_bayes and val[0] == 'x2':
            val[4] = '+'
        if 'x3' in opt_bayes and val[0] == 'x3':
            val[4] = '+'
        if 'x4' in opt_bayes and val[0] == 'x4':
            val[4] = '+'
        if 'x5' in opt_bayes and val[0] == 'x5':
            val[4] = '+'
        if 'x6' in opt_bayes and val[0] == 'x6':
            val[4] = '+'
        if 'x7' in opt_bayes and val[0] == 'x7':
            val[4] = '+'
        if 'x8' in opt_bayes and val[0] == 'x8':
            val[4] = '+'
        if 'x1' in opt_laplas and val[0] == 'x1':
            val[5] = '+'
        if 'x2' in opt_laplas and val[0] == 'x2':
            val[5] = '+'
        if 'x3' in opt_laplas and val[0] == 'x3':
            val[5] = '+'
        if 'x4' in opt_laplas and val[0] == 'x4':
            val[5] = '+'
        if 'x5' in opt_laplas and val[0] == 'x5':
            val[5] = '+'
        if 'x6' in opt_laplas and val[0] == 'x6':
            val[5] = '+'
        if 'x7' in opt_laplas and val[0] == 'x7':
            val[5] = '+'
        if 'x8' in opt_laplas and val[0] == 'x8':
            val[5] = '+'

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
    Label(tab_7, text="Оптимальное решение : "+ str(x_opt), height=5).pack()


class Window:
    def __init__(self, width, height, title="MyWindow"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+300+200")
        self.root.geometry("+300+100")

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
        self.tabs_control.add(self.tab_5, text="Критерий Байеса")

        self.tab_6 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_6, text="Критерий Лапласа")

        self.tab_7 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_7, text="Матрица Голосования")

    def run(self):
        self.solve_kdz()
        self.root.mainloop()

    def solve_kdz(self):
        self.draw_menu()
        self.tabs_control.pack(fill=BOTH, expand=1)

        values = [["x1", 1, 4, 2, 8], ["x2", 8, 5, 3, 10], ["x3", 3, 4, 5, 13], ["x4", 5, 2, 8, 4],
                  ["x5", 2, 5, 3, 9], ["x6", 9, 6, 4, 11], ["x7", 4, 5, 6, 14], ["x8", 6, 7, 8, 9]]
        values_int = [[1, 4, 2, 8], [8, 5, 3, 10], [3, 4, 5, 13], [5, 2, 8, 4],
                      [2, 5, 3, 9], [9, 6, 4, 11], [4, 5, 6, 14], [6, 7, 8, 9]]

        # Матрица
        main_matrix(self.tab_1, values)

        # Вальд
        opt_wald = wald(self.tab_2, values, values_int)
        print(opt_wald)

        # Сэвидж
        opt_savage = savage(self.tab_3, values, values_int)
        print(opt_savage)

        # Гурвиц
        opt_gurvitz = gurvitz(self.tab_4, values, values_int)
        print(opt_gurvitz)

        # Байес
        opt_bayes = bayes(self.tab_5, values, values_int)
        print(opt_bayes)

        # Лаплас
        opt_laplas = laplas(self.tab_6, values, values_int)
        print(opt_laplas)

        # Голосование
        golosovanie(self.tab_7, opt_wald, opt_savage, opt_gurvitz, opt_bayes, opt_laplas)


    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_separator()

        self.root.configure(menu=menu_bar)


if __name__ == "__main__":
    window = Window(800, 500, "KDZ 6")
    window.run()
