Str1 = input()
Str2 = input()
S1 = list(Str1)
S2 = list(Str2)
M = len(S2)
N = len(S1)
k = 0
for i in range (N):
    if S1[i] == S2[k]:
        k += 1
        if k == M:
            break
    else:
        k = 0
if k == M:
    print ("Содержится")
else:
    print ("Не содержится")
