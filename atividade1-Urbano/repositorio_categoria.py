from conexao import conectar

def inserir_categoria(nome, tipo):
    with conectar() as conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO categoria (nome, tipo) VALUES (%s, %s)"
        cursor.execute(sql, (nome, tipo))
        conexao.commit()

def listar_categorias():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, tipo FROM categoria")
        return cursor.fetchall()

def atualizar_categoria(id_categoria, nome, tipo):
    with conectar() as conexao:
        cursor = conexao.cursor()
        sql = "UPDATE categoria SET nome = %s, tipo = %s WHERE id = %s"
        cursor.execute(sql, (nome, tipo, (id_categoria,)))
        conexao.commit()

def excluir_categoria(id_categoria):
    with conectar() as conexao:
        cursor = conexao.cursor()
        sql = "DELETE FROM categoria WHERE id = %s"
        cursor.execute(sql, (id_categoria,))
        conexao.commit()