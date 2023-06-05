data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = map(int, data.split("/"))

if ano < 1900 or ano > 2100 or mes < 1 or mes > 12:
    print("A data informada não é válida")
elif dia < 1 or dia > 31:
    print("A data informada não é válida")
else:
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia > 29:
                print("A data informada não é válida")
            else:
                print("A data informada é válida")
        elif dia > 28:
            print("A data informada não é válida")
        else:
            print("A data informada é válida")
    elif mes in [4, 6, 9, 11]:
        if dia > 30:
            print("A data informada não é válida")
        else:
            print("A data informada é válida")
    else:
        print("A data informada é válida")
