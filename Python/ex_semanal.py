n = int(input())
l = []
c = 0

for i in range(0,n):
    p = input()
    

    print('c -> ', c)
    
    if p in l:
        c += 1

    l.append(p)

print("Falta(m) {} pomekon(s).".format(151 - (n-c)))