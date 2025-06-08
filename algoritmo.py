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
    print("1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- potenciação\n6- raiz quadrada\n7- porcentagem\n8- binário\n9- octogonal\n10- hexadecimal\n11- Logartimo \n12- fatorial\n13- sair")
    operacao = int(input("Digite sua operação escolhida: "))
    
    if operacao == 13:
        break

    elif operacao in [1, 2, 3, 4, 5]:
        num1 = float(input("Digite o primeiro número: "))
        num_final = float(input("Digite o segundo número: "))

        resultado = tabuada(num1, num_final, operacao)
           
        operacoes = ["soma", "subtração", "multiplicação", "divisão", "potenciação"]
        if operacao in [1]:
            print(f"O resultado da {operacoes[operacao-1]} entre {num1} + {num_final} = {resultado}")
        elif operacao in [2]:
            print(f"O resultado da {operacoes[operacao-1]} entre {num1} - {num_final} = {resultado}")
        elif operacao in [3]:
            print(f"O resultado da {operacoes[operacao-1]} entre {num1} x {num_final} = {resultado}")
        elif operacao in [4]:
            print(f"O resultado da {operacoes[operacao-1]} entre {num1} / {num_final} = {resultado}")
        else:
            print(f"O resultado da {operacoes[operacao-1]} entre {num1} ** {num_final} = {resultado}")
    elif operacao == 6:
        num = float(input("digite o número que você deseja descobrir a raiz quadrada: "))
        print(f"A raiz quadrada de {num} é: {math.sqrt(num)}")
        
    elif operacao == 7:
        num = float(input("digite o número inteiro : "))
        porcentagem = float(input("digite quantos porcento você deseja saber do número total: "))
        conta = num * (porcentagem / 100)
        print(f"os {porcentagem}% de {num} é: {conta:.2f}")

    elif operacao in [8, 9, 10]:
        num1 = int(input("Digite o número: "))
        
        resultado1 = traducao(num1,operacao)
        
        operacoes = {
        8: "binário",
        9: "octogonal",
        10: "hexadecimal"
        }
        print(f"O resultado da tradução de {num1} para {operacoes[operacao]} é: {resultado1}")

    elif operacao == 11:
        num = int(input("digite o número que você deseja ver o log: "))
        num_final = int(input("digite qual a base do log que você deseja: "))
        print(f"o resultado do logartimo de {num} na base {num_final} :{math.log(num,num_final):.2f}")
    
    elif operacao == 12:
        num = int(input("digite o número que deseja descobrir o fatorial: "))
        print(f"o fatorial de {num} é {math.factorial(num)}")
    else:
        print("Operação inválida! Tente novamente.")
        continue
    stop = input(f"Você deseja continuar? S/N")
    stopUp = stop.upper()
    if stopUp == "S":
        continue
    else:
        break
   