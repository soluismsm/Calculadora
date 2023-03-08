from os import system

operadores = ["Soma", "Subtração", "Multiplicação", "Divisão"]


def start_screen():
    print("Bem-vindo à Calculadora")
    for i, operador in enumerate(operadores):
        print(f"{i+1}) {operador}")
    while True:
        try:
            operador = int(input("Qual operação deseja realizar (1-4)? "))
            if 1 <= operador <= 4:
                return operador
            continue
        except ValueError:
            print("ERRO. Digite um número válido (1-4)\n")
            continue


def get_num1():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            return num1
        except ValueError:
            print("ERRO. Digite um número válido")


def get_num2():
    while True:
        try:
            num2 = float(input("Digite o segundo número: "))
            return num2
        except ValueError:
            print("ERRO. Digite um número válido")


def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    return num1 / num2


def escolha():
    while True:
        escolha = input("Deseja realizar outra operação? (s/n) ")
        if "S" in escolha[0].upper():
            return True
        elif "N" in escolha[0].upper():
            return False
        else:
            print("Digite uma resposta válida (s/n).")


def main():
    while True:
        operador = start_screen()
        system("cls")
        print(f"-=-=-=-{operadores[operador - 1]}-=-=-=-")
        num1 = get_num1()
        num2 = get_num2()
        resultado = None

        # Soma
        if operador == 1:
            resultado = somar(num1, num2)
        # Subtração
        if operador == 2:
            resultado = subtrair(num1, num2)

        # Multiplicação
        if operador == 3:
            resultado = multiplicar(num1, num2)

        # Divisão
        if operador == 4:
            if num2 == 0:
                print("Não é possível dividir por zero.")
                continue
            resultado = dividir(num1, num2)

        if resultado is not None:
            print(
                f"\nA {operadores[operador-1]} de {num1:.0f} e {num2:.0f}"
                f"é {resultado:.0f}"
            )

        continuar = escolha()
        if continuar:
            system("cls")
        else:
            print("Volte sempre!")
            break


main()
