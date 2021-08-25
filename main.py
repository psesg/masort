mas = [10,16,6,13,11,18,8,5,9,0,2,15,4,3,7,14,12,19,1,17]
#mas = [4,3,1,2]
print(mas)

k = 0
while True:
    maxv = 0
    m, n = 0, 0
    l = 0
    for i in range(0, len(mas)):
        for j in range(i+1, len(mas)):
            #print(mas[i], mas[j])
            if mas[i] > mas[j] and i < j:
                l+=1
                if mas[i] - mas[j] > maxv:
                    m, n = i, j
                    maxv = mas[i] - mas[j]
    if m != 0 or n != 0:
        a = mas[m]
        mas[m] = mas[n]
        mas[n] = a
        k+=1
    if l == 0:
        break

print('k ='.format({}),k)
print(mas)