print(" 1 - soma"
" 2 - subtração"
" 3 - multiplicação"
" 4 - divisão")
tipo_Calc =int(input("digite o tipo de operação que você deseja: "))
valor_calc = int(input("digite o número que você deseja ver a tabuada: "))
valor_final = int(input("até qual número você deseja que seja operado?: "))
for i in range (valor_final + 1):
    if tipo_Calc == 1: 
        print (f"{valor_calc} + {i} = {valor_calc + i}")
        print("______________________________")
    elif tipo_Calc == 2:
        print (f"{valor_calc} - {i} = {valor_calc - i}")
        print("______________________________")
    elif  tipo_Calc == 3:
        print (f"{valor_calc} x {i} = {valor_calc * i}")
    else:
        tipo_Calc == 4
        print (f"{valor_calc} / {i} = {valor_calc // i}") 
