#Criar um programa para adicionar, remover, listar e atualizar os produtos. MENU Interativo FEITO
    #Converter tudo em uma string estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00" FEITO
#Criar um função MAIN que roda todas as funções FEITO
# Criar uma função de Cadastro de produto FEITO
#Criar uma função de inserção inicial do estoque FEITO
#Criar uma função para remover o produto FEITO
#Criar uma função de listagem de produtos dentro de uma lista incluindo a descrição, codigo(ID), quantidade, custo, preço de venda de cada item. FEITO
#Criar uma função para buscar o produto por palavra chave FEITO
#Criar uma função que exiba todos os produtos com a quantidade FEITO
#Criar uma função que permite filtrar os produtos com quantidade abaixo de um limite minimo estabelecido pelo usuário ou uma quantidade padrão, caso o usuário não forneça, gere um relátorio com esses produtos FEITO
#Criar uma função para atualizar a quantidade de um produto especifico no estoque. Adicionando a entrada(aumento) ou a saida(diminuição) da quantidade de produtos FEITO
#Criar uma função para atualizar os preços da venda de um produto especifico FEITO
#Criar uma função que valida as alterações de quantidade, preço, ou altere as funções de atualização para garantir que o estoque não fique negativo após uma atualização e que o novo preço de venda não seja menor que o custo do item FEITO
#Criar uma função que calcule o valor total do estoque , mutiplicando a quantidade de cada produto pelo seu preço de venda (quantidade * preço) FEITO
#Criar uma função que calcule o lucro presumido do estoque, considerando a diferença entre o preço da venda e o custo de cada item multiplicado pela quantidade disponivel(preço, custo do ID * quantidade), exiba o lucro total no terminal.   FEITO
#Criar uma função que permite ao usuário ordenar os produtos pela quantidade disponivel no estoque, exibindo a lista em ordem crescente ou descrescente. FEITO
#Criar uma função de busca de produto no estoque com base na descrição ou ID do produto, recebendo parâmetros por palavra-chave. Caso não seja encontrado exibir uma mensagem de erro. E caso mais de 1 produto seja encontrado as informações de todos devem ser exibidas. FEITO
#Documentar todo o codigo, cada função e o que foi feito. FEITO
#Criar uma função que exiba um relatório geral no terminal, incluindo a descrição, codigo(ID), quantidade, custo, preço de venda, e o valor total por item(quantidade * preço). O relatório deve usar os metodos ljust(), rjust(), format() ou metódos semelhantes para formatar a saída de forma organizada. Ao final do relátorio, exiba o custo total e o faturamento total do estoque. FEITO

estoque = []

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

contador_id = 213

def carregar_estoque_inicial(estoque_string):
    """
    Carrega o estoque inicial a partir de uma string formatada.
    
    Args:
        estoque_string (str): String contendo os produtos, separados por '#' e atributos separados por ';'.
    
    Returns:
        None
    """
    produtos = estoque_string.split("#")

    for produto_string in produtos:
        detalhes = produto_string.split(";")
        produto = {
            'nome' : detalhes[0],
            'id' : int(detalhes[1]),
            'quantidade' : float(detalhes[2]),
            'preco_compra' : float(detalhes[3]),
            'preco_venda' : float(detalhes[4])
        }

        estoque.append(produto)


def listar_produtos():
    """ Exibe todos os produtos disponíveis no estoque, mostrando detalhes como nome, ID, quantidade, preço de compra e venda. """
    if not estoque:
        print("Estoque Vázio.\n") 
    else:
        for produto in estoque:
            print(f"ID: {produto['id']}, nome: {produto['nome']}, quantidade: {produto['quantidade']}, Preço de Compra: {produto['preco_compra']}, Preço de Venda: {produto['preco_venda']}")
        print()


def adicionar_produto():
    """ Permite ao usuário adicionar um novo produto ao estoque com um ID automático, baseado no contador global. """
    global contador_id
    nome = input("Digite o nome do produto: ")
    quantidade = float(input("Digite a quantidade do produto: "))
    preco_compra = float(input("Digite o preço de compra do produto: "))
    preco_venda = float(input("Digite o preço de venda do produto: "))
    
    produto = {
        'id' : contador_id,
        'nome' : nome,
        'quantidade' : quantidade,
        'preco_compra' : preco_compra,
        'preco_venda' : preco_venda
    }
    
    estoque.append(produto)
    print(f"Produto {nome} adicionado ao estoque com o ID {contador_id}. \n")
    
    contador_id +=1


