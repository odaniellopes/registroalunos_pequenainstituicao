#Objetivo: criar um protótipo utilizando a metodologia RAD.
'''
Aluno: Daniel Lopes da Costa // matrícula: 202108093785
Estácio maracanã noite
'''
#importando bibliotecas utilizadas no projeto
import requests
import tkinter
from tkinter import *


#Passo1: Solicitando o nome e a nota do aluno ao usuário na janela
def registro():
    nome_aluno = Label(janela, text='Insira o nome do aluno:')
    nome_aluno.grid(column=0, row=3)
    nome_aluno = tkinter.Entry()
    nome_aluno.grid(column=0, row=4)

    nota_aluno = Label(janela, text='Insira a nota do aluno: ')
    nota_aluno.grid(column=1,row=3)
    nota_aluno = tkinter.Entry()
    nota_aluno.grid(column=1, row=4)

#passo2: Inserindo o nome e a nota em um banco de dados
    def guardando_info():
        print(nome_aluno.get())


#passo3: exibindo todas as notas do aluno




#interface gráfica
janela = Tk()
janela.title('Registro de notas')
janela.rowconfigure([0,1,2,3], weight=1)
janela.columnconfigure([0, 1], weight=1)

texto_orientacao = Label(janela, text = 'Clique em iniciar para começar os registros', bg='Black', fg='white')
texto_orientacao.grid(column=0, row=0, columnspan=2, sticky='NSEW')

botao = Button(janela, text = 'Iniciar', command=registro)
botao.grid(column=0, row=2, columnspan=2)

botao2 = tkinter.Button(text='Registrar', command=registro)
botao2.grid(column=0, row=5, columnspan=2)

texto_dados = Label(janela, text = '')
texto_dados.grid(column=0, row=3)

janela.mainloop()


