import PySimpleGUI as sg
import sqlite3 as bbb

#faz conexão com o banco
conn = bbb.connect("Desktop/Manoel_py/clientes.db")
c = conn.cursor()

#criar layout do sistema de cadastro
layout = [
    [sg.Button("Cadastrar")],
    [sg.Button("Fornecedores")],
    [sg.Button("Transportadora")]
]

#cria janela principal para chamar os componentes desta janela
window = sg.Window("Sistema de cadastro de clientes 1.0",layout,size=(600,400))

#while do cadastro de clientes
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Cadastrar":

        #Criar layout do cadastro de clientes
        cliente_layout = [
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
            [sg.Text("Estado")],      
            [sg.InputText(key="Estado")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
        ]

        #Cria uma janela para cadastrar clientes
        cliente_window = sg.Window("Cadastro de cliente",cliente_layout,size=(800,600))

        #While do cadastro
        while True:
            event, values = cliente_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cliente_window.close()
                break
            #faz conexão com banco, fazendo insert na tabela clientes    
            c.execute("INSERT INTO clientes (Nome, CPF, Endereço, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)", (values["Nome"], values["CPF"], values["Endereço"], values["Cidade"], values["Estado"]))
            conn.commit()

            #Limpa os inputs após o cadastro de clientes
            cliente_window["Nome"].update("")
            cliente_window["CPF"].update("")
            cliente_window["Endereço"].update("")
            cliente_window["Cidade"].update("")
            cliente_window["Estado"].update("")

            #mostra na tela que o cadastro foi realizado
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

    #elif para cadastro de fornecedores        
    elif event == "Fornecedores":

        #Criar layout do cadastro de fornecedores
        fornecedor_layout = [
            [sg.Text("Id_fornecedor")],      
            [sg.InputText(key="Id_fornecedor")],
            [sg.Text("Nome_fornecedor")],      
            [sg.InputText(key="Nome_fornecedor")],
            [sg.Text("Endereço")],      
            [sg.InputText(key="Endereço")],
            [sg.Text("CEP")],
            [sg.InputText(key="CEP")],
            [sg.Text("Cidade")],      
            [sg.InputText(key="Cidade")],
            [sg.Text("Estado")],      
            [sg.InputText(key="Estado")],
            [sg.Text("País")],
            [sg.InputText(key="País")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
        ]

        #Cria uma janela para cadastrar fornecedores
        fornecedor_window = sg.Window("Cadastro de Fornecedores",fornecedor_layout,size=(800,600))

        #While do cadastro
        while True:
            event, values = fornecedor_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                fornecedor_window.close()
                break
            
            #faz conexão com banco, fazendo insert na tabela fornecedores
            c.execute("INSERT INTO fornecedores (Id_fornecedor, Nome_fornecedor, Endereço, CEP, Cidade, Estado, País) VALUES (?, ?, ?, ?, ?, ?, ?)", (values["Id_fornecedor"], values["Nome_fornecedor"], values["Endereço"], values["CEP"], values["Cidade"], values["Estado"], values["País"]))
            conn.commit()

            #limpa os inputs apos o cadastro de fornecedores
            fornecedor_window["Id_fornecedor"].update("")
            fornecedor_window["Nome_fornecedor"].update("")
            fornecedor_window["Endereço"].update("")
            fornecedor_window["CEP"].update("")
            fornecedor_window["Cidade"].update("")
            fornecedor_window["Estado"].update("")
            fornecedor_window["País"].update("")

            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

    #elif para cadastro de transpotadores
    elif event == "Transportadora":

        #Criar layout do cadastro de transportadora
        transportadora_layout = [
            [sg.Text("Id_transportadora")],      
            [sg.InputText(key="Id_transportadora")],
            [sg.Text("Nome_transportadora")],      
            [sg.InputText(key="Nome_transportadora")],
            [sg.Text("Telefone")],      
            [sg.InputText(key="Telefone")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
        ]

        #Cria uma janela para cadastrar transportadoras
        transportadora_window = sg.Window("Cadastro de Transportadores",transportadora_layout,size=(800,600))

        #While do cadastro
        while True:
            event, values = transportadora_window.read()
     
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                transportadora_window.close()
                break

            #interagindo com o banco, realizando insert na tabela transportadora
            c.execute("INSERT INTO transportadora (Id_transportadora, Nome_transportadora, Telefone) VALUES (?, ?, ?)", (values["Id_transportadora"], values["Nome_transportadora"], values["Telefone"]))
            conn.commit()      

            #Limpar inputs após o cadastro de transportadores
            transportadora_window["Id_transportadora"].update("")
            transportadora_window["Nome_transportadora"].update("")
            transportadora_window["Telefone"].update("")

            #Confirmar o cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")
conn.close()

