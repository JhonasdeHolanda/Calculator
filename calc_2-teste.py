import math

tipo_Calc =int(input("digite o tipo de operação que você deseja: "))
valor_calc = int(input("digite o número que você deseja ver a tabuada: "))
valor_final = int(input("até qual número você deseja que seja operado?: "))


def operacao_basica():
    for i in range (1,valor_final + 1):
        if tipo_Calc == 1: 
             print(f"{valor_calc} + {i} = {valor_calc + i}")
        else:
            print("aa")






aa = operacao_basica()
print (aa)
            