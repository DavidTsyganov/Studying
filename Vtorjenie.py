def ConquestCampaign(N, M, L, battalion):
    a = []
    for i in range(N):  # Цикл по строкам.
        b = []  # Подготовка вложенного списка.
        for j in range(M):  # Цикл по столбцам.
            b.append(0)  # Заполнение двумерного списка нулями.
        a.append(b)  # Добавление подсписков в основной список.

    for i in range(len(battalion)): #Цикл, организующий высадку десантников по координатам. Точкам высадки присваивается 1.
        if i == 0 or i % 2 == 0:
            for k in range(len(a) + 1):
                if k == battalion[i]:
                    for j in range(len(b) + 1):
                        if battalion[i + 1] == j:
                            a[k - 1][j - 1] = 1
    for i in range(len(a)): #Цикл, увеличивающий на +1 координату высадки в первый день.
        for j in range(len(b)):
            if a[i][j] != 0:
                a[i][j] += 1
    for i in range(len(a)): #Проверка заполнения всех клеток.
        for j in range(len(b)):
            if a[i][j] == 0:
                proverka = False # При заполнении не всех клеток. Происходит дальнейший захват.
                break
            else:
                proverka = True # При заполнении всех клеток. День захвата - 1. Дальнейший захват не происходит.

    if proverka == True:
        k = 1
    else:
        k = 0
        while proverka == False: # Цикл выполняется пока есть незахваченные клетки.
            for i in range(len(a)): # Проверка наличия свободных клеток.
                for j in range(len(b)):
                    if a[i][j] == 0:
                        proverka = False
                        break
                    else:
                        proverka = True
                        break

            for i in range(len(a)): # Следующие циклы заполняют соседние клетки уже заполненных клеток.
                for j in range(len(b)):
                    if a[i][j] != 0:
                        a[i][j] += 1

            for i in range(len(a)):
                for j in range(len(b) - 1):
                    if a[i][j] == 0 and a[i][j + 1] >= 2:
                        a[i][j] += 1

            for i in range(len(a)):
                for j in range(len(b) - 1, 0, -1):
                    if a[i][j] == 0 and a[i][j - 1] >= 2:
                        a[i][j] += 1

            for j in range(len(b)):
                for i in range(len(a) - 1):
                    if a[i][j] == 0 and a[i + 1][j] >= 2:
                        a[i][j] += 1

            for j in range(len(b)):
                for i in range(len(a) - 1, 0, -1):
                    if a[i][j] == 0 and a[i - 1][j] >= 2:
                        a[i][j] += 1
            k += 1 # Подсчет количества дней, прошедших с момента начала операции захвата.
    return k
