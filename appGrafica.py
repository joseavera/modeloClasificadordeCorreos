import tkinter as tk
from tkinter import messagebox

# 1. Función que hace el cálculo (La Lógica de la IA)
def procesar_decision():
    try:
        # Obtenemos el dato de la caja de texto
        x1 = float(entrada_dato.get())
        peso = 0.8
        bias = -0.5
        umbral = 0.5
        
        # Operación sistemática
        resultado = (x1 * peso) + bias
        
        # Función de activación
        if resultado >= umbral:
            mensaje = f"Suma: {resultado:.2f} \n¡ACTIVADA! ✅"
            color = "green"
        else:
            mensaje = f"Suma: {resultado:.2f} \nAPAGADA ❌"
            color = "red"
            
        lbl_resultado.config(text=mensaje, fg=color)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido")

# 2. Configuración de la Ventana Principal
ventana = tk.Tk()
ventana.title("Mi Primera IA - Simulador")
ventana.geometry("300x250")

# 3. Componentes de la Interfaz (Widgets)
tk.Label(ventana, text="Ingresa un valor (X1):", font=("Arial", 10)).pack(pady=10)

entrada_dato = tk.Entry(ventana)
entrada_dato.pack(pady=5)

btn_calcular = tk.Button(ventana, text="Procesar con Neurona", command=procesar_decision)
btn_calcular.pack(pady=15)

lbl_resultado = tk.Label(ventana, text="Esperando datos...", font=("Arial", 12, "bold"))
lbl_resultado.pack(pady=10)

# 4. Iniciar la aplicación
ventana.mainloop()
