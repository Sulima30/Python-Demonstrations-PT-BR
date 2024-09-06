# Programa: Aula Introdutória
# Autor: Sullivan Lima
# Versão da Aula: 1.0
# Ano: 2024
# Linguagem Python. Versão 3.x
# Descrição: Esta aula introdutória visa iniciar os conceitos da linguagem Python referentes a saídas e entradas de dados na tela do usuário.


# Um dos pontos que fazem a linguagem python ser tão usada, é o fato dela ter uma simplicidade na execuação. Entretanto, devemos respeitar as questões envolvendo a intentação. O código deve ficar com a intentação correta para poder funcionar sem eventuais bugs. 
# Esse código foi adaptado da própria aula de java do meu repositório. 

def main():
    # Exibindo uma mensagem com quebra de linha
    print("Primeiro Programa em Python")
    
    # Exibindo uma mensagem na mesma linha
    print("O famoso: Hello World!", end=" ")
    
    # Exemplo de print com caracteres especiais e quebra de linha
    print("Continuando com essa frase para demonstrar o comportamento do print sem o \"end\".")
    
    # Usando f-strings para formatar a saída
    print(f"Quando utilizamos o print podemos passar múltiplos argumentos: {'Argumento 1, '} {'Argumento 2, '} {'Outros Argumentos...'}")
    
    # Informando sobre a entrada de dados pelo usuário
    print("Agora, dando continuidade, iremos trabalhar com a inserção de dados pelo usuário.")
    
    # Solicitando dados ao usuário e armazenando na variável
    entrada_de_palavra = input("Digite uma palavra qualquer: ")
    
    # Exibindo a palavra digitada pelo usuário
    print(f"Sua palavra digitada foi: {entrada_de_palavra}")

# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    main()
