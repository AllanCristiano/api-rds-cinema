# api-rds-cinema
Api para projeto da aula de banco de dados

## Uso
Acesse a documentação da API em http://localhost:8000/docs para ver todas as rotas disponíveis e testá-las.

## Rotas
### Clientes
- POST /clientes/: Cria um novo cliente.
- GET /clientes/: Retorna todos os clientes.
- PUT /clientes/{cliente_id}: Atualiza os detalhes de um cliente existente.
- DELETE /clientes/{cliente_id}: Deleta um cliente.

### Filmes
- POST /filmes/: Cria um novo filme.
- GET /filmes/: Retorna todos os filmes.
- PUT /filmes/{filme_id}: Atualiza os detalhes de um filme existente.
- DELETE /filmes/{filme_id}: Deleta um filme.

### Promoções
- POST /promocoes/: Cria uma nova promoção.
- GET /promocoes/: Retorna todas as promoções.
- PUT /promocoes/{promocao_id}: Atualiza os detalhes de uma promoção existente.
- DELETE /promocoes/{promocao_id}: Deleta uma promoção.

### Avaliações
- POST /avaliacoes/: Cria uma nova avaliação. Os campos necessários são `id_cliente`, `id_filme`, `nota(1 a 5)`, `comentario`, e `data_avaliacao`
- GET /avaliacoes/: Retorna todas as avaliações.
- GET /avaliacoes/{avaliacao_id}: Retorna os detalhes de uma avaliação específica.
- PUT /avaliacoes/{avaliacao_id}: Atualiza os detalhes de uma avaliação existente. Os campos necessários são `id_cliente`, `id_filme`, `nota(1 a 5)`, `comentario`, e `data_avaliacao`.


### Clientes_Promoções
- POST /clientes_promocoes/: Cria uma nova participação de um cliente em uma promoção. Os campos necessários são `id_cliente` e `id_promocao`.
- GET /clientes_promocoes/: Retorna todas as participações de clientes em promoções.
- GET /clientes_promocoes/{cliente_id}/{promocao_id}: Retorna os detalhes de uma participação específica de um cliente em uma promoção.
- PUT /clientes_promocoes/{cliente_id}/{promocao_id}: Atualiza os detalhes de uma participação de um cliente em uma promoção. Os campos necessários são `id_cliente` e `id_promocao`.
- DELETE /clientes_promocoes/{cliente_id}/{promocao_id}: Deleta a participação de um cliente em uma promoção.




## Tecnologias Utilizadas
- FastAPI: Framework web assíncrono para Python.
- PostgreSQL: Sistema de gerenciamento de banco de dados relacional.
- AWS RDS: Serviço de banco de dados relacional da Amazon Web Services.

## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões, correções de bugs ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
