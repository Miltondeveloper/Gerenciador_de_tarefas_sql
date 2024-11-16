# importando o custom tkinter
from tkinter import *
from tkinter import font

# Importando calendário
from tkcalendar import Calendar, DateEntry

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
janela.geometry("800x453")
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
l_cal = Label(frame_baixo,text='Data de término *',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4, relief='flat')
l_cal.place(x=150,y=70)

e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
e_cal.place(x=155,y=100)

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


janela.mainloop()