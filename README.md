# MCPs-IA

Repositório para desenvolvimento de aplicações de Inteligência Artificial utilizando Python.

---

## 🚀 Como começar

Clone o repositório e prepare o ambiente com o [uv](https://github.com/astral-sh/uv), um gerenciador de dependências moderno para Python.

```bash
git clone https://github.com/LoboProgrammingg/MCPs-IA.git
cd MCPs-IA
uv init
uv add fastmcp genai google-genai google-generativeai python-dotenv wikipedia
```

Crie um arquivo `.env` na raiz do projeto com suas variáveis de ambiente.

---

## 📁 Estrutura do Projeto

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
- **.env**: Variáveis de ambiente (NÃO versionado).
- **.gitignore**: Arquivos e pastas ignorados pelo Git.
- **pyproject.toml**: Gerenciamento das dependências do projeto.
- **uv.lock**: Lockfile gerado pelo uv.
- **.venv/**: Ambiente virtual (NÃO versionado).

---

## 🛠️ Requisitos

- Python 3.11 ou superior
- [uv](https://github.com/astral-sh/uv) instalado (`pip install uv`)

---

## ⚙️ Scripts principais

- `client.py`: Executa o cliente.
- `servidor.py`: Executa o servidor.

Execute cada script com:
```bash
uv venv
uv pip install -r requirements.txt  # Caso haja requirements.txt
python client.py
# ou
python servidor.py
```

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Abra um issue ou pull request para discutir melhorias ou relatar problemas.

---

## 📄 Observações

- Os arquivos `.env` e a pasta `.venv/` NÃO devem ser versionados.
- Para adicionar novas dependências, utilize:
  ```bash
  uv add <nome-do-pacote>
  ```

---