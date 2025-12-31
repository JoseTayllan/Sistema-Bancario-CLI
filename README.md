# 🏦 Sistema Bancário em Python (CLI)

Projeto desenvolvido como parte do **Desafio do Módulo 2 – Bootcamp Luizalabs | Back-end com Python (DIO)**.
O objetivo é aplicar conceitos fundamentais de **Python**, **lógica de programação** e **regras de negócio**, simulando um sistema bancário simples executado via **terminal (CLI)**.

---

## 📌 Funcionalidades

✔ Cadastro de usuários (identificados por CPF)
✔ Criação de contas correntes vinculadas a usuários
✔ Listagem de contas cadastradas
✔ Depósitos em conta
✔ Saques com regras de negócio
✔ Emissão de extrato bancário detalhado

---

## 🧠 Regras de Negócio Implementadas

* Cada usuário é identificado **exclusivamente pelo CPF**
* Não é permitido cadastrar mais de um usuário com o mesmo CPF
* Cada conta corrente:

  * Está vinculada a um único usuário
  * Possui **agência fixa `0001`**
  * Possui **número sequencial automático**
* Regras para saque:

  * Limite de valor por saque
  * Máximo de **3 saques diários**
  * Não é permitido sacar valor maior que o saldo
* O extrato registra **todas as movimentações**, incluindo depósitos e saques

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* Biblioteca padrão:

  * `textwrap`

---

## 📂 Estrutura do Projeto

```text
.
├── desafio.py
└── README.md
```

---

## ▶️ Como Executar o Projeto

1. Clone este repositório ou copie o arquivo `desafio.py`
2. No terminal, navegue até o diretório do projeto
3. Execute o comando:

```bash
python desafio.py
```

---

## 📄 Exemplo de Uso

```text
========== MENU ==========
[d] Depositar
[s] Sacar
[e] Extrato
[n] Nova conta
[u] Novo usuário
[l] Listar contas
[q] Sair
==========================
```

---

## 🎯 Objetivo Educacional

Este projeto tem como foco:

* Reforçar fundamentos da linguagem Python
* Trabalhar com estruturas de dados e controle de fluxo
* Implementar regras de negócio próximas a um cenário real
* Praticar organização e clareza de código

---

## 🚀 Próximas Melhorias (Sugestões)

* Persistência de dados (arquivo ou banco de dados)
* Implementação de orientação a objetos (POO)
* Testes automatizados
* Interface gráfica ou API REST

---

📌 *Projeto desenvolvido para fins educacionais no Bootcamp Luizalabs – Back-end com Python.*
