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
    
def traducao(num1, operacao):
    if operacao == 8:
        return bin(num1)
    elif operacao == 9:
        return oct(num1)
    elif operacao == 10:
        return hex(num1)

while True:
    print("Escolha a sua operação matemática") 
    print("1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- potenciação\n6- raiz quadrada\n7- porcentagem\n8- binário\n9- octogonal\n10- hexadecimal\n11- sair")
    operacao = int(input("Digite sua operação escolhida: "))
    
    if operacao == 11:
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

    elif operacao in [8, 9, 10]:
        num1 = int(input("Digite o número: "))
        
        resultado1 = traducao(num1,operacao)
        
        operacoes = ["","","","","","","","binário","octogonal","hexadecimal"]
        print(f"O resultado da tradução de {num1} para {operacoes[operacao-1]} é: {resultado1}")

    else:
        print("Operação inválida! Tente novamente.")
        continue
    
   