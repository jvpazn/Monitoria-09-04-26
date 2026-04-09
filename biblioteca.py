'''Problema: Gerenciamento de Livraria

Você deve criar um sistema simples para gerenciar livros em uma livraria. O programa deve permitir:

    1.Criar uma sequência que contém as categorias de livros da livraria. Esta sequência não pode ser alterada.

    2.Cada livro será representado por uma estrutura que terá os seguintes atributos: código, título, autor, ano de publicação, preço e quantidade disponível.

    3.Criar uma sequência que representará o banco de dados da livraria, onde cada livro será armazenado onde será possível, adicionar, remover e modificar cada livro.

    4.Criar uma função que recebe os dados de um livro e que o adiciona ao banco de dados.

    5.Criar uma função que receba o código de um livro e a quantidade comprada e que calcule o valor a ser pago por esse livro.

    6.Criar uma função que diminui a quantidade de um livro disponível, sempre que um ou mais exemplares dele for(em) vendido(s).
    Exemplo: digamos que o livro "A máquina do caos" tenha 5 exemplares inicialmente. Após uma pessoa comprar 2 exemplares dele, a quantidade deste livro na lista deve ser atualizada para 3.

    7.Criar uma função que simula um caixa e que fica perguntando o código do livro e a quantidade, até que o caixa encerre a compra. Ao final, deve retornar o valor devido pelo cliente e deve diminuir a quantidade de livros disponíveis que foram comprados.

    8. 
    Crie uma função que lista todos os livros cadastrados, com a seguinte estrutura:
    Código: xxxx
    Título: xxxxx
    Autor: xxx
    Preço: R$ xx,xx

    9. Crie uma função que buscar livros por autor.

    10. Crie uma função que remove um livro pelo título.'''


# 1.Criar uma sequência que contém as categorias de livros da livraria. Esta sequência não pode ser alterada.

Sequencia_livros = ("Sci-fi", "Romance")

# 2.Cada livro será representado por uma estrutura que terá os seguintes atributos: código, título, autor, ano de publicação, preço e quantidade disponível.

Biblioteca = {"Livro1":{"Codigo" : 1, "Titulo": "Androides Sonham com Ovelhas Elétricas?", "Autor": "Philip K. Dick", "Ano_publicado": 1968, "preco":15, "qntd":18}}

# 3.Criar uma sequência que representará o banco de dados da livraria, onde cada livro será armazenado onde será possível, adicionar, remover e modificar cada livro.

Biblioteca["Livro2"] = {
    "Codigo": 2, 
    "Titulo": "Duna", 
    "Autor": "Frank Herbert", 
    "Ano_publicado": 1965, 
    "preco": 45, 
    "qntd": 10
}
'''
Biblioteca["Livro1"]["preco"] = 25

del Biblioteca["Livro2"]

'''

# 4. Criar uma função que recebe os dados de um livro e que o adiciona ao banco de dados.
def adicionar_livro(codigo, titulo, autor, ano, preco, qntd):
    chave = f"Livro{codigo}"
    Biblioteca[chave] = {
        "Codigo": codigo,
        "Titulo": titulo,
        "Autor": autor,
        "Ano_publicado": ano,
        "preco": preco,
        "qntd": qntd
    }
    print(f"\n O livro '{titulo}' foi adicionado com sucesso!")

# adicionar_livro(2, "Fundação", "Isaac Asimov", 1951, 50.00, 5)

# 5. Criar uma função que receba o código de um livro e a quantidade comprada e que calcule o valor a ser pago por esse livro.
def calcular_valor(codigo, quantidade_comprada):
    for livro in Biblioteca.values():
        if livro["Codigo"] == codigo:
            return livro["preco"] * quantidade_comprada
    return 0.0 

# print(calcular_valor(1, 2))

# 6. Criar uma função que diminui a quantidade de um livro disponível, sempre que um ou mais exemplares dele for(em) vendido(s).
def diminuir_quantidade(codigo, quantidade_vendida):
    for livro in Biblioteca.values():
        if livro["Codigo"] == codigo:
            if livro["qntd"] >= quantidade_vendida:
                livro["qntd"] -= quantidade_vendida
                return True 
            else:
                print(f"\n[!] Estoque insuficiente. Temos apenas {livro['qntd']} exemplares de '{livro['Titulo']}'.")
                return False 
    
    print("\n[!] Código de livro não encontrado.")
    return False

# diminuir_quantidade(2, 20)



# 8. Crie uma função que lista todos os livros cadastrados
def listar_livros():
    print("\n--- LISTA DE LIVROS ---")
    for livro in Biblioteca.values():
        print(f"Código: {livro['Codigo']}")
        print(f"Título: {livro['Titulo']}")
        print(f"Autor: {livro['Autor']}")
        print(f"Ano Publicado: {livro['Ano_publicado']}")
        print(f"Preço: R$ {livro['preco']:.2f}")
        print("-" * 20)

# 9. Crie uma função que buscar livros por autor.
def buscar_por_autor(autor_buscado):
    encontrou = False
    
    for livro in Biblioteca.values():
        if autor_buscado.lower() in livro["Autor"].lower():
            print(f"Encontrado: '{livro['Titulo']}' (Código: {livro['Codigo']})")
            encontrou = True
            
    if not encontrou:
        print("Nenhum livro deste autor foi encontrado.")

# buscar_por_autor("Joao victor paz")

# 10. Crie uma função que remove um livro pelo título.
def remover_por_titulo(titulo_buscado):
    chave_para_remover = None
    
    for chave, livro in Biblioteca.items():
        if livro["Titulo"].lower() == titulo_buscado.lower():
            chave_para_remover = chave
            break 
            
    if chave_para_remover:
        del Biblioteca[chave_para_remover]
        print(f"\n[-] O livro '{titulo_buscado}' foi removido do banco de dados.")
    else:
        print(f"\n[!] O livro '{titulo_buscado}' não foi encontrado.")

# remover_por_titulo("Duna")

print(Biblioteca)