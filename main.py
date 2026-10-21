# Estruturas de dados globais
acervo = {}          # Armazena os livros cadastrados. Formato: {titulo: {'autor': autor, 'quantidade': qtd}}
emprestados = []     # Histórico de empréstimos. Armazena tuplas: (titulo, quantidade_emprestada)


def exibir_menu():
    """Exibe o menu principal com as opções disponíveis para o usuário."""
    print("Gerenciador de livros: ")
    print("1. Adicionar livro.")
    print("2. Listar livros.")
    print("3. Remover livro.")
    print("4. Atualizar quantidade.")
    print("5. Registrar empréstimo.")
    print("6. Histórico de empréstimos.")
    print("7. Sair.")


def adicionar_livro():
    """
    Cadastra um novo livro ou atualiza a quantidade caso já exista no acervo.
    Solicita título, autor e a quantidade de exemplares.
    """
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    quantidade = int(input("Digite a quantidade de exemplares: "))
    
    # Se o livro já existir, incrementa o estoque com a quantidade informada
    if titulo in acervo:
        acervo[titulo]['quantidade'] += quantidade
    else:
        # Se for um título inédito, cria um novo registro no dicionário
        acervo[titulo] = {'autor': autor, 'quantidade': quantidade}
    
    print(f"Livro '{titulo}' adicionado com sucesso!")


def listar_livros():
    """
    Lista todos os livros do acervo em ordem alfabética de título.
    Exibe autor e quantidade de exemplares disponíveis de cada um.
    """
    if not acervo:
        print("Nenhum livro cadastrado.")
        return
    
    print("Livros disponíveis:")
    for titulo, info in sorted(acervo.items()):
        print(f"Título: {titulo}, Autor: {info['autor']}, Quantidade: {info['quantidade']}")


def remover_livro():
    """
    Remove um livro do catálogo a partir do título informado pelo usuário.
    Caso o título não exista, exibe uma mensagem de erro.
    """
    titulo = input("Digite o título do livro a ser removido: ")
    
    if titulo in acervo:
        del acervo[titulo]
        print(f"Livro '{titulo}' removido com sucesso!")
    else:
        print(f"Erro: Livro '{titulo}' não encontrado no acervo.") 


def atualizar_quantidade():
    """
    Permite redefinir manualmente a quantidade de exemplares de um livro já cadastrado.
    """
    titulo = input("Digite o título do livro para atualizar a quantidade: ")
    
    if titulo in acervo:
        nova_quantidade = int(input("Digite a nova quantidade de exemplares: "))
        acervo[titulo]['quantidade'] = nova_quantidade
        print(f"Quantidade do livro '{titulo}' atualizada para {nova_quantidade}.")
    else:
        print(f"Erro: Livro '{titulo}' não encontrado no acervo.")


def registrar_emprestimo():
    """
    Registra o empréstimo de cópias de um livro disponível.
    Deduz os exemplares do estoque e adiciona a transação à lista de empréstimos.
    """
    titulo = input("Digite o título do livro a ser emprestado: ")
    quantidade_emprestada = int(input("Digite a quantidade de exemplares a serem emprestados: "))
    
    if titulo in acervo and acervo[titulo]['quantidade'] >= quantidade_emprestada:
        acervo[titulo]['quantidade'] -= quantidade_emprestada
        emprestados.append((titulo, quantidade_emprestada))
        print(f"Livro '{titulo}' emprestado com sucesso!")
        
        # Alerta se o estoque do livro zerou após o empréstimo
        if acervo[titulo]['quantidade'] == 0:
            print(f"Livro '{titulo}' esgotado. Não há mais exemplares disponíveis.")
    else:
        print(f"Erro: Livro '{titulo}' não disponível para empréstimo.")


def historico_emprestimos():
    """
    Exibe a listagem de todos os empréstimos realizados em ordem alfabética de título,
    mostrando a respectiva quantidade emprestada.
    """
    if not emprestados:
        print("Nenhum empréstimo registrado.")
        return
    
    print("Histórico de empréstimos:")
    for titulo, quantidade_emprestada in sorted(emprestados):
        print(f"Título: {titulo}, Quantidade emprestada: {quantidade_emprestada}")


def main():
    """
    Função principal e ponto de entrada da aplicação.
    Executa o loop interativo, apresenta o menu e direciona para a função escolhida.
    """
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            atualizar_quantidade()
        elif opcao == '5':
            registrar_emprestimo()
        elif opcao == '6':
            historico_emprestimos()
        elif opcao == '7':
            print("Saindo do gerenciador de livros.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()