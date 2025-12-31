# 🏦 Sistema Bancário em Python (CLI)

Projeto desenvolvido como parte do **Desafio do Módulo 2 – Bootcamp Luizalabs | Back-end com Python (DIO)**.  
O sistema simula operações básicas de um banco utilizando **Python puro**, com execução via **terminal (CLI)**.

---

## 📌 Funcionalidades

✔ Criar usuários  
✔ Criar contas correntes vinculadas a usuários  
✔ Listar contas cadastradas  
✔ Realizar depósitos  
✔ Realizar saques com regras de negócio  
✔ Exibir extrato bancário  

---

## 🧠 Regras de Negócio Implementadas

- Cada usuário é identificado unicamente pelo **CPF**
- Não é permitido cadastrar dois usuários com o mesmo CPF
- Uma conta corrente:
  - Pertence a um usuário
  - Possui **agência fixa (`0001`)**
  - Possui número sequencial automático
- Saques possuem:
  - **Limite de valor por saque**
  - **Limite máximo de 3 saques**
- O extrato registra todas as movimentações (depósitos e saques)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Biblioteca padrão:
  - `textwrap`

---

## ▶️ Como Executar o Projeto

1. Clone o repositório ou copie o arquivo `.py`
2. No terminal, navegue até a pasta do projeto
3. Execute o comando:

```bash
python desafio.py
