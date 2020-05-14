def odometer (oksana):
    kilom = 0
    time = 0
    if len(oksana) % 2 == 0:
        for j in range (0, len (oksana), 2):
            kilom += oksana [j] * (oksana [j + 1] - time)
            time = oksana [j + 1]
        return kilom
    else:
        for j in range (0, len (oksana) - 1, 2):
            kilom += oksana [j] * (oksana [j + 1] - time)
            time = oksana [j + 1]
        return kilom
