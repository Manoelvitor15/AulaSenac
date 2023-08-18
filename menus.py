import PySimpleGUI as sg
import sqlite3 as bbb

conn = bbb.connect("clientes.db.db")
c = conn.cursor()

layout = [
    [sg.Menu([
        ['Cadastro', ['Cadastro Clientes','Cadastro Fornecedores', 'Cadastro Transportadora']],
        ['Consulta', ['Consulta Clientes','Consulta Fornecedores', 'Consulta Transportadora']],
        ['Relatórios', ['Relatórios Clientes','Relatórios Fornecedores', 'Relatórios Transportadora']]
    ], tearoff=False)]
]

layout_window = sg.Window("Menu do Sistema 1.0",layout,resizable=True,size=(600,400))

while True:
    event, values = layout_window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == "Cadastro Clientes":
        cadastro_layout_clientes = [
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
            [sg.Button("Cadastrar"), sg.Button("Cancelar")]
        ]
        cadastro_clientes = sg.Window("Cadastro de clientes", cadastro_layout_clientes, resizable=True,size=(600,400))
        while True:
            event, values = cadastro_clientes.read()
            if event == cadastro_clientes.close() or event == "Cancelar":
                cadastro_clientes.close()
                break
            
            c.execute("INSERT INTO clientes (Nome, CPF, Endereço, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)", (values["Nome"], values["CPF"], values["Endereço"], values["Telefone"], values["Cidade"], values["Estado"]))
            conn.commit()
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")
            
    elif event == "Consulta Clientes":
        consulta_layout_clientes = [
            [sg.Text("CPF")],
            [sg.InputText(key="CPF")],
            [sg.Button("Consultar"), sg.Button("Cancelar")],
            [sg.Table(values=[], headings=["Nome","CPF","Endereço","Telefone","Cidade","Estado"], display_row_numbers=False, auto_size_columns=False, num_rows=1, key="tabela")]
        ]
        consulta_clientes = sg.Window("Consulta de clientes",consulta_layout_clientes,resizable=True,size=(1000,800))
        while True:
            event, values = consulta_clientes.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_clientes.close()
                break

                # operações no banco de dados
            produto_busca = values["CPF"].upper()
            c.execute("SELECT Nome, CPF, Endereço, Telefone, Cidade, Estado FROM clientes WHERE UPPER(CPF) = ?", (produto_busca,))
            registros = c.fetchall()

                # atualizar
            tabela = consulta_clientes["tabela"]
            tabela.update(values=registros)
                
                
    #elif event == "Relatório Clientes":
    
    elif event == "Cadastro Fornecedores":
        cadastro_layout_fornecedores = [
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
            [sg.Button("Cadastrar"), sg.Button("Cancelar")]
        ]
        cadastro_fornecedores = sg.Window("Cadastro de Fornecedores",cadastro_layout_fornecedores,resizable=True,size=(800,400))
        while True:
            event, values = cadastro_fornecedores.read()
            if event == cadastro_fornecedores.close() or event == "Cancelar":
                cadastro_fornecedores.close()          
                break
            c.execute("INSERT INTO fornecedores (Id_fornecedor, Nome_fornecedor, Endereço, CEP, Cidade, Estado, País) VALUES (?, ?, ?, ?, ?, ?, ?)", (values["Id_fornecedor"], values["Nome_fornecedor"], values["Endereço"], values["CEP"], values["Cidade"], values["Estado"], values["País"]))
            conn.commit()
            sg.popup("Cadastro realizado!", title="Cadastro")
            
            
           
    elif event == "Consulta Fornecedores":
        consulta_layout_fornecedores = [
            [sg.Text("Id_fornecedor")],
            [sg.InputText(key="Id_fornecedor")],
            [sg.Button("Consultar"), sg.Button("Cancelar")],
            [sg.Table(values=[], headings=["Id_fornecedor","Nome_fornecedor","Endereço","CEP","Cidade","Estado","País"], display_row_numbers=False, auto_size_columns=False, num_rows=1, key="tabela")]
        ]
        consulta_fornecedor = sg.Window("Consultar Fornecedores",consulta_layout_fornecedores,resizable=True,size=(800,400))
        while True:
            event, values = consulta_fornecedor.read()
            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_fornecedor.close()
                break
            
            produto_busca = values["Id_fornecedor"].upper()
            c.execute("SELECT Id_fornecedor, Nome_fornecedor, Endereço, CEP, Cidade, Estado, País FROM fornecedores WHERE UPPER(Id_fornecedor) = ?", (produto_busca,))
            registros = c.fetchall()

            # atualizar
            tabela = consulta_fornecedor["tabela"]
            tabela.update(values=registros)
            
            
    if event == "Cadastro Transportadora":
        cadastro_layout_transportadora = [
            [sg.Text("Id_transportadora")],      
            [sg.InputText(key="Id_transportadora")],
            [sg.Text("Nome_transportadora")],      
            [sg.InputText(key="Nome_transportadora")],
            [sg.Text("Telefone")],      
            [sg.InputText(key="Telefone")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]           
        ]
        cadastro_transportadora = sg.Window("Sistema de cadastramento de transportadora",cadastro_layout_transportadora,resizable=True,size=(800,400))
        
        while True:
            event, values = cadastro_transportadora.read()
            if event == cadastro_transportadora.close() or event == "Cancelar":
                cadastro_transportadora.close()
                break
            
            c.execute("INSERT INTO transportadora (Id_transportadora, Nome_transportadora, Telefone) VALUES (?, ?, ?)", (values["Id_transportadora"], values["Nome_transportadora"], values["Telefone"]))
            conn.commit()
            
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")
    
    elif event == "Consulta Transportadora":
        consulta_layout_transportadora = [
            [sg.Text("Id_transportadora")],
            [sg.InputText(key="Id_transportadora")],
            [sg.Button("Consultar"), sg.Button("Cancelar")],
            [sg.Table(values=[], headings=["Id_transportadora","Nome_transportadora","Telefone"], display_row_numbers=False, auto_size_columns=False, num_rows=1, key="tabela")]
        ]
        consulta_transportadora = sg.Window("Consultar Transportadora",consulta_layout_transportadora,resizable=True,size=(1000,800))
        while True:
            event, values = consulta_transportadora.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_transportadora.close()
                break

                # operações no banco de dados
            produto_busca = values["Id_transportadora"].upper()
            c.execute("SELECT Id_transportadora, Nome_transportadora, Telefone FROM transportadora WHERE UPPER(Id_transportadora) = ?", (produto_busca,))
            registros = c.fetchall()

                # atualizar
            tabela = consulta_transportadora["tabela"]
            tabela.update(values=registros)
           
conn.close()       