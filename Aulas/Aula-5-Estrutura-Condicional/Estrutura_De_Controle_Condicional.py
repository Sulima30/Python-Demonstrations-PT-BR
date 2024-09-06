# Programa: Aula Estrutura de Controle Condicional: Se / Se...Então / Casos Certos (Switch)
# Autor: Sullivan Lima
# Versão da Aula: 1.0
# Ano: 2024
# Linguagem Python. Versão 3.x
# Descrição: Esta aula visa iniciar os conceitos da linguagem Python referentes a estrutura de controle condicionais envolvendo os casos do Se / Se Então 

# Como sempre mencionamos, aqui temos a função principal da aplicação

# Deixarei aqui uma nota breve sobre as estruturas de controle.
# As estruturas de controle são essenciais para desenvolver softwares e controlar suas execuções.
# Permitem tomar decisões, realizar outras operações e fazer inúmeras coisas legais
# Iniciaremos aqui as estruturas condicionais de controle que não envolvem repetição. Uma coisa por vez...

def main():
    # Nossa primeira estrutura condicional é o SE ou em inglês da linguagem IF
    # Note que apenas a estrutura IF é bem simples, porém, muito útil e veremos nos projetos posteriores!
    # Dentro dos parenteses da estrutura IF colocamos a condicional (que podemos utilizar as operações relacionais ou lógicas

    # Primeira nota do aluno
    nota1 = int(input("Digite a primeira nota do aluno: "))

    # Início da estrutura condicional SE
    if nota1 >= 7:
        # Condição verdadeira
        print(f"\nA nota do aluno é: {nota1}")
        # Se você digitar um valor abaixo de 7, o comando não será executado.
    # Fim da estrutura condicional SE

    # Condicional IF...ELSE
    if nota1 >= 7:
        print(f"\n\nVocê digitou {nota1} que é uma nota maior ou igual a 7. O aluno está aprovado.")
    else:
        print(f"\nVocê digitou {nota1} que é uma nota menor que 7. O aluno está reprovado.")
    # Fim do bloco IF...ELSE

    # Condicional IF...ELSE IF...ELSE
    if 4 <= nota1 < 7:
        print(f"\n\nVocê digitou {nota1}, que é uma nota entre 4 e 7. O aluno está em recuperação.")
    elif nota1 >= 7:
        print(f"\nVocê digitou {nota1}, que é uma nota maior ou igual a 7. O aluno está aprovado.")
    else:
        print(f"\nVocê digitou {nota1}, que é menor que 4. O aluno está reprovado.")
    # Fim do bloco IF...ELSE IF...ELSE

    # Não existe Switch em Python, mas podemos usar um dicionário para ilustrar algo similar.
    # Utilizando um dicionário para simular o Switch
    casos = {
        0: "Você digitou 0.",
        1: "Você digitou 1.",
        2: "Você digitou 2.",
        3: "Você digitou 3.",
        4: "Você digitou 4.",
        5: "Você digitou 5.",
        6: "Você digitou 6.",
        7: "Você digitou 7.",
        8: "Você digitou 8.",
        9: "Você digitou 9.",
        10: "Você digitou 10."
    }

    print(casos.get(nota1, "Digitou nenhum dos valores entre 0 até 10."))

if __name__ == "__main__":
    main()
