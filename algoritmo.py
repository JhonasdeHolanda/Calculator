import math

def tabuada(num1, num_final, operacao):
    if operacao == 1:
        return num1 + num_final
    elif operacao == 2:
        return num1 - num_final
    elif operacao == 3:
        return num1 * num_final
    elif operacao == 4:
        return num1 / num_final
    elif operacao == 5:
        return num1 ** num_final

while True:
    print("Escolha a sua operação matemática")
    print("1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- potenciação\n6- raiz quadrada\n7- porcentagem\n8- sair")
    operacao = int(input("Digite sua operação escolhida: "))
    
    if operacao == 8:
        break

    elif operacao in [1, 2, 3, 4, 5]:
        num1 = float(input("Digite o primeiro número: "))
        num_final = float(input("Digite o segundo número: "))

        resultado = tabuada(num1, num_final, operacao)
        
        operacoes = ["soma", "subtração", "multiplicação", "divisão", "potenciação"]
        print(f"O resultado da {operacoes[operacao-1]} entre {num1} e {num_final} = {resultado}")

    elif operacao == 6:
        num = float(input("digite o número a ser calculado: "))
        raiz = math.sqrt(num)
        print(f"A raiz quadrada de {num} é: {raiz}")
        
    elif operacao == 7:
        num = float(input("digite o primeiro número: "))
        porcentagem = float(input("digite a porcentagem desejada: "))
        conta = num * (porcentagem / 100)
        print(f"os {porcentagem}% de {num} é: {conta}")

    else:
        print("\n\nOperação inválida! Tente novamente.\n \n")
        continue
    
   