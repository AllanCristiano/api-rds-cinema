from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import psycopg2
from psycopg2 import sql

## comando rodar uvicode uvicorn main:app --reload --port 8080
# Definindo modelos Pydantic para as tabelas
class Cliente(BaseModel):
    nome: str
    email: str
    telefone: Optional[str] = None
    saldo: Optional[float] = None


class Filme(BaseModel):
    titulo: str
    diretor: Optional[str] = None
    ano_lancamento: Optional[int] = None


class Promocao(BaseModel):
    nome: str
    descricao: Optional[str] = None
    desconto: float


# Configuração do banco de dados
DATABASE = {
    'dbname': 'tabelas_cinema',
    'user': 'aluno',
    'password': 'aluno123',
    'host': 'db-rds-cinema.c6ieh0ptqnno.us-east-1.rds.amazonaws.com'
}

# Inicialização do aplicativo FastAPI
app = FastAPI()


# Função para conectar ao banco de dados
def connect_to_db():
    return psycopg2.connect(**DATABASE)


# Rotas CRUD para a tabela de clientes
@app.post("/clientes/")
def create_cliente(cliente: Cliente):
    query = sql.SQL("INSERT INTO cinema.clientes (nome, email, telefone, saldo) VALUES (%s, %s, %s, %s)")
    data = (cliente.nome, cliente.email, cliente.telefone, cliente.saldo)
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()
        return {"message": "Cliente criado com sucesso"}


@app.get("/clientes/")
def read_clientes():
    query = sql.SQL("SELECT * FROM cinema.clientes")
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query)
        return [{"id_cliente": row[0], "nome": row[1], "email": row[2], "telefone": row[3], "saldo": row[4]} for row in
                cur.fetchall()]


@app.put("/clientes/{cliente_id}")
def update_cliente(cliente_id: int, cliente: Cliente):
    query = sql.SQL("UPDATE cinema.clientes SET nome = %s, email = %s, telefone = %s, saldo = %s WHERE id_cliente = %s")
    data = (cliente.nome, cliente.email, cliente.telefone, cliente.saldo, cliente_id)
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()
        return {"message": f"Cliente com id {cliente_id} atualizado com sucesso"}


@app.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int):
    query = sql.SQL("DELETE FROM cinema.clientes WHERE id_cliente = %s")
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, (cliente_id,))
        conn.commit()
        return {"message": f"Cliente com id {cliente_id} deletado com sucesso"}


# Rotas CRUD para a tabela de filmes
@app.post("/filmes/")
def create_filme(filme: Filme):
    query = sql.SQL("INSERT INTO cinema.filmes (titulo, diretor, ano_lancamento) VALUES (%s, %s, %s)")
    data = (filme.titulo, filme.diretor, filme.ano_lancamento)
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()
        return {"message": "Filme criado com sucesso"}


@app.get("/filmes/")
def read_filmes():
    query = sql.SQL("SELECT * FROM cinema.filmes")
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query)
        return [{"id_filme": row[0], "titulo": row[1], "diretor": row[2], "ano_lancamento": row[3]} for row in
                cur.fetchall()]


@app.put("/filmes/{filme_id}")
def update_filme(filme_id: int, filme: Filme):
    query = sql.SQL("UPDATE cinema.filmes SET titulo = %s, diretor = %s, ano_lancamento = %s WHERE id_filme = %s")
    data = (filme.titulo, filme.diretor, filme.ano_lancamento, filme_id)
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()
        return {"message": f"Filme com id {filme_id} atualizado com sucesso"}


@app.delete("/filmes/{filme_id}")
def delete_filme(filme_id: int):
    query = sql.SQL("DELETE FROM cinema.filmes WHERE id_filme = %s")
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, (filme_id,))
        conn.commit()
        return {"message": f"Filme com id {filme_id} deletado com sucesso"}


# Rotas CRUD para a tabela de promoções
@app.post("/promocoes/")
def create_promocao(promocao: Promocao):
    query = sql.SQL("INSERT INTO cinema.promocoes (nome, descricao, desconto) VALUES (%s, %s, %s)")
    data = (promocao.nome, promocao.descricao, promocao.desconto)
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()
        return {"message": "Promoção criada com sucesso"}


@app.get("/promocoes/")
def read_promocoes():
    query = sql.SQL("SELECT * FROM cinema.promocoes")
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query)
        return [{"id_promocao": row[0], "nome": row[1], "descricao": row[2], "desconto": row[3]} for row in
                cur.fetchall()]


@app.put("/promocoes/{promocao_id}")
def update_promocao(promocao_id: int, promocao: Promocao):
    query = sql.SQL("UPDATE cinema.promocoes SET nome = %s, descricao = %s, desconto = %s WHERE id_promocao = %s")
    data = (promocao.nome, promocao.descricao, promocao.desconto, promocao_id)
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()
        return {"message": f"Promoção com id {promocao_id} atualizada com sucesso"}


@app.delete("/promocoes/{promocao_id}")
def delete_promocao(promocao_id: int):
    query = sql.SQL("DELETE FROM cinema.promocoes WHERE id_promocao = %s")
    with connect_to_db() as conn, conn.cursor() as cur:
        cur.execute(query, (promocao_id,))
        conn.commit()
        return {"message": f"Promoção com id {promocao_id} deletada com sucesso"}

