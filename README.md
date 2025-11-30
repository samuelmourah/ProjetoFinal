## 📌 Projeto Final — Sistema de Recados

Disciplina: Web II
Curso: Técnico Integrado em Informática – IFCE

⸻

### 📖 1. Descrição Geral

O Sistema de Recados é uma aplicação web que permite ao usuário criar, buscar, visualizar e excluir recados, cada um contendo um título e uma mensagem.
O projeto foi desenvolvido para praticar organização de pastas no padrão MVC simples, manipulação de dados e criação de páginas web interativas.

⸻

### ✨ 2. Funcionalidades

✔ Adicionar recado com título

O usuário pode cadastrar um recado informando:
	•	Título do recado
	•	Mensagem ou descrição do recado

Ambos são armazenados pela aplicação.

✔ Listar/visualizar recados

Exibe todos os recados cadastrados, mostrando título e mensagem.

✔ Buscar recado

Permite pesquisar recados pelo título ou por palavras presentes na mensagem.

✔ Excluir recado

Remove um recado específico da lista, atualizando imediatamente as informações exibidas.

⸻

### 🗂 3. Estrutura de Pastas

/projeto_final
│
├── /controllers
│   └── views.py
│       - Controla rotas e integra as páginas com o model.
│
├── /models
│   └── modelo.py
│       - Armazena os recados e implementa métodos:
│         adicionar, buscar, listar, excluir.
│
├── /templates
│   ├── index.html             # Página principal (formulário para título e recado)
│   └── outras_paginas.html    # Demais páginas do sistema
│
├── /static
│   ├── /css
│   │   └── style.css
│   │
│   ├── /js
│   │   └── script.js
│   │
│   └── /img
│       └── imagens usadas no projeto
│
├── README.md
└── run.py
