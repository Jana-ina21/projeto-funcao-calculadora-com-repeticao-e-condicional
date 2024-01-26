def calculadora():
    while True:
        print("Operações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = int(input("Digite o número para a operação desejada: "))

        if operacao == 0:
            print("Saindo da calculadora. Até logo!")
            break

        if operacao not in [1, 2, 3, 4]:
            print("Essa opção não existe. Tente novamente.")
            continue

        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        if operacao == 1:
            resultado = num1 + num2
        elif operacao == 2:
            resultado = num1 - num2
        elif operacao == 3:
            resultado = num1 * num2
        elif operacao == 4:
            if num2 != 0:  
                resultado = num1 / num2
            else:
                print("Erro: Divisão por zero!")
                continue

        print("Resultado:", resultado)

calculadora()