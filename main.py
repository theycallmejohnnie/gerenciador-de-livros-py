acervo = {}

emprestados = []

def exibir_menu():
    print("Gerenciador de livros: ")
    print("1. Adicionar livro.")
    print("2. Listar livros.")
    print("3. Remover livro.")
    print("4. Atualizar quantidade.")
    print("5. Registrar empréstimo.")
    print("6. Histórico de empréstimos.")
    print("7. Sair.")

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    quantidade = int(input("Digite a quantidade de exemplares: "))
    
    if titulo in acervo:
        acervo[titulo]['quantidade'] += quantidade
    else:
        acervo[titulo] = {'autor': autor, 'quantidade': quantidade}
    
    print(f"Livro '{titulo}' adicionado com sucesso!")

def listar_livros():
    if not acervo:
        print("Nenhum livro cadastrado.")
        return
    
    print("Livros disponíveis:")
    for titulo, info in sorted(acervo.items()):
        print(f"Título: {titulo}, Autor: {info['autor']}, Quantidade: {info['quantidade']}")

def remover_livro():
    titulo = input("Digite o título do livro a ser removido: ")
    
    if titulo in acervo:
        del acervo[titulo]
        print(f"Livro '{titulo}' removido com sucesso!")
    else:
        print(f"Erro: Livro '{titulo}' não encontrado no acervo.") 

def atualizar_quantidade():
    titulo = input("Digite o título do livro para atualizar a quantidade: ")
    
    if titulo in acervo:
        nova_quantidade = int(input("Digite a nova quantidade de exemplares: "))
        acervo[titulo]['quantidade'] = nova_quantidade
        print(f"Quantidade do livro '{titulo}' atualizada para {nova_quantidade}.")
    else:
        print(f"Erro: Livro '{titulo}' não encontrado no acervo.")

def registrar_emprestimo():
    titulo = input("Digite o título do livro a ser emprestado: ")
    quantidade_emprestada = int(input("Digite a quantidade de exemplares a serem emprestados: "))
    if titulo in acervo and acervo[titulo]['quantidade'] >= quantidade_emprestada:
        acervo[titulo]['quantidade'] -= quantidade_emprestada
        emprestados.append((titulo, quantidade_emprestada))
        print(f"Livro '{titulo}' emprestado com sucesso!")
    else:
        print(f"Erro: Livro '{titulo}' não disponível para empréstimo.")
    if acervo[titulo]['quantidade'] == 0:
        print(f"Livro '{titulo}' esgotado. Não há mais exemplares disponíveis.")
def historico_emprestimos():
    if not emprestados:
        print("Nenhum empréstimo registrado.")
        return
    
    print("Histórico de empréstimos:")
    for titulo, quantidade_emprestada in sorted(emprestados):
        print(f"Título: {titulo}, Quantidade emprestada: {quantidade_emprestada}")

def main():
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