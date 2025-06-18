# 🚀 MCPs-IA

Bem-vindo ao **MCPs-IA**!  
Um projeto focado em aplicações de Inteligência Artificial com Python, pronto para acelerar seu desenvolvimento com uma estrutura moderna e eficiente.

---

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![uv](https://img.shields.io/badge/Powered%20by-uv-9cf?logo=python)

</div>

---

## ✨ Comece em minutos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/LoboProgrammingg/MCPs-IA.git
   cd MCPs-IA
   ```

2. **Inicie seu ambiente com o [uv](https://github.com/astral-sh/uv):**
   ```bash
   uv init
   uv add fastmcp genai google-genai google-generativeai python-dotenv wikipedia
   ```

3. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto com suas configurações.

---

## 📂 Estrutura do Projeto

```
├── client.py
├── servidor.py
├── .env
├── .gitignore
├── pyproject.toml
├── .python-version
├── README.md
├── uv.lock
└── .venv/
```

- **client.py**: Script principal do cliente.
- **servidor.py**: Script principal do servidor.
- **.env**: Variáveis de ambiente.
- **pyproject.toml**: Gerenciamento das dependências.
- **uv.lock**: Lockfile do uv.
- **.venv/**: Ambiente virtual (não versionado).

---

## ⚡ Requisitos

- Python **3.11+**
- [uv](https://github.com/astral-sh/uv) instalado  
  <sub>Instale com: <code>pip install uv</code></sub>

---

## 🛠️ Principais Scripts

- Inicie o **cliente**:
  ```bash
  python client.py
  ```
- Inicie o **servidor**:
  ```bash
  python servidor.py
  ```

---

## 📦 Gerenciamento de Dependências

- Para adicionar novos pacotes:
  ```bash
  uv add <nome-do-pacote>
  ```
- O arquivo `pyproject.toml` e o `uv.lock` serão atualizados automaticamente.

---

## 🤝 Contribua!

Contribuições são super bem-vindas!  
Basta abrir um _issue_ ou um _pull request_ com sua ideia, sugestão ou correção.

---

<div align="center">

Feito por [LoboProgrammingg](https://github.com/LoboProgrammingg)
---

</div>
