from tkinter import *
from tkinter import ttk
import sqlite3
root = Tk()
class Funcs():
    def limparTela(self):
        self.codeEntry.delete(0, END)
        self.nameEntry.delete(0, END)
        self.foneEntry.delete(0, END)
        self.endEntry.delete(0, END)
    def conectaBd(self):
        self.conn = sqlite3.connect("client.bd")
        self.cursor = self.conn.cursor()
    def desconectaBd(self):
        self.conn.close()
    def montaTab(self):
        self.conectaBd();
        print("conect to BD")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            cod INTEGER PRIMARY KEY,
            nomeCliente CHAR(40)NOT NULL,
            telefone INTEGER(20),
            end CHAR(40)
        )""")
        self.conn.commit();
        print("BD")
        self.desconectaBd()
    def variaveis(self):
        self.cod = self.codeEntry.get()
        self.name = self.nameEntry.get()
        self.fone = self.foneEntry.get()
        self.end = self.endEntry.get()
    def addClient(self):
        self.variaveis()
        self.conectaBd()
        self.cursor.execute("""INSERT INTO clientes (nomeCliente, telefone, end)
            VALUES(?,?,?)""", (self.name, self.fone, self.end))
        self.conn.commit()
        self.desconectaBd()
        self.selectList()
        self.limparTela()
    def selectList(self):
        self.listaCliente.delete(*self.listaCliente.get_children())
        self.conectaBd()
        lista = self.cursor.execute("""SELECT cod, nomeCliente, telefone, end FROM clientes
        ORDER BY nomeCliente ASC;""")
        for i in lista:
            self.listaCliente.insert("", END, values=i)
        self.desconectaBd()
    def onDoubleClick(self, event):
        self.limparTela()
        self.listaCliente.selection()

        for n in self.listaCliente.selection():
            col1, col2, col3, col4 = self.listaCliente.item(n, 'values')
            self.codeEntry.insert(END, col1)
            self.nameEntry.insert(END, col2)
            self.foneEntry.insert(END, col3)
            self.endEntry.insert(END, col4)

    def deletaCliente(self):
        self.variaveis()
        self.conectaBd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.cod))
        self.conn.commit()
        self.desconectaBd()
        self.limparTela()
        self.selectList()

    def alterarCliente(self):
        self.variaveis()
        self.conectaBd()
        self.cursor.execute("""UPDATE clientes SET nomeCliente = ?, telefone = ?, end = ?
            WHERE cod = ?""", (self.name, self.fone, self.end, self.cod))
        self.conn.commit()
        self.desconectaBd()
        self.selectList()
        self.limparTela()
class app(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets()
        self.listaFrame2()
        self.montaTab()
        self.selectList()
        root.mainloop()
    def tela(self):
        self.root.title("gp2 ads")
        self.root.configure(bg="#4F4F4F")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=1000, height=700)
        self.root.minsize(width=500, height=400)
        self.status = 0
        self.local = ""
        self.imgLogo = PhotoImage(file="banner.PNG")
    def frames_da_tela(self):
        self.frameLogo = Frame(self.root, bg="black")
        self.frameLogo.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.14)

        self.frames1 = Frame(self.root, bd=4, bg="black")  # , highlightbackground="#808080", highlightthickness=5)
        self.frames1.place(relx=0.02, rely=0.17, relwidth=0.96, relheight=0.39)

        self.frames2 = Frame(self.root, bd=4, bg="black")  # highlightbackground="#808080", highlightthickness=5)
        self.frames2.place(relx=0.02, rely=0.57, relwidth=0.96, relheight=0.42)

    def widgets(self):
        #LOGO
        self.logo = Label(self.frameLogo, image=self.imgLogo, bg="black")
        self.logo.pack(side="left")
        # CAD
        self.btNovo = Button(self.frames1, text=" NOVO ", bg="#9400D3", fg="black", command=self.addClient)
        self.btNovo.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.17)

        self.btAlterar = Button(self.frames1, text=" ALTERAR ", bg="#9932CC", fg="black", command=self.alterarCliente)
        self.btAlterar.place(relx=0.15, rely=0.05, relwidth=0.1, relheight=0.17)

        self.btLimpar = Button(self.frames1, text=" LIMPAR ", bg="#BA55D3", fg="black", command=self.limparTela)
        self.btLimpar.place(relx=0.25, rely=0.05, relwidth=0.1, relheight=0.17)

        self.btBuscar = Button(self.frames1, text=" BUSCAR ", bg="#A020F0", fg="black")
        self.btBuscar.place(relx=0.4, rely=0.05, relwidth=0.1, relheight=0.17)

        self.btApagar = Button(self.frames1, text=" APAGAR ", bg="#8B008B", fg="black", command=self.deletaCliente)
        self.btApagar.place(relx=0.5, rely=0.05, relwidth=0.1, relheight=0.17)

        self.lbCode = Label(self.frames1, text="COD", bg="black", fg="white")
        self.lbCode.place(relx=0.05, rely=0.34)
        self.codeEntry = Entry(self.frames1, bg="#4F4F4F", fg="white")
        self.codeEntry.place(relx=0.05, rely=0.45, relwidth=0.15, relheight=0.13)

        self.lbName = Label(self.frames1, text="CLIENTE", bg="black", fg="white")
        self.lbName.place(relx=0.25, rely=0.34)
        self.nameEntry = Entry(self.frames1, bg="#4F4F4F", fg="white")
        self.nameEntry.place(relx=0.25, rely=0.45, relwidth=0.65, relheight=0.13)

        self.lbFone = Label(self.frames1, text="PLACA", bg="black", fg="white")
        self.lbFone.place(relx=0.5, rely=0.65)
        self.foneEntry = Entry(self.frames1, bg="#4F4F4F", fg="white")
        self.foneEntry.place(relx=0.05, rely=0.75, relwidth=0.4, relheight=0.13)

        self.lbEnd = Label(self.frames1, text="VEICULO", bg="black", fg="white")
        self.lbEnd.place(relx=0.05, rely=0.65)
        self.endEntry = Entry(self.frames1, bg="#4F4F4F", fg="white")
        self.endEntry.place(relx=0.5, rely=0.75, relwidth=0.4, relheight=0.13)

    #LISTA DE CLIENTES
    def listaFrame2(self):
        self.listaCliente = ttk.Treeview(self.frames2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listaCliente.heading("#0", text="")
        self.listaCliente.heading("#1", text="COD")
        self.listaCliente.heading("#2", text="CLIENTE")
        self.listaCliente.heading("#3", text=" VEICULO ")
        self.listaCliente.heading("#4", text=" PLACA ")

        self.listaCliente.column("#0", width=1)
        self.listaCliente.column("#1", width=50)
        self.listaCliente.column("#2", width=125)
        self.listaCliente.column("#3", width=125)
        self.listaCliente.column("#4", width=125)
        self.listaCliente.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frames2, orient='vertical')
        self.listaCliente.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCliente.bind("<Double-1>", self.onDoubleClick)

app()