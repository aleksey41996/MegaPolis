f = open('D:/docs/Student-627/Downloads/24_11241 (1).txt')
s = f.readline()
k = 1
max_pos = 0
g = "ABCD"
for i in range(len(s) - 1):
    if s[i] not in g and s[i+1] not in g:
        k += 1
        max_pos = max(max_pos,k)
    else:
        k = 1
print(max_pos)
