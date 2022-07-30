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
    return None

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

def main():
    arrays = [[1,3,4,2], [1,6142,8192,10239], [2,7,11,15], [3,2,4], [3,3], [-10,-1,-18,-19], [-5, 5]]
    alvos = [6, 18431, 9, 6, 6, -19, -5]

    i = 0
    while i < len(arrays):
        arrayAtual = arrays[i]
        arrayBraba = pegarArrayBraba(arrayAtual)
        resultadoON2 = oN2(arrayAtual, alvos[i])
        resultadoON = oN(arrayAtual, arrayBraba, alvos[i])

        if resultadoON is None:
            print(resultadoON2 == resultadoON, ' => ', resultadoON2, ' = ', resultadoON)
            return
            
        print(resultadoON2[0] == resultadoON[0] and resultadoON2[1] == resultadoON[1] or 
            resultadoON2[1] == resultadoON[0] and resultadoON2[0] == resultadoON[1], 
            ' => ', resultadoON2, ' = ', resultadoON)
        i += 1
main()