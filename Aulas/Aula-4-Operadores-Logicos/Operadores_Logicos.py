# Programa: Aula Operadores Lógicos
# Autor: Sullivan Lima
# Versão da Aula: 1.0
# Ano: 2024
# Linguagem Python. Versão 3.x
# Descrição: Esta aula de operadores lógicos visa explicar como usar operadores lógicos para combinar expressões booleanas. O programa permite a entrada de valores booleanos pelo usuário e exibe os resultados das operações lógicas.

def main():
    # Interação com o usuário para informar os dois valores a serem analisados
    primeiro_valor = input("Digite o primeiro valor booleano (true/false) para ser analisado: ").strip().lower() == 'true'
    segundo_valor = input("Digite o segundo valor booleano (true/false) para ser analisado: ").strip().lower() == 'true'
    
    # Análise utilizando o operador lógico E (and)
    e_logico = (primeiro_valor and segundo_valor)
    print(f"\nO resultado de {primeiro_valor} E (and) {segundo_valor} é: {e_logico}")
    # Nota: O operador E lógico (and) retorna verdadeiro apenas se ambos os valores forem verdadeiros. Caso contrário, retorna falso.
    
    # Análise utilizando o operador lógico OU (or)
    ou_logico = (primeiro_valor or segundo_valor)
    print(f"\nO resultado de {primeiro_valor} OU (or) {segundo_valor} é: {ou_logico}")
    # Nota: O operador OU lógico (or) retorna verdadeiro se pelo menos um dos valores for verdadeiro. Retorna falso apenas se ambos forem falsos.
    
    # Análise utilizando o operador lógico de negação not
    negacao_logica_primeiro_valor = not primeiro_valor
    negacao_logica_segundo_valor = not segundo_valor
    print(f"\nO resultado da negação lógica de {primeiro_valor} (not {primeiro_valor}) é: {negacao_logica_primeiro_valor}")
    print(f"O resultado da negação lógica de {segundo_valor} (not {segundo_valor}) é: {negacao_logica_segundo_valor}")
    # Nota: A negação lógica (not) inverte o valor booleano. Se o valor for verdadeiro, a negação será falsa e vice-versa.
    
    # Análise utilizando o operador lógico OU Exclusivo (xor)
    operador_ou_exclusivo_logico = (primeiro_valor != segundo_valor)
    print(f"\nO resultado do OU Exclusivo (xor) entre {primeiro_valor} e {segundo_valor} é: {operador_ou_exclusivo_logico}")
    # Nota: O operador OU Exclusivo (xor) retorna verdadeiro se exatamente um dos valores for verdadeiro. Se ambos forem iguais, o resultado é falso.

if __name__ == "__main__":
    main()
