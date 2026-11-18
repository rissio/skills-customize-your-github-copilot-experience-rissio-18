# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprender a criar uma API REST simples com o framework FastAPI, definindo rotas que recebem e retornam dados em JSON.

## 📝 Tarefas

### 🛠️ Criar uma API de Tarefas

#### Descrição
Crie uma API com FastAPI que gerencie uma lista de tarefas em memória.

#### Requisitos
O programa concluído deve:

- Expor uma rota `GET /tasks` que retorne a lista de tarefas
- Expor uma rota `POST /tasks` que adicione uma nova tarefa a partir de um JSON
- Expor uma rota `GET /tasks/{id}` que retorne uma tarefa específica ou erro 404 se não existir

### 🛠️ Validar os Dados

#### Descrição
Use modelos Pydantic para validar os dados recebidos pela API.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic com os campos `title` (string) e `done` (booleano)
- Rejeitar requisições com dados inválidos com resposta de erro apropriada
