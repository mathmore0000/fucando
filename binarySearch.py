from datetime import datetime
import numpy as np

def acharInArrayB(array, valor):
    i = 0
    menor = 0
    maior = len(array)-1

    while (maior >= menor):
        medio = menor + (maior - menor) // 2
        
        if (array[medio] == valor): 
            return {"index": medio, "passos": i}

        elif (array[medio] > valor): 
            maior = medio - 1

        elif (array[medio] < valor): 
            menor = medio + 1
        i = i+1            
        
    return {"index": -1, "passos": i}

def acharInArrayL(array, valor):
    i = 0
    while (i < len(array)):
        if (array[i] == valor): return i
        i = i + 1
    return -1 

def main():
    array = np.loadtxt("array.txt", dtype=int)
    valor =  854666 #1854666
    binary = ""

    print("Pesquisar com binary search --")

    agora = datetime.now()

    resposta = acharInArrayB(array, valor)
    tempoDecorridoB = datetime.now() - agora
    index = resposta["index"]
    passos = resposta["passos"]

    if (index != -1): 
        print(f"{str(index)} - {str(array[index])}")
    else:
        print("valor não encontrado na array")
        binary = " não"
    #print(f"Binary search levou {str(passos)} passos para{binary} achar")

    print("")

    print("Pesquisar com loop while comum --")

    agora = datetime.now()

    index = acharInArrayL(array, valor)
    #print("Linear search levou " + str(index) + " passos para achar")

    tempoDecorridoL = datetime.now() - agora

    if (index != -1): 
        print(f"{str(index)} - {str(array[index])}")
    else:
        print("valor não encontrado na array") 

    print("")

    print(f"Tempo decorrido B -  {str(tempoDecorridoB)}")
    print(f"Tempo decorrido L -  {str(tempoDecorridoL)}")

main()