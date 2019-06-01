
from tkinter import ttk
from tkinter import *
 
class Desk:
    def _init_(self, window):
        # Initializations
       
        #ancho
        ancho = 800
       
        #alto
        alto = 600
       
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window
 
        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))
 
        #centramos el contenido
        self.wind.columnconfigure(0, weight=1)
       
        #le damos un titulo a la ventana
        self.wind.title('Aplicación con interface gráfica en Python - By Ing. Gerson Altamirano')
       
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Examen')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
       
        # creamos un etiqueta
        Label(frame, text = 'valor1: ').grid(row = 1, column = 0)
       
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
       
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'valor 2: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        Label(frame, text = 'valor 3: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 2, column = 1)
       
        #Creamos un boton para ejecutar la suma
        Button(frame, text = 'Button1', command = self.operacion).grid(row = 3, columnspan =2, sticky = W + E)
 
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
       
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
   
    # esta es la función que ejecuta la suma
    def operacion(self):
        if self.validation():
            if(self.var1 > self.var3):
                multi = int(self.var1) * int(self.var2) * int(self.var1)
                self.message['text'] = 'El var 1 es mayor al valor3 el resultado de multiplicacion de los tres valores es: {}'.format(multi)
            if(self.var1 == self.var3 and self.var2 ==  self.var3 ):
                suma = int(self.var1) + int(self.var2) + int(self.var1)
                self.message['text'] = 'Todos los valores son iguales la operacion es una suma que es: {}'.format(suma)
            if(self.var2 ==  0 ):
                if(self.var1 < self.var3):
                    resta = int(self.var3) - int(self.var1)
                    self.message['text'] = 'el valor2 es o se restara el menor al mayor que es: {}'.format(resta)
                else:
                    resta = int(self.var1) - int(self.var2)
                    self.message['text'] = 'el valor2 es o se restara el menor al mayor que es: {}'.format(resta)
        else:
            self.message['text'] = 'los campos son requeridos'
 
#validamos si estamos en la aplicación inicial
if _name_ == '_main_':
   
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
   
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana
    app = Desk(window)
 
    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()
        
    
    