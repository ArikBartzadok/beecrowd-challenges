while True:
    try:
        n = int(input())
        lista = []
    
        for i in range(n):
            e = input()
            n -= 1

            lista.append(e)

            lista.sort()
                
        for j in lista:
            print(j)
        
    except (EOFError):
        break

# 3
# 1233
# 0015
# 0100

# 7
# 0752
# 1110
# 0001
# 6322
# 8000
# 6321
# 0000