def remover_produto():
    """ Remove um produto específico do estoque com base no ID fornecido pelo usuário. """
    
    if not estoque:
        print("Estoque Vazio. Não há produtos para remover. \n")
        return

    listar_produtos()
    id_produto = int(input("Digite o ID do produto que deseja remover: "))
    
    for produto in estoque:
        if produto['id'] == id_produto:
            estoque.remove(produto)
            print(f"Produto '{produto['nome']}' removido com sucesso. \n")
            return
    
    print("Produto não encontrado. Tente novamente com um ID válido.\n")


def atualizar_produtos():
    """Atualiza as informações de um produto, como nome, quantidade, preço de compra e venda. 
    O usuário pode optar por manter os valores atuais deixando os campos em branco. """
    
    if not estoque:
        print("Estoque vazio. Não há produtos para atualizar. \n")
        return

    listar_produtos()
    id_produto = int(input("Digite o ID do produto para atualizar: "))
    
    for produto in estoque:
        if produto['id'] == id_produto:
            print(f"Atualizando o produto: {produto['nome']}")

            novo_nome = input(f"Novo nome (Deixe em branco para manter '{produto['nome']}'): ")
            if novo_nome:
                produto['nome'] = novo_nome
            
            nova_quantidade = input(f"Nova quantidade (Deixe em branco para manter '{produto['quantidade']}'): ")
            if nova_quantidade:
                produto['quantidade'] = int(nova_quantidade)
            
            novo_preco_compra = input(f"Novo preço de compra (Deixe em branco para manter '{produto['preco_compra']}'): ")
            if novo_preco_compra:
                produto['preco_compra'] = float(novo_preco_compra)
            
            novo_preco_venda = input(f"Novo preço de venda (Deixe em branco para manter '{produto['preco_venda']}'): ")
            if novo_preco_venda:
                produto['preco_venda'] = float(novo_preco_venda)
            
            print(f"Produto {produto['id']} atualizado com sucesso!\n")
            return
            
    print("Produto não encontrado. Tente novamente com um ID válido.\n")


def buscar_produto():
    """ Busca produtos no estoque que contenham uma palavra-chave fornecida pelo usuário no nome. """
    
    if not estoque:
        print("Estoque vazio. Não há produtos para buscar. \n")
        return
    
    palavra_chave = input("Digite a palavra chave para buscar: ").lower()
    
    produtos_encontrados = [produto for produto in estoque if palavra_chave in produto['nome']]
    
    if produtos_encontrados:
        print(f"Produtos encontrados contendo: {palavra_chave}: \n")
        for produto in produtos_encontrados:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço de Compra: {produto['preco_venda']}, Preço de Venda: {produto['preco_venda']}")
    else:
        print(f"Nenhum produto encontrado com a palavra chave: {palavra_chave}. \n")


def ordenar_quantidade():
    """ Ordena os produtos com base na quantidade disponível no estoque. O usuário pode optar por ordem crescente ou decrescente. """
    if not estoque:
        print("Estoque vazio. Não há produtos para ordenar.")
        return
    
    ordem = input("Deseja ordenar por quantidade Crescente (c) ou Descrescente (d): ").lower()
    
    if ordem == 'c':
        produtos_ordenados = sorted(estoque, key=lambda produto: produto['quantidade'])
    elif ordem == 'd':
        produtos_ordenados = sorted(estoque, key=lambda produto: produto['quantidade'], reverse=True)
    else:
        print("Ordem inválida. Tente novamente \n")
        return
    
    print(f"\nProdutos ordenados por quantidade ({'crescente' if ordem == 'c' else 'decrescente'}):\n")
    
    if produtos_ordenados:
        for produto in produtos_ordenados:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço de Compra: {produto['preco_compra']}, Preço de Venda: {produto['preco_venda']}")
            print()
    else:
        print("Não há produtos no estoque.\n")


def filtrar_produtos_por_quantidade():
    """ Filtra produtos com quantidade abaixo de um limite estabelecido pelo usuário ou de 10 unidades, se o usuário não fornecer um limite. """
    if not estoque:
        print("Estoque vazio. Não há produtos para filtrar. \n")
        return

    limite_str = input("Digite o limite mínimo de quantidade (ou pressione Enter para usar o padrão de 10): ")
    limite_minimo = int(limite_str) if limite_str else 10

    produtos_filtrados = [produto for produto in estoque if produto['quantidade'] < limite_minimo]

    if produtos_filtrados:
        print(f"\nProdutos com quantidade abaixo de {limite_minimo}:\n")
        for produto in produtos_filtrados:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço de Compra: {produto['preco_compra']}, Preço de Venda: {produto['preco_venda']}")
            print()
    else:
        print(f"Todos os produtos têm quantidade igual ou superior a {limite_minimo}.\n")


