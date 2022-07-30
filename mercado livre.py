def pegarNumeros(maxDigit):
    numerosPossiveis = []
    num = 6000
    
    while num < int((str(maxDigit)*4)):
        # if verificarMaxDigits(num, maxDigit): # se algum numero for maior que o maxDigit pula para proxima iteracao
        #     num = num + 1
        #     continue

        # j = 0
        # soma = 0
        # while j < 4:
        #     soma = soma + int(str(num)[j])
        #     j = j + 1

        soma = 0
        j = 0
        while j < 4:
            if int(str(num)[j]) > maxDigit:
                num = num + 1
                break
            soma = soma + int(str(num)[j])
            j = j + 1
        # se algum numero for maior que o maxDigit pula para a proxima iteração (de uma vez)
        # se não => soma = num[0] + num[1] + num[2] + num[3]

        if soma == 21:
            numerosPossiveis.append(num)
        num = num + 1
    return numerosPossiveis

print(pegarNumeros(6))