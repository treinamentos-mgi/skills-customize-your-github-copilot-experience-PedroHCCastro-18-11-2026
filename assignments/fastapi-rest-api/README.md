# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará rotas HTTP, modelos de dados, validação de entrada e códigos de status.

## 📝 Tasks

### 🛠️ Create the API and List Tasks

#### Description
Configure o aplicativo FastAPI e crie uma rota para consultar as tarefas armazenadas em memória.

#### Requirements
A API concluída deve:

- Criar uma instância FastAPI no arquivo `starter-code.py`.
- Implementar `GET /tasks` para retornar a lista de tarefas, inicialmente vazia.
- Iniciar o servidor localmente com `uvicorn starter-code:app --reload`.

### 🛠️ Create and Retrieve Tasks

#### Description
Defina os modelos de dados e implemente rotas para criar uma tarefa e consultar uma tarefa pelo identificador.

#### Requirements
A API concluída deve:

- Usar modelos Pydantic para validar os dados de entrada e representar uma tarefa com `id`, `title` e `completed`.
- Implementar `POST /tasks` para criar uma tarefa e retornar o código de status `201`.
- Implementar `GET /tasks/{task_id}` para retornar a tarefa correspondente ou responder com `404` quando ela não existir.

### 🛠️ Update and Delete Tasks

#### Description
Complete as operações da API permitindo atualizar e excluir tarefas existentes.

#### Requirements
A API concluída deve:

- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado `completed` de uma tarefa.
- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa existente e retornar `204`.
- Retornar `404` ao tentar atualizar ou excluir uma tarefa que não existe.