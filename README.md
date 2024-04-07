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

## Tecnologias Utilizadas
- FastAPI: Framework web assíncrono para Python.
- PostgreSQL: Sistema de gerenciamento de banco de dados relacional.

## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões, correções de bugs ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
