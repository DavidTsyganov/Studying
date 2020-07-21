def SynchronizingTables(N, ids, salary):
    result = []
    copy_ids = ids[:]

    for i in range(N):
        for j in range(i + 1, N):
            if ids[i] > ids[j]:
                ids[i], ids[j] = ids[j], ids[i]
    for i in range(N):
        for j in range(i + 1, N):
            if salary[i] > salary[j]:
                salary[i], salary[j] = salary[j], salary[i]
    for i in range(N):
        for j in range(N):
            if copy_ids[i] == ids[j]:
                result.append(salary[j])
    return result