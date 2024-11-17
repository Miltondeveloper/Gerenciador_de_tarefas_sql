#importando o sqlite
import sqlite3 as lite

#CRUD(CREATE, READ, UPDATE, DELETE)

# C = inserir/criar

#Criando conexão
conex = lite.connect('database.db')

#lista= ['Terminar o PI', "08/12/2024", "11/24/2024", 'Alta', 'Projeto integrador do curo de DS']

#inserir informações

def inserir_info(i):
    with conex:
        cur = conex.cursor()
        query = "INSERT INTO lista_de_tarefas(Nome_da_tarefa, Data_de_inicio, Data_de_Termino, Prioridade, Descrição) VALUES (?,?,?,?,?)"
        cur.execute(query, i)



# R = Read/Ler
#Acessar informações     


def mostrar_info():
    lista = []
    with conex:
        cur = conex.cursor()
        query = "SELECT * FROM lista_de_tarefas"
        cur.execute(query)
        info = cur.fetchall()
        
        for i in info:
                lista.append(i)  
    return lista  
       
    





# U = Update/atualizar

def atualizar_informacao(i):
    with conex:
        cur = conex.cursor()
        query = "UPDATE lista_de_tarefas SET Nome_da_tarefa=?, Data_de_inicio=?, Data_de_Termino=?, Prioridade=?, Descrição=? WHERE id=?"
        cur.execute(query, i)


'''
lista = [1]
# D = Delete/apagar

with conex:
    cur = conex.cursor()
    query = "DELETE FROM lista_de_tarefas WHERE id=?"
    cur.execute(query, lista)
'''