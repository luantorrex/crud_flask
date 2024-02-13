# Aplicação CRUD com Flask

Projeto de aplicação CRUD utilizando o framework *Flask*.
O projeto possui um blueprint e modelo para realizar a lógica de negócio de *Usuários*.

O padrão de design utilizado foi o *Factory Method*, um padrão bastante utilizado no Flask, pois permite realizarmos testes subindo a instância de uma aplicação.
Esse padrão também ajuda na escalabilidade, pois facilita a criação de múltiplas instâncias.

Para os testes foi utilizado o framework *pytest*.

Endpoints:
1. `GET /users`: Retorna a lista de todos os usuários.
2. `GET /users/{id}`: Retorna os detalhes de um usuário específico.
3. `POST /users`: Adiciona um novo usuário.
4. `PUT /users/{id}`: Atualiza os dados de um usuário existente.
5. `DELETE /users/{id}`: Remove um usuário.
