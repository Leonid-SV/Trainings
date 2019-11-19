import re
rows = []
table = []

file = open("Euler task 11 Table.txt", "r")

# Получение списка из строчек таблицы
for line in file:
    rows.append(line)

file.close()

q_rows = len(rows)  # колиечество строк в таблице
q_col = q_rows      # колиечество столбцов в таблице



# получение элементов строчек таблицы и их запись в
for i in range(q_rows):
    new_row = []
    for element in rows[i].split(" "):
        element = int(re.search(r'\w{2}', element)[0])
        new_row.append(element)
    table.append(new_row)

def direction():
# функция направления умножения по восьми направлениям от элемента таблицы
    dir = []
    for ver in [-1, 0, 1]:
        for hor in [-1, 0, 1]:
            if ver == 0 and hor == 0:
                continue
            dir.append([ver, hor])
    return dir

print(direction())


def multiple(tab, y, x, dir):
    # произведение 4х последовательных элементов/
    # таблицы по выбранному направлению dir
    mul = 1
    for step in range(4):
        mul *= tab[y+step*dir[0]][x+step*dir[1]]
   # print(tab[y][x])
    return mul

# создание расширенной таблицы на 4 нулевых строки и столбца в каждую сторону

table_exp = []
for exp_i in range(q_rows + 8):
    row_exp = []
    for exp_j in range(q_col + 8):
        cond_1 = exp_i >= 4
        cond_2 = exp_i <= q_rows + 3
        cond_3 = exp_j >= 4
        cond_4 = exp_j <= q_col + 3
        cond = cond_1 & cond_2 & cond_3 & cond_4
        x = table[exp_i - 4][exp_j - 4] if cond else 0
        row_exp.append(x)
    table_exp.append(row_exp)
'''
for k in range (q_rows + 8):
    print(table_exp[k])
print(len(table_exp[k]))
'''

# поиск максимального произведения в расширенной таблице в каждой точе таблицы по всем направлениям
max_mul = 1

for ii in range(4, 24):
    for jj in range(4, 24):
        for d in range(8):
            m = multiple(table_exp, ii, jj, direction()[d])
            if m > max_mul:
                max_mul = m
                coord_row = ii - 4
                coord_col = jj - 4


print(" ------------------------------------- ")
print("Максимальное произведение 4-х подряд элметов в таблице = ", max_mul)
print("Координаты точки: строка ", coord_row, ", столбец: ", coord_col)
print(" ------------------------------------- ")
