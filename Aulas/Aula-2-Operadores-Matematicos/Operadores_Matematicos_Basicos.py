# Programa: Aula Operadores Aritméticos
# Autor: Sullivan Lima
# Versão da Aula: 1.0
# Ano: 2024
# Linguagem Python. Versão 3.x
# Descrição: Esta aula de operadores visa iniciar os conceitos da linguagem Python referentes a saídas e entradas de dados na tela do usuário envolvendo operações matemáticas.

def main():
    # Título de boas-vindas
    print("Olá, vamos à segunda aula sobre Python!")

    # Solicita ao usuário para inserir números inteiros
    print("Você deverá digitar apenas números inteiros!\n")

    # Entrada de dados do usuário
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    # Realizando operações aritméticas. 
    # Aqui temos as variáveis que farão as operações com base no que o usuário digitar.

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 // numero2  # Divisão inteira (ignora parte decimal, caso esteja com apenas uma barra / poderá dar erro)
    modulo = numero1 % numero2

    # Exibindo resultados
    print(f"\nA soma entre os números digitados é: {soma}")
    print(f"A subtração entre os números digitados é: {subtracao}")
    print(f"A multiplicação entre os números digitados é: {multiplicacao}")
    print(f"A divisão entre os números digitados é: {divisao}")
    print(f"A divisão modular entre os números digitados é: {modulo}")

if __name__ == "__main__":
    main()
