# importando o custom tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox


# Importando calendário
from tkcalendar import Calendar, DateEntry

#importando views
import view
################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# Criando janela

janela = Tk()
janela.title("")
janela.geometry("1043x453")
janela.configure(background = co9)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a janela

frame_cima = Frame(janela, width=310, height=50, bg=co2,relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1,relief='flat')
frame_baixo.grid(row=1, column=0,sticky=NSEW,padx=0,pady=1)

frame_direita = Frame(janela, width=400, height=403, bg=co1,relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1,pady=0,sticky=NSEW)

# Label cima

app_nome = Label(frame_cima,text='Gerenciador de Tarefas',anchor=NW, font=('Ivy 13 bold'), bg=co2,fg=co1, relief='flat')
app_nome.place(x=10,y=20)

# variavel global tree
global tree


# função inserir
def inserir():
    nome = e_nome.get()
    inicio = e_cal.get()
    termino = e_cal2.get()
    estado = e_estado.get()
    descricao = e_descricao.get()

    lista = [nome, inicio, termino, estado, descricao]

    if nome=="":
        messagebox.showerror('Error', 'O nome não pode ser vazio')
    else:
        view.inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        e_nome.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_cal2.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_descricao.delete(0, 'end')

    # Apaga todos os dados inseridos e deixa a tela de digitação limpa
    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()



# função atualizar


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor_id = treev_lista[0]

        e_nome.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_cal2.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_descricao.delete(0, 'end')

        e_nome.insert(0, treev_lista[1])
        e_cal.insert(0, treev_lista[2])
        e_cal2.insert(0, treev_lista[3])
        e_estado.insert(0, treev_lista[4])
        e_descricao.insert(0, treev_lista[5])

        def update():
            nome = e_nome.get()
            inicio = e_cal.get()
            termino = e_cal2.get()
            estado = e_estado.get()
            descricao = e_descricao.get()

            lista = [nome, inicio, termino, estado, descricao, valor_id]

            if nome=="":
                messagebox.showerror('Error', 'O nome não pode ser vazio')
            else:
                view.atualizar_informacao(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                e_nome.delete(0, 'end')
                e_cal.delete(0, 'end')
                e_cal2.delete(0, 'end')
                e_estado.delete(0, 'end')
                e_descricao.delete(0, 'end')

            # Apaga todos os dados inseridos e deixa a tela de digitação limpa
            for widget in frame_direita.winfo_children():
                widget.destroy()
            
            mostrar()

        #Botão atualizar
        b_confirmar = Button(frame_baixo,command=update, text='Confirmar',width=10, font=('Ivy 9 bold'), bg=co2,fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=105,y=320)

       

    except IndexError:
        messagebox.showerror('Error', 'Selecione um dos dados na tabela')

# Configurando frame baixo

# Nome da tarefa
l_nome = Label(frame_baixo,text='Nome da Tarefa *',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4, relief='flat')
l_nome.place(x=10,y=10)

e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15,y=40)

# Data de inicio
l_cal = Label(frame_baixo,text='Data de início *',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4, relief='flat')
l_cal.place(x=10,y=70)

e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
e_cal.place(x=15,y=100)

# Data de término
l_cal2 = Label(frame_baixo,text='Data de término *',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4, relief='flat')
l_cal2.place(x=150,y=70)

e_cal2 = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
e_cal2.place(x=155,y=100)

# Nível de prioridade da tarefa
l_estado = Label(frame_baixo,text='Nível de prioridade da Tarefa *',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4, relief='flat')
l_estado.place(x=10,y=130)

e_estado = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_estado.place(x=15,y=160)

# Descrição da tarefa
l_descricao = Label(frame_baixo,text='Descrição da tarefa *',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4, relief='flat')
l_descricao.place(x=10,y=190)

e_descricao = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_descricao.place(x=15,y=220)

#Botão inserir
b_inserir = Button(frame_baixo,command=inserir, text='Inserir',width=10,font=('Ivy 9 bold'), bg=co6,fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15,y=270)

#Botão atualizar
b_atualizar = Button(frame_baixo,command=atualizar, text='Atualizar',width=10, font=('Ivy 9 bold'), bg=co2,fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=105,y=270)

#Botão deletar
b_deletar = Button(frame_baixo,text='Deletar',width=10, font=('Ivy 9 bold'), bg=co7,fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=195,y=270)

def mostrar():

    global tree

    lista = view.mostrar_info()
    
#Lista para cabeçalho
    tabela_head = ['ID', 'Nome da Tarefa', 'Data de início', 'Data de término', 'Prioridade', 'Descrição']

# criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show='headings')

#Scroll vertical
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

#Scroll horizontal
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "nw", "center", "center"]
    h=[30, 170, 100, 100, 100, 120]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajustando o tamanho da coluna para o cabeçalho
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

    

#chamando a função mostrar
mostrar()




janela.mainloop()