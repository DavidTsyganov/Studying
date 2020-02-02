Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Str1 = input()
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