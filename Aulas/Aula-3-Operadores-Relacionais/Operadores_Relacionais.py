# Programa: Aula Operadores Relacionais
# Autor: Sullivan Lima
# Versão da Aula: 1.0
# Ano: 2024
# Linguagem Python. Versão 3.x
# Descrição: Esta aula de operadores relacionais visa explicar como usar operadores de comparação entre variáveis numéricas. O programa permite a entrada de valores pelo usuário e exibe os resultados das comparações.

def main():
    # Cria um Scanner para leitura dos dados do usuário (não necessário em Python)
    
    # Interação com o usuário para inserir dois números e realizar a comparação com operadores relacionais
    primeiro_numero = int(input("Digite o primeiro número a ser comparado: "))
    segundo_numero = int(input("Digite o segundo número a ser comparado: "))

    # Nosso primeiro operador relacional será o de igualdade. Vamos comparar os números e armazenar o resultado na variável chamada igual do tipo booleano.
    igual = (primeiro_numero == segundo_numero)
    # A resposta será True quando for igual e False quando for diferente.
    print(f"\nO Primeiro Número: {primeiro_numero} é igual ao Segundo Número: {segundo_numero}? {igual}")

    # Nosso segundo operador relacional será o de diferente. Vamos comparar os números e armazenar o resultado na variável chamada diferente também do tipo booleano.
    diferente = (primeiro_numero != segundo_numero)
    # A resposta será True quando for diferente e False quando for igual.
    print(f"\nO Primeiro Número: {primeiro_numero} é diferente do Segundo Número: {segundo_numero}? {diferente}")

    # Nosso terceiro operador relacional será o de maior que. Vamos comparar os números e armazenar o resultado na variável chamada primeiro_numero_maior_que_segundo_numero também do tipo booleano.
    primeiro_numero_maior_que_segundo_numero = (primeiro_numero > segundo_numero)
    # A resposta será True quando o primeiro número for maior e False quando for menor ou igual.
    print(f"\nO Primeiro Número: {primeiro_numero} é maior que o Segundo Número: {segundo_numero}? {primeiro_numero_maior_que_segundo_numero}")

    # Nosso quarto operador relacional será o de menor que. Vamos comparar os números e armazenar o resultado na variável chamada primeiro_numero_menor_que_segundo_numero também do tipo booleano.
    primeiro_numero_menor_que_segundo_numero = (primeiro_numero < segundo_numero)
    # A resposta será True quando o primeiro número for menor e False quando for maior ou igual.
    print(f"\nO Primeiro Número: {primeiro_numero} é menor que o Segundo Número: {segundo_numero}? {primeiro_numero_menor_que_segundo_numero}")

    # Nosso quinto operador relacional será o de maior ou igual. Vamos comparar os números e armazenar o resultado na variável chamada primeiro_numero_maior_igual_segundo_numero também do tipo booleano.
    primeiro_numero_maior_igual_segundo_numero = (primeiro_numero >= segundo_numero)
    # A resposta será True quando o primeiro número for maior ou igual e False quando for menor.
    print(f"\nO Primeiro Número: {primeiro_numero} é maior ou igual que o Segundo Número: {segundo_numero}? {primeiro_numero_maior_igual_segundo_numero}")

    # Nosso sexto operador relacional será o de menor ou igual. Vamos comparar os números e armazenar o resultado na variável chamada primeiro_numero_menor_igual_segundo_numero também do tipo booleano.
    primeiro_numero_menor_igual_segundo_numero = (primeiro_numero <= segundo_numero)
    # A resposta será True quando o primeiro número for menor ou igual e False quando for maior.
    print(f"\nO Primeiro Número: {primeiro_numero} é menor ou igual que o Segundo Número: {segundo_numero}? {primeiro_numero_menor_igual_segundo_numero}")

if __name__ == "__main__":
    main()
