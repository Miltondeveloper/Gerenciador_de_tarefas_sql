#importando o sqlite
import sqlite3 as lite

#criando conexao
conex = lite.connect('database.db')

#criando tabela
with conex:
    cur =  conex.cursor()
    cur.execute("CREATE TABLE lista_de_tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, Nome_da_tarefa TEXT, Data_de_inicio DATE, Data_de_Termino DATE, Prioridade TEXT, Descrição TEXT)")