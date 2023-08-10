import PySimpleGUI as sg
import sqlite3 as bbb

#faz conexão com o banco
conn = bbb.connect("Desktop/Manoel_py/clientes.db")
c = conn.cursor()

#criar layout do sistema de cadastro
layout = [
    [sg.Button("Cadastrar")]
]

#cria janela principal para chamar os componentes desta janela
window = sg.Window("Sistema de cadastro 1.0",layout,size=(600,400))

#while do cadastro de clientes
while True:
    event, values = window.read()


    if event == sg.WINDOW_CLOSED:
        break

    if event == "Cadastrar":

        #Criar layout do cadastro de clientes
        cadastro_layout = [
            [sg.Text("Nome")],      
            [sg.InputText(key="Nome")],
            [sg.Text("CPF")],      
            [sg.InputText(key="CPF")],
            [sg.Text("Endereço")],      
            [sg.InputText(key="Endereço")],
            [sg.Text("Telefone")],      
            [sg.InputText(key="Telefone")],
            [sg.Text("Cidade")],      
            [sg.InputText(key="Cidade")],
            [sg.Text("estado")],      
            [sg.InputText(key="Estado")],
            [sg.Button("Cadastro")],
            [sg.Button("Cancelar")]
        ]

        cadastro_window = sg.Window("Cadastro de cliente",cadastro_layout,size=(800,600))

        #While do cadastro
        while True:
            event, values = cadastro_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_window.close()
                break


            #interagindo com o banco
            c.execute("INSERT INTO clientes (Nome, CPF, Endereço, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)", (values["Nome"], values["CPF"], values["Endereço"], values["Telefone"], values["Cidade"], values["Estado"],))
            conn.commit()

            #Limpar iputs após o cadastro
            cadastro_window["Nome"].update("")
            cadastro_window["CPF"].update("")
            cadastro_window["Endereço"].update("")
            cadastro_window["Telefone"].update("")
            cadastro_window["Cidade"].update("")
            cadastro_window["Estado"].update("")

            #Confirmar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")
 
            #cadastro_window.close()

conn.close()

