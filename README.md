<h1 align="center">📚 Gerenciador de Livros</h1>

<p align="center">
  <em>Um sistema simples e interativo via linha de comando (CLI) para gerenciamento de acervo e empréstimo de livros em Python.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" alt="Status" />
  <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-green" alt="Licença" />
</p>

---

## 📖 Sobre o Projeto

O **Gerenciador de Livros** é uma aplicação prática desenvolvida em Python para gerenciar o catálogo de uma biblioteca ou coleção pessoal. O sistema opera no terminal e permite cadastrar novos títulos, atualizar estoques, realizar e consultar empréstimos, além de listar os livros ordenados alfabeticamente.

Projeto desenvolvido com foco no aprendizado de estruturas de dados fundamentais (dicionários, listas e tuplas) e fluxo de controle em Python.

---

## ✨ Funcionalidades

- [x] **Adicionar livro:** Cadastra título, autor e quantidade de exemplares (acumulando cópias se o livro já existir).
- [x] **Listar livros em ordem alfabética:** Exibe todo o acervo ordenado de A a Z com autor e quantidade disponível.
- [x] **Remover livro:** Exclui um título do catálogo.
- [x] **Atualizar quantidade:** Permite ajustar manualmente o estoque de exemplares.
- [x] **Registrar empréstimo:** Permite emprestar uma ou mais cópias de um livro disponível, decrementando o estoque e avisando caso o título se esgote.
- [x] **Histórico de empréstimos:** Lista todos os empréstimos registrados com suas respectivas quantidades, em ordem alfabética.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** (versão 3.10+)
- **[Poetry](https://python-poetry.org/)** (gerenciamento de dependências e ambiente)

---

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina.

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/theycallmejohnnie/gerenciador-de-livros-py.git
   cd gerenciador-de-livros-py
   ```

2. *(Opcional)* **Configure o ambiente virtual:**
   ```bash
   # Usando venv
   python -m venv .venv
   source .venv/bin/activate  # No Linux/macOS
   # .venv\Scripts\activate   # No Windows
   ```
   *Ou utilizando o Poetry:*
   ```bash
   poetry install
   poetry shell
   ```

3. **Execute a aplicação:**
   ```bash
   python main.py
   ```

---

## 🖥️ Demonstração de Uso

Ao iniciar o programa, o menu interativo será exibido no terminal:

```text
Gerenciador de livros: 
1. Adicionar livro.
2. Listar livros.
3. Remover livro.
4. Atualizar quantidade.
5. Registrar empréstimo.
6. Histórico de empréstimos.
7. Sair.
Escolha uma opção: 
```

---

## 📁 Estrutura do Projeto

```text
gerenciador-de-livros/
├── main.py           # Código-fonte principal com o menu e as regras de negócio
├── pyproject.toml    # Configuração do projeto e dependências com Poetry
└── README.md         # Documentação do projeto
```

---

## 💡 Próximos Passos (Melhorias Futuras)

- [ ] Persistência de dados em arquivos (`JSON` ou `SQLite`).
- [ ] Refatoração para Programação Orientada a Objetos (POO).
- [ ] Tratamento avançado de exceções para entradas do usuário.
- [ ] Registro de data e devolução de empréstimos.

---

## 👤 Autor

Desenvolvido por **Jhonatan**.

- Email: [jhonatansousa354@gmail.com](mailto:jhonatansousa354@gmail.com)
- GitHub: [@theycallmejohnnie](https://github.com/theycallmejohnnie)
