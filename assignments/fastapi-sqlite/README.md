# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Parta da API de tarefas criada na atividade anterior e substitua o armazenamento em memória por SQLite. Você praticará persistência, consultas SQL parametrizadas e integração de banco de dados com FastAPI.

## 📝 Tasks

### 🛠️ Initialize the SQLite Database

#### Description
Configure um banco SQLite local para armazenar tarefas e inicialize a tabela quando a aplicação iniciar.

#### Requirements
A API concluída deve:

- Usar o módulo `sqlite3` da biblioteca padrão do Python e armazenar os dados em `tasks.db`.
- Executar a API com `uvicorn starter-code:app --reload` a partir desta pasta.
- Criar uma tabela `tasks` com `id` inteiro e chave primária, `title` obrigatório e `completed` com valor padrão `0`.
- Criar a tabela com `IF NOT EXISTS` para que iniciar a aplicação novamente não apague os dados existentes.

### 🛠️ Persist Task Creation and Listing

#### Description
Substitua o armazenamento em memória por consultas ao banco de dados nas operações de criação e listagem de tarefas.

#### Requirements
A API concluída deve:

- Fazer `GET /tasks` retornar as tarefas armazenadas no SQLite.
- Fazer `POST /tasks` salvar a nova tarefa no banco e retornar o registro criado com status `201`.
- Usar parâmetros SQL nas consultas, em vez de interpolar valores recebidos do usuário na string SQL.

### 🛠️ Persist Task Retrieval, Updates, and Deletion

#### Description
Complete a migração para que todas as operações de tarefas leiam e alterem os dados persistidos.

#### Requirements
A API concluída deve:

- Fazer `GET /tasks/{task_id}` e `PUT /tasks/{task_id}` ler e atualizar o registro correspondente.
- Fazer `DELETE /tasks/{task_id}` remover o registro correspondente.
- Retornar status `404` quando uma tarefa solicitada para consulta, atualização ou exclusão não existir.
- Manter os dados após encerrar e iniciar novamente o servidor.