def PutternUnlock(N, hits):
    diag = [26, 29, 27, 24, 62, 92, 42, 72, 15, 51, 18, 81, 53, 35, 83, 38]
    combination = []
    a = 0
    summa = 0
    SUMMA = []

    for i in range(N - 1):
        a = str(hits[i]) + str(hits[i + 1])
        combination.append(a)

    for i in range(N - 1):
        flag = False
        for j in range(len(diag)):
            if combination[i] == str(diag[j]):
                summa += 2 ** 0.5
                flag = True
                break
        if flag == False:
            summa += 1

    summa_itog = int(summa * 100000 + 0.5)

    summa_str = str(summa_itog)
    K = len(summa_str)

    summa_list = list(summa_str)

    for i in range(K):
        if summa_list[i] != "0":
            SUMMA.append(summa_list[i])
    SUMMA = "".join(SUMMA)
    return str(SUMMA)
