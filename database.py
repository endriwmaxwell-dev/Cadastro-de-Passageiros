import sqlite3

def conectar():
    conexao = sqlite3.connect("onibus.db")
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passageiros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            linha TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def cadastrar(nome, idade, linha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        " INSERT INTO passageiros (nome, idade, linha) VALUES (?, ?, ?)",
        (nome, idade, linha)
    )
    conexao.commit()
    conexao.close()

def listar():
    conexao = conectar()
    curso = conexao.cursor()
    curso.execute("SELECT * FROM passageiros;")
    resultados = curso.fetchall()
    conectar().close()
    return resultados

def buscar_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM passageiros WHERE nome LIKE ?", ('%' + nome + '%',))
    resultados = cursor.fetchall()
    conectar().close()
    return resultados

def atualizar(id_passageiro, nova_linha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE passageiros SET linha = ? WHERE id = ?",
        (nova_linha, id_passageiro)
    )
    conexao.commit()
    conexao.close()

def excluir(id_passageiro):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM passageiros WHERE id = ?", (id_passageiro,))
    conexao.commit()
    conexao.close()