def atualizar_quantidade_produto():
    """ Atualiza a quantidade de um produto específico, permitindo ao usuário adicionar ou remover quantidades do estoque."""
    
    if not estoque:
        print("Estoque vazio. Não há produtos para atualizar. \n")
        return

    listar_produtos()
    id_produto = int(input("Digite o ID do produto para atualizar a quantidade: "))
    
    for produto in estoque:
        if produto['id'] == id_produto:
            print(f"Atualizando a quantidade do produto: {produto['nome']}")
            
            nova_quantidade = float(input("Digite a nova quantidade (positiva para adicionar, negativa para remover): "))
            produto['quantidade'] += nova_quantidade
            
            print(f"A quantidade do produto {produto['nome']} foi atualizada para {produto['quantidade']}.\n")
            return

    print("Produto não encontrado. Tente novamente com um ID válido.\n")


def calcular_valor_total_estoque():
    """ Calcula e exibe o valor total do estoque com base nas quantidades e preços de venda dos produtos. """
    
    valor_total = sum(produto['quantidade'] * produto['preco_venda'] for produto in estoque)

    print(f"\nO valor total do estoque é: R$ {valor_total:.2f}\n")


def calcular_lucro_presumido():
    """ Calcula o lucro presumido do estoque com base na diferença entre o preço de venda e o preço de compra dos produtos."""
    
    lucro_presumido = sum(produto['quantidade'] * (produto['preco_venda'] - produto['preco_compra']) for produto in estoque)

    print(f"O lucro presumido do estoque é: R$ {lucro_presumido:.2f}\n")

def gerar_relatorio():
    """
    Gera e exibe um relatório completo do estoque, incluindo informações de todos os produtos, 
    o valor total do estoque e o lucro presumido.
    
    O relatório contém:
    - ID
    - Nome do produto
    - Quantidade disponível
    - Preço de compra
    - Preço de venda
    - Valor total do estoque (baseado no preço de venda)
    - Lucro presumido (diferença entre preço de venda e preço de compra)
    
    Returns:
        None
    """
    if not estoque:
        print("Estoque vazio. Não há produtos para gerar um relatório.\n")
        return
    
    print("\n-------- Relatório de Estoque --------")
    for produto in estoque:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço de Compra: {produto['preco_compra']}, Preço de Venda: {produto['preco_venda']}")
    
    valor_total = sum(produto['quantidade'] * produto['preco_venda'] for produto in estoque)
    lucro_presumido = sum(produto['quantidade'] * (produto['preco_venda'] - produto['preco_compra']) for produto in estoque)
    
    print(f"\nValor total do estoque: R$ {valor_total:.2f}")
    print(f"Lucro presumido: R$ {lucro_presumido:.2f}\n")
    print("--------------------------------------\n")

def main():
    """ Exibe o menu principal do sistema de controle de estoque, permitindo ao usuário selecionar as funcionalidades. """
    carregar_estoque_inicial(estoque_inicial)
    while True:
        print(" MENU ")
        print("1 - Listar Produtos")
        print("2 - Adicionar Produto")
        print("3 - Remover Produto")
        print("4 - Atualizar Produto")
        print("5 - Buscar Produto")
        print("6 - Ordenar Produtos por Quantidade")
        print("7 - Filtrar Produtos por Quantidade")
        print("8 - Atualizar Quantidade de Produto")
        print("9 - Calcular Valor Total do Estoque")
        print("10 - Calcular Lucro Presumido")
        print("11 - Gerar Relatório de Estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_produtos()
            
        elif opcao == "2":
            adicionar_produto()
            
        elif opcao == "3":
            remover_produto()
            
        elif opcao == "4":
            atualizar_produtos()
            
        elif opcao == "5":
            buscar_produto()
            
        elif opcao == "6":
            ordenar_quantidade()
            
        elif opcao == "7":
            filtrar_produtos_por_quantidade()
            
        elif opcao == "8":
            atualizar_quantidade_produto()
            
        elif opcao == "9":
            calcular_valor_total_estoque()
            
        elif opcao == "10":
            calcular_lucro_presumido()
            
        elif opcao == "11":
            gerar_relatorio()
            
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    main()