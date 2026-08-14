#Escolhi o SQLite pois ele armazena o banco de dados inteiro em um unico arquivo, e nao precisa de servidor
import sqlite3

#Essa funçao e responsavel pela conexao, e por ser possivel reutilizar em outras partes do codigo sem precisar reescrever
def conectar():
    conexao = sqlite3.connect("onibus.db")
    return conexao

"""
"cursor": é o executor dos comando do SQL, "CREATE TABLE IF NOT EXISTS": cria a tabela se ela nao existir
"id INTEGER PRIMARY KEY AUTOINCREMENT": cria o identificador que o SQL cria sozinho
"NOT NULL": obriga quem utilizar o sistema a preencher o campo solicitado (nao pode ficar sozinho)
"conexao.commit()": grava e salva as mudanças no arquivo e "conexao.close()": fecha a conexao com o arquivo.
"""
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
    
"""
O "?": é uma tupla que separa os dados passados (nome, idade, linha)
"f"INSERT INTO passageiros VALUES ('{nome}', ...)"": essa foi uma parametrizaçao da query pelo que estudei nao e muito seguro 
mas decidi usar para aprender, pois pelo que li ela pode ser muito bem utilizado quando utilizada corretamente e utilzar o "?"
o deixa mais segura a utilzar.
"""
def cadastrar(nome, idade, linha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        " INSERT INTO passageiros (nome, idade, linha) VALUES (?, ?, ?)",
        (nome, idade, linha)
    )
    conexao.commit()
    conexao.close()

"""
"SELECT * FROM passageiros": seleciona todas as linhas e colunas, "fetchall()" retorna o resultado como uma lista de tuplas Ex:
[(1, 'Maxwell', 19, 'Linha 100'), (2, 'Ana', 25, 'Linha 200')], cada tupla é uma linha em uma tabela.
"""
def listar():
    conexao = conectar()
    curso = conexao.cursor()
    curso.execute("SELECT * FROM passageiros;")
    resultados = curso.fetchall()
    conectar().close()
    return resultados

"""
"WHERE nome LIKE ?": Filtra o resultado, "LIKE + %texto%": Faz a busca parcial mesmo se o nome nao estiver completo ele encontra 
o nome "Max" na pesquisa que seria "Maxwell" e o "%" é um coringa que siguinifica qualquer coisa depois.
"""
def buscar_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM passageiros WHERE nome LIKE ?", ('%' + nome + '%',))
    resultados = cursor.fetchall()
    conectar().close()
    return resultados

#"UPDATE SET coluna = valor WHERE id = ?": Aqui é nao pode esquecer de usar o WHERE no UPDATE se nao atualiza toda a tabela.
def atualizar(id_passageiro, nova_linha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE passageiros SET linha = ? WHERE id = ?",
        (nova_linha, id_passageiro)
    )
    conexao.commit()
    conexao.close()

#Mesma logica de cima nao use um DELETE sem WHERE se nao vais apagar toda a tabela.
def excluir(id_passageiro):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM passageiros WHERE id = ?", (id_passageiro,))
    conexao.commit()
    conexao.close()
