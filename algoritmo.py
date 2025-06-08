
while True:
    print("Escolha a sua operação matemática")
    print("1- soma\n 2- subtração\n 3- multiplicação\n 4- divisão\n 5- sair")
    Operacao = int(input("digite sua operação escolhida: "))
    if Operacao == 5:
        break
    
    
    def tabuada(num1, num_final):
        


   
        if Operacao == 1:
            print(F"o resutado da soma entre {num1} + {num_final} ={tabuada(num1,num_final)}")
            
        elif Operacao == 2:
            print(f"o resultado da subtração entre {num1} - {num_final} = {num1 - num_final}")
        
        elif Operacao == 3:
            print(f"o resultado da multiplicação entre {num1} x {num_final} = {num1 * num_final}")
        
        elif Operacao == 4:
            print(f"O resultado da divisão entre {num1} / {num_final} = {num1/num_final}")
        
        
