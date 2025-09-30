# Automação de Processos Internos - SCI Web

Este projeto contém scripts para automatizar tarefas repetitivas dentro do sistema SCI Web.

## Módulo Atual: Atualização de CNPJ de Empresa Teste

O script `main.py` realiza o login no sistema, busca por uma empresa de teste pré-definida e atualiza o seu CNPJ.

---

### Pré-requisitos

-   [Python 3.8+](https://www.python.org/downloads/) instalado.
-   [Git](https://git-scm.com/downloads/) instalado.
-   Google Chrome instalado.

---

### Como Configurar e Rodar o Projeto

**1. Clone o Repositório:**
Abra o terminal e clone o projeto para a sua máquina.
```bash
git clone URL_DO_SEU_REPOSITORIO.git
cd automacao-sci
```

**2. Crie e Ative o Ambiente Virtual:**
Isso garante que as dependências do projeto não interfiram com outros projetos Python.
```bash
# Crie o ambiente
python -m venv venv

# Ative o ambiente

# No Windows:
.\venv\Scripts\activate

# No macOS/Linux:
source venv/bin/activate
```

**3. Instale as Dependências:**
Com o ambiente ativado, instale todas as bibliotecas necessárias com um único comando.
```bash
pip install -r requirements.txt
```

**4. Configure suas Credenciais:**
O script lê informações sensíveis de um arquivo `.env` para evitar expor dados no código.
-   Renomeie (ou crie) o arquivo `.env.example` para `.env`.
-   Abra o arquivo `.env` e preencha com suas informações:
    ```ini
    SCI_USER="seu_login_aqui"
    SCI_PASS="sua_senha_aqui"
    CNPJ_TESTE="cnpj_que_sera_usado_para_atualizar"
    EMPRESA_TESTE="Nome Exato Da Empresa Teste Para Busca"
    ```
*O arquivo `.env` já está no `.gitignore`.*

**5. Execute a Automação:**
Basta executar o script `main.py`.
```bash
python main.py
```

O script irá iniciar, executar os passos e imprimir o status no terminal. O navegador permanecerá aberto no final para verificação.
