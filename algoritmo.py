def tabuada(num1, num_final, operacao):
    if operacao == 1:
        return num1 + num_final
    elif operacao == 2:
        return num1 - num_final
    elif operacao == 3:
        return num1 * num_final
    elif operacao == 4:
        return num1 / num_final

while True:
    print("Escolha a sua operação matemática")
    print("1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- sair")
    operacao = int(input("Digite sua operação escolhida: "))
    
    if operacao == 5:
        break
    elif operacao not in [1, 2, 3, 4]:
        print("Operação inválida! Tente novamente.")
        continue
    
    num1 = float(input("Digite o primeiro número: "))
    num_final = float(input("Digite o segundo número: "))
    
    resultado = tabuada(num1, num_final, operacao)
    
    operacoes = ["soma", "subtração", "multiplicação", "divisão"]
    print(f"O resultado da {operacoes[operacao-1]} entre {num1} e {num_final} = {resultado}")