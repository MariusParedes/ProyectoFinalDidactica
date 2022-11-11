#from tkinter import filedialog
from tkinter import *
from tkinter import messagebox, ttk

#from tkinter import font
#from turtle import width

dicCursos = {}



'''MENU PRINCIPAL / PANTALLA 1 ++++++++++++++++++++++++++++++++++++++'''
class MenuPrincipal():
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Proyecto Final")
        self.ventana.geometry('600x600')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()
        
    def VentanaFrame(self):
        self.frame = Frame(height=500, width=500)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=50, pady=50)
        Label(self.frame, text="Menú Principal ", font=('Segoe UI',20), fg='#FDFEFE', bg='#00747C', width=60).place(x=250, y=50, anchor="center")
        Label(self.frame, text="Didactica de la Programación", font=('Segoe UI',15), fg='#FDFEFE', bg='#00747C', width=50).place(x=250, y=90, anchor="center")
        Label(self.frame, text="", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=69, height=18).place(x=250, y=340, anchor="center")
        Button(self.frame, text="Gestion de vuelos", command=self.btnGestionar , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=20).place(x=375, y=300, anchor="center")    
        Button(self.frame, text="Listar Vuelos", command=self.btnlistarVuelos , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=20).place(x=375, y=210, anchor="center")
        Button(self.frame, text="Salir", command=self.salir , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=20).place(x=375, y=400, anchor="center")
        
        self.frame.mainloop()
    
    

    def salir(self):
        self.ventana.destroy()
    def btnGestionar(self):
        self.ventana.destroy()
        Vuelos()
    def btnlistarVuelos(self):
        self.ventana.destroy()
        ListarVuelos()


class Vuelos():

    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Proyecto Final Didactica")
        self.ventana.geometry('750x400')
        #self.ventana.configure(bg='#202022')
        self.VentanaFrame()
        
    
    def VentanaFrame(self):

                
        def btnAgregar():
            valoresInd = [ nombreValor.get(), apellidovalor.get(), direccionvalor.get(), vueloValor.get(), asientoValor.get(), nivelValor.get()]  
            if valoresInd[1] =="":
                messagebox.showinfo(message="Error, datos insuficientes",title="Informacion")
                self.btnsalir()
            else:
                dicCursos[codigo.get()] = valoresInd  
                print("Agregando Vuelo")
                messagebox.showinfo(message="El vuelo se a cargado", title="Pasajero Creado")
                #ListarVuelos()
                self.btnsalir()            
        
        self.frame = Frame(height=390, width=500)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=10, pady=10)
        
        Label(self.frame, text="Registro de Boleto de viaje", font=('Segoe UI',15), fg='#00747C', bg='#202022', width=60).place(x=250, y=20, anchor="center")
        
        Label(self.frame, text="Código: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=60, anchor="center")
        Label(self.frame, text="Nombre: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=100, anchor="center")
        Label(self.frame, text="Apellido: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=140, anchor="center")
        Label(self.frame, text="Dirección: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=180, anchor="center")
        Label(self.frame, text="Vuelo: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=220, anchor="center")
        Label(self.frame, text="Asiento: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=260, anchor="center")
        Label(self.frame, text="Nivel: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=300, anchor="center")
        
        codigo = StringVar()
        nombreValor = StringVar()
        apellidovalor = StringVar()
        direccionvalor = StringVar()
        vueloValor = StringVar()
        asientoValor = StringVar()
        nivelValor = StringVar()

        boxCodigo= Entry(self.frame, textvariable=codigo, font=('Segoe UI',10), fg='#000000', width=40).place(x=300, y=60, anchor="center")
        boxNombre = Entry(self.frame, textvariable=nombreValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=100, anchor="center")
        boxApellido = Entry(self.frame, textvariable=apellidovalor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=140, anchor="center")
        boxDireccion = Entry(self.frame, textvariable=direccionvalor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=180, anchor="center")
        boxValor = Entry(self.frame, textvariable=vueloValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=220, anchor="center")
        boxAsiento = Entry(self.frame, textvariable=asientoValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=260, anchor="center")
        boxNivel = Entry(self.frame, textvariable=nivelValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=300, anchor="center")

        Button(self.frame, text="Cancelar", command=self.btnsalir , font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=435, y=360, anchor="center")
        Button(self.frame, text="Agregar", command=btnAgregar, font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=300, y=360, anchor="center")
  
        self.frame.mainloop()

    def btnsalir(self):   
        self.ventana.destroy()
        MenuPrincipal()
        


#
class ListarVuelos():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(1,1)
        self.ventana.title("Lista de Viajeros Asignados")
        
        self.ventana.geometry('750x400')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()


   
        
    def VentanaFrame(self):
        self.frame = Frame(height=390, width=600)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=10, pady=10)
        
        Label(self.frame, text="Listado de Viajeros", font=('Segoe UI',15), fg='#00747C', bg='#202022', width=60).place(x=270, y=20, anchor="center")
        
        tabla = ttk.Treeview(self.frame, columns=("col1","col2", "col3", "col4", "col5", "col6"))
        tabla.place(x=250, y=160, anchor="center")
        
        style = ttk.Style()
        style.configure(
            'Treeview',
            background = 'white',
            foreground = '#202022',
            rowheight = 20,
            fielbackground = 'silver'
        )
        style.map(
            'Treeview',
            background = [('selected', '#00747C')]
        )
        
        tabla.column("#0",width=55)
        tabla.column("col1",width=110, anchor=CENTER)
        tabla.column("col2",width=80, anchor=CENTER)
        tabla.column("col3",width=60, anchor=CENTER)
        tabla.column("col4",width=70, anchor=CENTER)
        tabla.column("col5",width=60, anchor=CENTER)
        tabla.column("col6",width=50, anchor=CENTER)

        tabla.heading("#0", text="Codigo", anchor=CENTER)
        tabla.heading("col1", text="Nombre", anchor=CENTER)
        tabla.heading("col2", text="Apellido", anchor=CENTER)
        tabla.heading("col3", text="Direccion", anchor=CENTER)
        tabla.heading("col4", text="Vuelo", anchor=CENTER)
        tabla.heading("col5", text="Asiento", anchor=CENTER)
        tabla.heading("col6", text="Nivel", anchor=CENTER)
        
        for c in dicCursos:
            valores = dicCursos[c]
            tabla.insert("",END,text=c, values=(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5]))

        Button(self.frame, text="Regresar", command=self.btnsalir , font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=435, y=360, anchor="center")
        self.frame.mainloop()
        
    
    def btnsalir(self):
        self.ventana.destroy()
        MenuPrincipal()
# 

        
MenuPrincipal()