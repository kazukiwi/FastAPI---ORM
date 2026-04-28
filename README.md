
# 📦 Nexus | Gestão de Produtos

O **Nexus** é uma aplicação moderna de gerenciamento de inventário projetada para oferecer uma experiência de usuário fluida e visualmente atraente. O sistema utiliza uma interface baseada em *Glassmorphism* para o cadastro e monitoramento de produtos em tempo real.

![Preview do Projeto](https://img.shields.io/badge/UI-Modern-6366f1) ![FastAPI](https://img.shields.io/badge/Backend-FastAPI-05998b) ![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)

---

## 🚀 Funcionalidades

* **Dashboard Intuitivo:** Visualização rápida dos itens em estoque.
* **Gestão de Produtos:** Cadastro completo incluindo Nome, Marca e Categoria.
* **Categorização Dinâmica:** Integração com banco de dados para listagem de categorias existentes.
* **Interface Responsiva:** Design adaptável para diferentes tamanhos de tela.
* **Confirmação de Ações:** Proteção contra exclusões acidentais via diálogos nativos.

---

## 🛠️ Tecnologias Utilizadas

### **Frontend**
* **HTML5 & CSS3:** Estrutura e estilização customizada com variáveis CSS.
* **Google Fonts:** Tipografia *Plus Jakarta Sans*.
* **Font Awesome:** Ícones vetoriais.
* **Jinja2:** Engine de templates para renderização dinâmica de dados.

### **Backend**
* **Python:** Linguagem base.
* **FastAPI:** Framework web de alta performance.
* **SQLAlchemy:** ORM para manipulação robusta do banco de dados.
* **SQLite/PostgreSQL:** Suporte a múltiplos bancos de dados.

---

## 🔧 Configuração e Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/nexus-gestao.git
    cd nexus-gestao
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install fastapi uvicorn sqlalchemy jinja2
    ```

4.  **Inicie a aplicação:**
    ```bash
    uvicorn main:app --reload
    ```
    Acesse em: `http://localhost:8000`

---

## 📂 Estrutura de Rotas (API)

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| **GET** | `/` | Lista produtos e exibe formulário |
| **POST** | `/produtos/salvar` | Salva um novo produto no banco |
| **POST** | `/produtos/deletar/{id}` | Remove um produto por ID |
| **GET** | `/categorias` | Gerenciamento de categorias |

---

## 🎨 Preview da Interface

> **Destaque do Design:** O projeto utiliza um fundo com gradiente linear e cartões com efeito de vidro (`backdrop-filter: blur`), seguindo as tendências de UI de 2024/2025.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### **Contribuição**
Sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request* para melhorias no sistema de filtros ou relatórios em PDF. 🚀
