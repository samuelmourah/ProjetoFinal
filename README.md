# 📌  Mural de Recados
 Disciplina: Web II
Curso: Técnico Integrado em Informática – IFCE

## 📖 1. Descrição Geral

### O Murral de Recados é uma aplicação web que permite ao usuário criar, buscar, visualizar e excluir recados, cada um contendo um título e uma mensagem.
### O projeto foi desenvolvido para praticar organização de pastas no padrão MVC simples, manipulação de dados e criação de páginas web interativas.

## ✨ 2. Funcionalidades

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

## 🗂 3. Estrutura de Pastas
![Image](https://github.com/user-attachments/assets/721fad1e-62de-4821-8653-81eeb6c839fe)

## ⚙ 4. Como Rodar o Projeto

Requisitos

	•	Python 3 instalado
	
Passo a passo

	1.	Abra o terminal na pasta principal.
	2.	Execute:
	python run.py
	
3.	Acesse o sistema no navegador:
http://localhost:5000

## 🧠 5. Lógica de Funcionamento (Resumo Técnico)

### 📌 Model (modelo.py)

Responsável por gerenciar os dados:

	•	Estrutura para armazenar título + mensagem
	•	Métodos:
	•	adicionar_recado(titulo, mensagem)
	•	buscar_recado(termo)
	•	listar_recados()
	•	excluir_recado(titulo) (ou ID)

### 📌 Controller (views.py)
	•	Recebe dados do formulário
	•	Chama métodos do model
	•	Renderiza páginas com os resultados

### 📌 Templates (HTML)
	•	Formulário para título e texto do recado
	•	Páginas para exibir buscas, exclusões e listas


## 🎨 6. Layout e Design

O style.css organiza:

	•	Cores, botões, tipografia
	•	Espaçamentos e alinhamentos
	•	Responsividade básica

O script.js pode conter:

	•	Confirmações de exclusão
	•	Alertas
	•	Ajustes de interação

## 📌 7. Possíveis Melhorias Futuras
	•	Adicionar edição de recados
	•	Salvar dados em arquivo ou banco de dados
	•	Criar IDs únicos para cada recado
	•	Implementar login simples para usuários

## 👩‍💻 8. Autores
	• Samuel Oliveira 
	• Joyciane Sousa 
	• Ana Júlia A. 
	
