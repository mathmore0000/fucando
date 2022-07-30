import random
import time

def oN2(array, alvo):
    i = 0
    while i < len(array)-1:
        i += 1
        j = 0
        while j < len(array)-1:
            if i != j and array[i] + array[j] == alvo:
                return [i, j]
            j += 1
    print('nada encontrado')

def pegarArrayBraba(array):
    if (min(array)*-1) > max(array):
        arrayBraba = [None] * ((min(array)*-1)+1)
    else:
        arrayBraba = [None] * (max(array)+1)
    
    i = 0
    while i < len(array):
        if 0 > array[i]:
            arrayBraba[array[i]*-1] = i
        else:
            arrayBraba[array[i]] = i
        i += 1
    return arrayBraba

def oN(array, arrayBraba, alvo):
    i = 0
    while i < len(array):
        try:
            indexSubAlvo = arrayBraba[alvo - array[i]]
            if indexSubAlvo != i and array[i] + array[indexSubAlvo] == alvo:
                return [i, indexSubAlvo]
        except:
            try:
                indexSubAlvo = arrayBraba[(alvo - array[i])*-1]
                if indexSubAlvo != i and array[i] + array[indexSubAlvo] == alvo:
                    return [i, indexSubAlvo]
            except:
                pass
        i += 1

# import random and generate random array with 10000 unique random numbers between 0 and 25000
array = random.sample(range(0, 25000), 10000)
inicio = time.time()
resultadoON2 = oN2(array, 988)
print('O(N2) - ', time.time() - inicio)
print(resultadoON2)
print(array[resultadoON2[0]], array[resultadoON2[1]])
print(array[resultadoON2[0]] + array[resultadoON2[1]])

print()

inicio = time.time()
arrayBraba = pegarArrayBraba(array)
resultadoON = oN(array, arrayBraba, 988)
print('O(N) - ', time.time() - inicio)
print(resultadoON)
print(array[resultadoON[0]], array[resultadoON[1]])
print(array[resultadoON[0]] + array[resultadoON[1]])