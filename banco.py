#importando o sqlite
import sqlite3 as lite

#criando conexao
conex = lite.connect('database.db')

#criando tabela
with conex:
    cur =  conex.cursor()
    cur.execute("CREATE TABLE lista_de_tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_da_tarefa TEXT, status TEXT)")