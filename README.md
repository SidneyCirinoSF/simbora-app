# 🚀 Backend Simbora APP - Projeto Integrador (Padrão MTV)

## 💻 Visão Geral do Projeto

Este repositório contém o código **Backend** do **Simbora APP**, um projeto desenvolvido como parte do **Projeto Integrador** do curso de Programador de Sistemas. O projeto utiliza o framework Django.

O objetivo desta fase é estabelecer a base de dados e a lógica de negócios para o cadastro de usuários e perfis, renderizando as páginas web completas diretamente.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Django
* **Padrão de Projeto:** MTV (Model-Template-View)
* **Banco de Dados:** SQLite (`db.sqlite3`)
* **Gerenciamento de Dependências:** `requirements.txt`

## 🧩 Estrutura Inicial do Repositório

O repositório está estruturado em *apps* do Django para modularizar as funcionalidades:

| Diretório/Arquivo | Descrição |
| :--- | :--- |
| `manage.py` | Utilitário de linha de comando do Django. |
| `requirements.txt` | Lista de bibliotecas Python necessárias. |
| `core/` | App principal do projeto. Contém configurações básicas e modelos fundamentais. |
| `perfil/` | App dedicada à gestão dos dados adicionais do perfil do usuário. |
| `simbora_app/` | Diretório principal do projeto Django (contém `settings.py`, `urls.py`). |
| `media/fotos_perfil/` | Configurado para armazenar arquivos de mídia (ex: fotos de perfil). |


## ⚙️ Instalação e Configuração

Para configurar o ambiente de desenvolvimento:

### 1. Pré-requisitos

* Python (versão 3.x)
* Git

## 🧑‍💻 Autores e Equipe

O time de Back-end do Projeto Integrador é composto pelos seguintes membros (em ordem alfabética):

* **Alison**
* **Geovane**
* **Julia Gonçalves**
* **Julia Martins**
* **Katarina**
* **Sidney**

**Curso:** Programador de Sistemas
**Instituição:** SENAC em parceria com Serasa (Programa Transforme-se)

### 2. Clonar e Acessar o Repositório

```bash
git clone link_do_repositório
cd [nome-do-repositorio]

# 1. Criar ambiente virtual
python -m venv venv 

# 2. Ativar ambiente virtual (Linux/macOS)
source venv/bin/activate 

# 2. Ativar ambiente virtual (Windows)
.\venv\Scripts\activate

#3. Com o ambiente virtual ativo, instale todas as bibliotecas Python necessárias:
pip install -r requirements.txt

#4. Aplique as migrações do Django para criar o banco de dados (db.sqlite3) e as tabelas:
python manage.py makemigrations 
python manage.py migrate

#5. Inicie o servidor de desenvolvimento do Django:
python manage.py runserver

