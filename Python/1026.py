def xor_bit_a_bit(n1, n2):
    print(n1 ^ n2)

def executar(i):
    n1, n2 = i.split(" ")
    xor_bit_a_bit(int(n1), int(n2))

while True:
    try:
        i = input()
        executar(i)
    except (EOFError):
        break