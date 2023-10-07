import tkinter as tk

def convertir():
    try:
        #obtiene el valor ingresado en el campo de entrada
        kilometros = float(entrada_Kilometros.get())

        #realiza la conversion a millas (1 kilometro = 0.6231 millas)
        millas = kilometros * 0.621371

        #Acualiza la etiqueta de resultado
        etiqueta_resultado.config(text=f"{kilometros} Kilometros son {millas} millas ")

    except ValueError:
        #manejo de errores para entrada no validado
        etiqueta_resultado.config(text="Ingrese un valor numerico válido")
        
#crear la ventana principal
ventana = tk.Tk()
ventana.title("conversor de kilometros a millas")
ventana.geometry("300x150")#Establece el tama;o de la ventana

#crear etiqueta de instruciones y colocarla en la cuadricula
etiqueta_instruccion = tk.Label(ventana, text="Ingrese la distacia en kilometros:")
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#crea campo de entrada y colocarlo en la cuadricula
entrada_Kilometros = tk.Entry(ventana)
entrada_Kilometros.grid(row=1, column=0, padx=10, pady=10)

#crea boton de conversion y colocarlo en la cuadricula
boton_convertir = tk.Button (ventana, text="convertir", command= convertir)
boton_convertir.grid(row=1,column=1 ,padx=10, pady=10)

#crea etiqueta de resultado y colocarla en la cuadricula
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#iniciar la aplicacion
ventana.mainloop() 