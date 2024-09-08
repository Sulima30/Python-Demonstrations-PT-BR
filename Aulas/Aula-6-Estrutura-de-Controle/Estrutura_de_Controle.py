# Programa: Aula Estrutura de Repetição usando FOR, WHILE e DO...WHILE
# Autor: Sullivan Lima
# Versão da Aula: 1.0
# Ano: 2024
# Linguagem Python. Versão 3.11
# Descrição: Esta aula visa iniciar os conceitos da linguagem Python referentes a estrutura de repetição usando FOR, WHILE, e DO...WHILE

# Em Python, usamos as estruturas de repetição para executar blocos de código várias vezes com base em condições definidas.
# Vamos explorar três estruturas principais: FOR, WHILE e DO...WHILE (ou o equivalente em Python).

# Estrutura de Repetição FOR
# O FOR é usado quando sabemos o número de repetições de antemão.
# Em Python, o FOR é usado para iterar sobre uma sequência, como uma lista ou um intervalo de números.

print("\n\nTítulo do Bloco FOR\n\n")
for numeroInteiro in range(5):
    # O range(5) gera uma sequência de números de 0 a 4.
    # O valor de "numeroInteiro" será exibido em cada iteração.
    print(f"Número Inteiro: {numeroInteiro}")

# BLOCO WHILE
# O WHILE é usado para repetir um bloco de código enquanto uma condição for verdadeira.
# A condição é verificada antes de cada iteração.
# A repetição continua até que a condição se torne falsa.

numeroInteiroWhile = 0 # Variável usada no laço WHILE

print("\n\nTítulo do Bloco WHILE\n\n")
while numeroInteiroWhile < 5:
    # Imprime o número enquanto a condição (numeroInteiroWhile < 5) for verdadeira.
    print(f"Número impresso na tela: {numeroInteiroWhile}")
    numeroInteiroWhile += 1 # Incrementa a variável em cada iteração.

# DO...WHILE
# Python não tem uma estrutura DO...WHILE nativa, mas podemos simular esse comportamento.
# No DO...WHILE, o bloco é executado pelo menos uma vez e depois repetido enquanto a condição for verdadeira.

numeroInteiroDoWhile = 0 # Variável para o laço DO...WHILE

print("\n\nTítulo do Bloco DO...WHILE\n\n")
while True:
    # Executa o bloco pelo menos uma vez.
    print(f"Número impresso na tela usando o DO...While: {numeroInteiroDoWhile}")
    numeroInteiroDoWhile += 1
    if numeroInteiroDoWhile >= 5:
        break # Sai do laço quando a condição (numeroInteiroDoWhile >= 5) for atendida.

# FOR com BREAK e CONTINUE
# Podemos usar "break" para sair de um laço antes de ele terminar e "continue" para pular para a próxima iteração.

print("\n\nTítulo do Bloco FOR COM INTERRUPÇÃO\n\n")

for inteiroForComandosBreakEContinue in range(10):
    if inteiroForComandosBreakEContinue == 5:
        break # Interrompe o laço quando o número for 5.
    
    if inteiroForComandosBreakEContinue % 2 == 0:
        continue # Pula para a próxima iteração se o número for par.
    
    # Imprime apenas números ímpares, pois os pares são ignorados pelo "continue".
    print(f"Número ímpar: {inteiroForComandosBreakEContinue}")

# FOR Aninhado
# Usado para estruturas bidimensionais, como matrizes.
# O laço interno é executado completamente para cada iteração do laço externo.

print("\n\nTítulo do Bloco FOR Aninhado\n\n")
for inteiroAninhado1 in range(3):
    for inteiroAninhado2 in range(3):
        # Imprime todos os pares possíveis de inteiros dentro das faixas definidas.
        print(f"Inteiro Aninhado 1: {inteiroAninhado1}, Inteiro Aninhado 2: {inteiroAninhado2}")
