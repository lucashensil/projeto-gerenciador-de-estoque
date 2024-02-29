from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import sqlite3
import pandas as pd
import time
import os

window = ctk.CTk()

class Funcs():
    def connect_db(self):
        self.conn = sqlite3.connect('estoque.db')
        self.cursor = self.conn.cursor()
    def disconnect_db(self):
        self.conn.close()
    def criar_janela(self, nome, arg=None):
        self.window = Tk.iconify(window)
        self.janela = ctk.CTkToplevel(window)

        self.janela.title(f'Gerenciador de Estoque ({str(nome)})')
        self.janela.geometry('800x700')
        self.janela.configure(bg='#000080')
        self.janela.resizable(False, False)
        self.janela.transient(self.window)
        self.janela.grab_set()
        self.criar_menu(self.janela)
        self.janela_frame1 = ctk.CTkFrame(self.janela,)
        if arg == 2:
            self.janela_frame1.place(relx=0.075, rely=0.03, relheight=0.28, relwidth=0.85)
        else:   
            self.janela_frame1.place(relx=0.075, rely=0.03, relheight=0.38, relwidth=0.85)

        if arg == 2:
            self.label_name = ctk.CTkLabel(self.janela_frame1, text='Nome', text_color='#FFFFFF', font=('Helvetica', 16, 'bold'))
            self.label_name.place(relx=0.105, rely=0.07)
            self.entry_name = ctk.CTkEntry(self.janela_frame1)
            self.entry_name.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.1)

            self.label_cod = ctk.CTkLabel(self.janela_frame1, text='Cod', text_color='#FFFFFF', font=('Helvetica', 16, 'bold'))
            self.label_cod.place(relx=0.56, rely=0.07)
            self.entry_cod_produto = ctk.CTkEntry(self.janela_frame1)
            self.entry_cod_produto.place(relx=0.55, rely=0.2, relwidth=0.08, relheight=0.1)

            self.label_categoria = ctk.CTkLabel(self.janela_frame1, text='Categoria', text_color='#FFFFFF', font=('Helvetica', 16, 'bold'))
            self.label_categoria.place(relx=0.1, rely=0.32)
            self.entry_categoria = ctk.CTkEntry(self.janela_frame1)
            self.entry_categoria.place(relx=0.1, rely=0.45, relwidth=0.4, relheight=0.1)
        else:
            self.label_name = ctk.CTkLabel(self.janela_frame1, text='Nome', text_color='#FFFFFF', font=('Helvetica', 18, 'bold'))
            self.label_name.place(relx=0.105, rely=0.1)
            self.entry_name = ctk.CTkEntry(self.janela_frame1, font=('Helvetica', 14, 'bold'))
            self.entry_name.place(relx=0.1, rely=0.2, relwidth=0.5, relheight=0.085)

            self.label_cod = ctk.CTkLabel(self.janela_frame1, text='Cod', text_color='#FFFFFF', font=('Helvetica', 18, 'bold'))
            self.label_cod.place(relx=0.755, rely=0.1)
            self.entry_cod_produto = ctk.CTkEntry(self.janela_frame1, font=('Helvetica', 14, 'bold'))
            self.entry_cod_produto.place(relx=0.75, rely=0.2, relwidth=0.08, relheight=0.085)

            self.label_categoria = ctk.CTkLabel(self.janela_frame1, text='Categoria', text_color='#FFFFFF', font=('Helvetica', 18, 'bold'))
            self.label_categoria.place(relx=0.105, rely=0.35)
            self.entry_categoria = ctk.CTkEntry(self.janela_frame1, font=('Helvetica', 14, 'bold'))
            self.entry_categoria.place(relx=0.1, rely=0.45, relwidth=0.2, relheight=0.08)
        
        if arg is None:
                self.label_qtd = ctk.CTkLabel(self.janela_frame1, text='Qtd.', text_color='#FFFFFF', font=('Helvetica', 18, 'bold'))
                self.label_qtd.place(relx=0.4, rely=0.35)
                self.entry_qtd = ctk.CTkEntry(self.janela_frame1, font=('Helvetica', 14, 'bold'))
                self.entry_qtd.place(relx=0.4, rely=0.45, relwidth=0.1, relheight=0.085)
        elif arg == 1:
                self.label_price = ctk.CTkLabel(self.janela_frame1, text='Preco', text_color='#FFFFFF', font=('Helvetica', 18, 'bold'))
                self.label_price.place(relx=0.4, rely=0.35)
                self.entry_price = ctk.CTkEntry(self.janela_frame1)
                self.entry_price.place(relx=0.4, rely=0.45, relwidth=0.1, relheight=0.085)
        else: pass

        if arg != 2:
            self.bt_return = ctk.CTkButton(self.janela_frame1, text='Voltar', fg_color='#a4161a', hover_color='#e5383b', font=('Helvetica', 12, 'bold'), command=lambda: self.fechar_max(self.janela))
            self.bt_return.place(relx=0.03, rely=0.87, relwidth=0.1, relheight=0.08)

            self.bt_clean = ctk.CTkButton(self.janela_frame1, text='Limpar', fg_color='#a4161a', hover_color='#e5383b', font=('Helvetica', 12, 'bold'), command=self.limpar_tela)
            self.bt_clean.place(relx=0.15, rely=0.87, relwidth=0.1, relheight=0.08)
        else:
            self.bt_return = ctk.CTkButton(self.janela_frame1, text='Voltar', fg_color='#a4161a', hover_color='#e5383b', font=('Helvetica', 12, 'bold'), command=lambda: self.fechar_max(self.janela))
            self.bt_return.place(relx=0.03, rely=0.87, relwidth=0.1, relheight=0.11)

            self.bt_clean = ctk.CTkButton(self.janela_frame1, text='Limpar', fg_color='#a4161a', hover_color='#e5383b', font=('Helvetica', 12, 'bold'), command=self.limpar_tela)
            self.bt_clean.place(relx=0.15, rely=0.87, relwidth=0.1, relheight=0.11)

        if arg is None:
            self.bt_adc = ctk.CTkButton(self.janela_frame1, text='Adicionar', fg_color='#25a244', hover_color='#6ede8a', font=('Helvetica', 12, 'bold'), command=lambda: (self.update(modo=1,operacao=None)))
            self.bt_adc.place(relx=0.35, rely=0.83, relwidth=0.25, relheight=0.13)
            self.bt_remove = ctk.CTkButton(self.janela_frame1, text='Retirar', fg_color='#25a244', hover_color='#6ede8a', font=('Helvetica', 12, 'bold'), command=lambda: (self.update(modo=1, operacao=1)))
            self.bt_remove.place(relx=0.68, rely=0.83, relwidth=0.25, relheight=0.13)
        elif arg == 1:
            self.bt_reg = ctk.CTkButton(self.janela_frame1, text='Registrar', fg_color='#25a244', hover_color='#6ede8a', font=('Helvetica', 12, 'bold'), command= self.reg_prod)
            self.bt_reg.place(relx=0.35, rely=0.83, relwidth=0.25, relheight=0.13)
            self.bt_remove = ctk.CTkButton(self.janela_frame1, text='Remover', fg_color='#25a244', hover_color='#6ede8a', font=('Helvetica', 12, 'bold'), command=self.delete)
            self.bt_remove.place(relx=0.68, rely=0.83, relwidth=0.25, relheight=0.13)
            self.bt_update_price = ctk.CTkButton(self.janela_frame1, text='⟳', fg_color='#25a244', hover_color='#6ede8a', font=('Helvetica', 14), command=self.update)
            self.bt_update_price.place(relx=0.52, rely=0.45, relwidth=0.07, relheight=0.085)
        else: 
            self.bt_search = ctk.CTkButton(self.janela_frame1, text='Buscar', fg_color='#25a244', hover_color='#6ede8a', command=self.buscar)
            self.bt_search.place(relx=0.7, rely=0.18, relwidth=0.2, relheight=0.13)
            self.bt_reset = ctk.CTkButton(self.janela_frame1, text='⟳', fg_color='#25a244', hover_color='#6ede8a', command=self.select_tab, font=('Helvetica', 14))
            self.bt_reset.place(relx=0.91, rely=0.18, relwidth=0.07, relheight=0.13)
            self.bt_df = ctk.CTkButton(self.janela_frame1, text='Excel', fg_color='#25a244', hover_color='#6ede8a', command=self.planilhar)
            self.bt_df.place(relx=0.8, rely=0.85, relwidth=0.15, relheight=0.13)

        #FRAME 2
        self.janela_frame2 = ctk.CTkFrame(self.janela, fg_color='#25a244')
       
        if arg == 2:
            self.style = ttk.Style()
            self.style.configure('TNotebook.Tab', font=('Helvetica', 12, ''))
            self.abas = ttk.Notebook(self.janela)
            self.aba1 = Frame(self.abas)
            self.aba2 = Frame(self.abas)

            self.abas.add(self.aba1, text='Estoque')
            self.abas.add(self.aba2, text='Movimentacoes')

            self.aba1.configure(bg='#25a244')
            self.aba2.configure(bg='#25a244')
            self.abas.place(relx=0.075, rely=0.33, relheight=0.62, relwidth=0.85)


            self.tab_treeview_estoque(self.aba1)
            self.tab_treeview_movimentacoes(self.aba2)
            
        else:
            self.janela_frame2.place(relx=0.075, rely=0.43, relheight=0.55, relwidth=0.85)
            self.tab_treeview_movimentacoes(self.janela_frame2)
            self.tab_treeview_estoque(self.janela_frame2)
        

        self.select_tab()
        self.tab_est.bind("<Double-1>", self.OnDoubleClick)
        self.janela.protocol('WM_DELETE_WINDOW', lambda: self.fechar_max(self.janela))
    def variaveis(self):
        self.cod_produto = self.entry_cod_produto.get()
        self.prod= self.entry_name.get()
        self.categoria = self.entry_categoria.get()
        self.price = None
        self.qtd = None
        self.data = time.localtime()
        self.data_atual = time.strftime('%d-%m-%y', self.data)
        self.data_hora = time.strftime('%d-%m-%y / %H:%M:%S', self.data)
        try:
            self.price = self.entry_price.get()
        except:
            self.qtd = self.entry_qtd.get()
    def table(self):
        self.connect_db()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS estoque 
                                ( cod_produto INTEGER(3) PRIMARY KEY,
                                  categoria CHAR(40),
                                  nome_produto CHAR(40) NOT NULL,
                                  preco FLOAT,
                                  qtd INTEGER
                                  
                            ); """)
        self.conn.commit()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS movimentacoes 
                                ( cod_produto INTEGER(3),
                                  categoria CHAR(40),
                                  nome_produto CHAR(40) NOT NULL,
                                  qtd INTEGER,
                                  entrada DATA,
                                  saida DATA,
                                  one DATA
                                  
                            ); """)
        self.conn.commit()
        self.disconnect_db()
    def reg_prod(self):
        self.variaveis()
        self.connect_db()
        try:
            self.cursor.execute(""" INSERT INTO estoque (cod_produto, nome_produto, categoria, preco, qtd) 
                            VALUES (?, ?, ?, ?, ?)""", (self.cod_produto, self.prod, self.categoria, self.price, 0))            
            self.conn.commit()
            self.limpar_tela()
            self.disconnect_db()
            self.select_tab()
        except:
            self.alertar(error='registro')
            self.disconnect_db()   
    def update(self, modo=None, operacao=None):
        self.variaveis()
        self.connect_db()
        try:
            if modo is None:
                self.cursor.execute("UPDATE estoque SET preco = ? WHERE cod_produto = ?", (self.price, self.cod_produto))
            elif modo == 1:
                self.cursor.execute("SELECT qtd FROM estoque WHERE cod_produto = ?", (self.cod_produto,))
                valor_anterior = self.cursor.fetchone()[0]
                if operacao is None:
                    self.novo_valor = float(valor_anterior) + float(self.qtd)
                    self.cursor.execute(""" INSERT INTO movimentacoes (cod_produto, nome_produto, categoria, qtd, entrada, one) 
                                VALUES (?, ?, ?, ?, ?, ?)""", (self.cod_produto, self.prod, self.categoria, self.qtd, self.data_atual, self.data_hora))
                else:
                    self.novo_valor = float(valor_anterior) - float(self.qtd)
                    self.qtd = 0 - int(self.qtd)
                    self.cursor.execute(""" INSERT INTO movimentacoes (cod_produto, nome_produto, categoria, qtd, saida, one) 
                                VALUES (?, ?, ?, ?, ?, ?)""", (self.cod_produto, self.prod, self.categoria, self.qtd, self.data_atual, self.data_hora))
                self.cursor.execute("UPDATE estoque SET qtd = ? WHERE cod_produto = ?", (self.novo_valor, self.cod_produto))
            self.conn.commit()
            self.disconnect_db()
            self.select_tab()
            self.limpar_tela()
        except:
            self.alertar(error='adicionar')
            self.disconnect_db()   
    def select_tab(self):
        self.connect_db()
        
        self.tab_est.delete(*self.tab_est.get_children())
        lista = self.cursor.execute(""" SELECT 
                                        cod_produto, 
                                        categoria, 
                                        nome_produto,
                                        qtd,
                                        preco
                                        FROM estoque;
                                        """)
        for i in lista:
            self.tab_est.insert('', END, values=i)
    
        self.tab_mov.delete(*self.tab_mov.get_children())
        lista = self.cursor.execute(""" SELECT 
                                        cod_produto, 
                                        categoria, 
                                        nome_produto,
                                        qtd,
                                        IFNULL(entrada,'---'),
                                        IFNULL(saida,'---')
                                        FROM movimentacoes
                                        ORDER BY one DESC;
                                        """)
        for i in lista:
                self.tab_mov.insert('', END, values=i)
        self.conn.commit()
        self.disconnect_db()
    def fechar_max(self, janela):
        self.janela = janela
        self.janela.destroy()
        self.window = Tk.deiconify(window)        
    def criar_menu(self, janela):
        self.janela = janela
        
        menubar =   Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0, foreground='#25a244')
        filemenu2 = Menu(menubar, tearoff=0, foreground='#b32020')

        menubar.add_cascade(label='Opcoes', menu=filemenu)
        menubar.add_cascade(label='Ajuda', menu=filemenu2)  

        filemenu.add_command(label='Gerar Planilha', command=self.planilhar)
        
        filemenu2.add_command(label='Instrucoes', command=self.help_window)
        filemenu2.add_command(label='Sair', command=lambda: (window.destroy()))
    def limpar_tela(self):
        try:
            self.entry_cod_produto.delete(0, END)
            self.entry_name.delete(0, END)
            self.entry_categoria.delete(0, END)
            try:
                self.entry_price.delete(0, END)
            except:
                self.entry_qtd.delete(0, END)
        except:
            self.entry_cod_produto.delete(0, END)
            self.entry_name.delete(0, END)
            self.entry_categoria.delete(0, END)
    def OnDoubleClick(self, event):
        self.limpar_tela()
        self.tab_est.selection()
        self.tab_mov.selection()

        for n in self.tab_est.selection():
            col1, col2, col3, col4, col5 = self.tab_est.item(n, "values")
            self.entry_cod_produto.insert(END, col1)
            self.entry_categoria.insert(END, col2)
            self.entry_name.insert(END, col3)

            try:
                self.entry_price.insert(END, col5)
            except:
                pass
        for n in self.tab_mov.selection():
            col1, col2, col3, col4, col5, col6 = self.tab_est.item(n, "values")
            self.entry_cod_produto.insert(END, col1)
            self.entry_categoria.insert(END, col2)
            self.entry_name.insert(END, col3)
    def delete(self):
        self.variaveis()
        self.connect_db()
        msg = messagebox.askokcancel('Exluir Registro', 'O Registro será exluido',
                                        icon='warning')
        if msg is True:
            self.cursor.execute(""" DELETE FROM estoque WHERE cod_produto = ? """, (self.cod_produto,))
            self.cursor.execute(""" DELETE FROM movimentacoes WHERE cod_produto = ? """, (self.cod_produto,))
            self.conn.commit()
            self.disconnect_db()
            self.limpar_tela()
            self.select_tab()
    def buscar(self):
        self.connect_db()
        self.tab_est.delete(*self.tab_est.get_children())
        self.tab_mov.delete(*self.tab_mov.get_children())

        #Busca na tabela estoque
        if self.entry_name.get() != '':
            self.entry_name.insert(END, '%')
            nome = self.entry_name.get()
            self.cursor.execute("SELECT cod_produto, categoria, nome_produto, qtd, preco FROM estoque WHERE nome_produto LIKE '%s'" % nome)
        else: pass
        
        if self.entry_categoria.get() != '':
            self.entry_categoria.insert(END, '%')
            categoria = self.entry_categoria.get()
            self.cursor.execute("SELECT cod_produto, categoria, nome_produto, qtd, preco FROM estoque WHERE categoria LIKE '%s'" % categoria)
        else: pass

        if self.entry_cod_produto.get() != '':
            self.entry_cod_produto.insert(END, '%')
            cod_produto = self.entry_cod_produto.get()
            self.cursor.execute("SELECT cod_produto, categoria, nome_produto, qtd, preco FROM estoque WHERE cod_produto LIKE '%s'" % cod_produto)
        else: pass
        
        resultados = self.cursor.fetchall()
        for i in resultados:
            self.tab_est.insert('', END, values=i)

        #Busca na tabela movimentacoes
        if self.entry_name.get() != '':
            self.entry_name.insert(END, '%')
            nome = self.entry_name.get()
            self.cursor.execute("SELECT cod_produto, categoria, nome_produto, qtd, entrada, saida FROM movimentacoes WHERE nome_produto LIKE '%s'" % nome)
        else: pass
        
        if self.entry_categoria.get() != '':
            self.entry_categoria.insert(END, '%')
            categoria = self.entry_categoria.get()
            self.cursor.execute("SELECT cod_produto, categoria, nome_produto, qtd, entrada, saida FROM movimentacoes WHERE categoria LIKE '%s'" % categoria)
        else: pass

        if self.entry_cod_produto.get() != '':
            self.entry_cod_produto.insert(END, '%')
            cod_produto = self.entry_cod_produto.get()
            self.cursor.execute("SELECT cod_produto, categoria, nome_produto, qtd, entrada, saida FROM movimentacoes WHERE cod_produto LIKE '%s'" % cod_produto)
        else: pass
        
        resultados2 = self.cursor.fetchall()
        for i in resultados2:
            self.tab_mov.insert('', END, values=i)

        self.limpar_tela()
        self.disconnect_db()
    def tab_treeview_estoque(self, frame):
        self.style = ttk.Style()
        self.style.configure('Treeview', font=('Helvetica', 12, ''))
        self.style.configure('Treeview.Heading', font=('Helvetica', 12, ''))

        self.tab_est = ttk.Treeview(frame, height=5, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.tab_est.heading('#0', text='')
        self.tab_est.column('#0', width=1)
        self.tab_est.heading('#1', text='Codigo')
        self.tab_est.column('#1', width=25)
        self.tab_est.heading('#2', text='Categoria')
        self.tab_est.column('#2', width=75)
        self.tab_est.heading('#3', text='Produto')
        self.tab_est.column('#3', width=75)
        self.tab_est.heading('#4', text='Qtd.')
        self.tab_est.column('#4', width=25)
        self.tab_est.heading('#5', text='Preco')
        self.tab_est.column('#5', width=25)
        
        self.tab_est.place(relx=0.01, rely=0.01, relheight=0.97, relwidth=0.95)
        self.scrool = ttk.Scrollbar(frame, orient='vertical')
        self.tab_est.configure(yscrollcommand=self.scrool.set)
        self.scrool.place(relx=0.965, rely=0.01, relheight=0.95, relwidth=0.025)
    def tab_treeview_movimentacoes(self, frame):
        self.tab_mov = ttk.Treeview(frame, height=6, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        self.tab_mov.heading('#0', text='')
        self.tab_mov.column('#0', width=1)
        self.tab_mov.heading('#1', text='Codigo')
        self.tab_mov.column('#1', width=25)
        self.tab_mov.heading('#2', text='Categoria')
        self.tab_mov.column('#2', width=75)
        self.tab_mov.heading('#3', text='Produto')
        self.tab_mov.column('#3', width=50)
        self.tab_mov.heading('#4', text='Qtd.')
        self.tab_mov.column('#4', width=25)
        self.tab_mov.heading('#5', text='Entrada')
        self.tab_mov.column('#5', width=25)
        self.tab_mov.heading('#6', text='Saida')
        self.tab_mov.column('#6', width=25)

        self.tab_mov.place(relx=0.01, rely=0.01, relheight=0.97, relwidth=0.95)
        self.scrool = ttk.Scrollbar(frame, orient='vertical')
        self.tab_mov.configure(yscrollcommand=self.scrool.set)
        self.scrool.place(relx=0.965, rely=0.01, relheight=0.95, relwidth=0.025)
    def planilhar(self):
        self.data = time.localtime()
        self.data_atual = time.strftime('%d-%m-%y', self.data)
        self.connect_db()
        self.dados = "SELECT * FROM estoque"
        self.df = pd.read_sql_query(self.dados, self.conn)
        self.disconnect_db()
        self.df.to_csv('CSV_Estoque.csv')
        self.df = pd.read_csv('CSV_Estoque.csv', decimal=',')
        self.pasta_selecionada = filedialog.askdirectory(title='Selecione a Pasta para salvar')
        self.df.to_excel(f'{self.pasta_selecionada}/Planilha_Estoque_{self.data_atual}.xlsx', index=False)
        os.remove('CSV_Estoque.csv')
        self.alertar(alert='excel')
    def alertar(self, error=None, alert=None):
        if error == 'registro':
            messagebox.showerror("Erro", "Erro ao Registrar Produto, por favor, preencha os campos corretamente, lembre-se o ID não pode se repetir")
            self.limpar_tela()
        if error =='adicionar':
            messagebox.showerror("Erro", "Erro ao Adicionar ou Remover Produto, por favor, preencha os campos corretamente")
            self.limpar_tela()
        if alert =='excel':
            messagebox.showinfo('Alerta', 'O arquivo foi salvo na Pasta Selecionada')




class App(Funcs):
    def __init__(self):
        self.window = window
        ctk.set_appearance_mode("dark")
        self.tela()
        self.frames()
        self.widgets()
        self.Menu()
        self.table()
        window.mainloop()
    def tela(self):
        self.window.title('Gerenciador de Estoque')
        self.window.geometry('500x680')
        self.window.resizable(False, False) 
    def frames(self):
        self.frame1 = ctk.CTkFrame(self.window)
        self.frame1.place(relx=0.075, rely=0.03, relheight=0.38, relwidth=0.85)

        self.frame2 = ctk.CTkFrame(self.window)
        self.frame2.place(relx=0.075, rely=0.43, relheight=0.55, relwidth=0.85)
    def widgets(self):
        self.label1 = ctk.CTkLabel(self.frame1, text='Gerenciador de Estoque', font=('Helvetica', 22, 'bold'), text_color='#25a244')
        self.label1.place(relx=0.18, rely=0.4)

        self.bt_add = ctk.CTkButton(self.frame2, text='Adicionar', command=self.add_window, fg_color='#25a244', hover_color='#6ede8a')
        self.bt_add.place(relx=0.335, rely=0.15, relwidth=0.35, relheight=0.1)

        self.bt_regis = ctk.CTkButton(self.frame2, text='Registrar', command=self.reg_window, fg_color='#25a244', hover_color='#6ede8a')
        self.bt_regis.place(relx=0.335, rely=0.35, relwidth=0.35, relheight=0.1)

        self.bt_visu = ctk.CTkButton(self.frame2, text='Visuzalizar', command=self.visu_window, fg_color='#25a244', hover_color='#6ede8a')
        self.bt_visu.place(relx=0.335, rely=0.55, relwidth=0.35, relheight=0.1)

        self.ajuda = ctk.CTkButton(self.frame2, text='Ajuda', command=self.help_window, fg_color='#25a244', hover_color='#6ede8a')
        self.ajuda.place(relx=0.335, rely=0.75, relwidth=0.35, relheight=0.1)
    def reg_window(self):
        self.criar_janela(arg=1, nome='Registrar')
    def add_window(self):
        self.criar_janela(arg=None, nome='Adicionar')
    def visu_window(self):
        self.criar_janela(arg=2, nome='Visualizar')
    def help_window(self):

        self.window = Tk.iconify(window)
        self.janela = ctk.CTkToplevel(window)
        self.criar_menu(self.janela)

        self.janela.title(f'Gerenciador de Estoque (Ajuda)')
        self.janela.geometry('800x700')
        self.janela.configure(bg='#000080')
        self.janela.resizable(False, False)
        self.janela.transient(self.window)
        self.janela.grab_set()
        self.janela.protocol('WM_DELETE_WINDOW', lambda: self.fechar_max(self.janela))

        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Helvetica', 12, ''))
        self.abas = ttk.Notebook(self.janela)
        self.aba1 = Frame(self.abas, background='#2b2b2b')
        self.aba2 = Frame(self.abas, background='#2b2b2b')

        self.abas.add(self.aba1, text='Sobre Abas')
        self.abas.add(self.aba2, text='Instrucoes')
        self.abas.place(relx=0.02, rely=0.01, relheight=0.96, relwidth=0.96)

        sobre = '''




        ADICIONAR: Esta função permite adicionar ou retirar produtos do estoque rapidamente. 
        Basta inserir a quantidade desejada de produtos a serem adicionados ou removidos. 
        Certifique-se de verificar a disponibilidade do produto antes de realizar qualquer modificação.

        
        REGISTRAR: A função de registro é essencial para manter um controle preciso do estoque. 
        Aqui, você pode registrar a entrada ou saída de produtos, além de poder modificar o preço 
        de um produto, se necessário. 
        Remover um produto resultará na exclusão completa de seus registros do sistema.
        obs: ⟳  ao clicar altera o preco

        
        VISUALIZAR: Esta função oferece uma visão abrangente do estoque permitindo visualizar todos 
        os produtos disponíveis, juntamente com suas quantidades e movimentações de entrada e 
        saída. Além disso, você pode acessar uma planilha detalhada do estoque para uma análise mais 
        aprofundada. 
        Utilize esta função para tomar decisões informadas sobre o gerenciamento do estoque.

        
        AJUDA: Aba atual. Resumo de as outras abas e informações uteis para a utilizacao  
        '''

        self.label_sobre = ctk.CTkLabel(self.aba1, fg_color='#2b2b2b', text=sobre, font=('Helvetica', 16, 'bold'), anchor='nw', justify='left')
        self.label_sobre.place(relx=0, rely=0.03, relheight=0.9, relwidth=1,)

        instrucoes = """
        Este gerenciador funciona de forma simples, qualquer problema que acontecer apenas o 
        reinicie que voltara ao normal.

        
        Detalhes Importantes: 

        Para registrar um produto, informe de forma correta o nome, categoria e codigo. 
        Alteracoes nao serao possiveis nestes campos.
        Sao permitidos repeticoes nos campos de nome e categoria, 
        porem ao tentar registrar produtos com dois codigos iguais, um erro acontecera.

        
        Ao remover um produto do estoque, todas as informacoes do mesmo sumira no 
        historico de movimentacoes.

        
        Para buscar um produto ou categoria, preencha apenas os campos necessarios 
        na aba de visualizar e aperte o botao 'Buscar'.
        Apos o uso, aperte o botao ao lado para reiniciar a visualizacao.

        Em todas as abas ha a funcionalidade de clique duplo, utilize para pegar as
        informacoes de forma mais rapida.
        Ha tambem o botao 'limpar', o utilize para limpar a tela.

        Caso deseje gerar uma planilha excel, havera um botao em visualizar e em opcoes.
        """

        self.label_instrucoes = ctk.CTkLabel(self.aba2, fg_color='#2b2b2b', text=instrucoes, font=('Helvetica', 16, 'bold'), anchor='nw', justify='left')
        self.label_instrucoes.place(relx=0, rely=0.03, relheight=0.9, relwidth=1,)

        self.bt_voltar = ctk.CTkButton(self.abas, text='Voltar', fg_color='#a4161a', hover_color='#e5383b', font=('Helvetica', 12, 'bold'), command=lambda: self.fechar_max(self.janela), bg_color='#a4161a')
        self.bt_voltar.place(relx=0.03, rely=0.9, relwidth=0.1, relheight=0.05)
    def Menu(self):
        self.criar_menu(janela=self.window)
 
App()