import tkinter as tk

def convertir_a_Celsius():
    Fahrenheit=float (Entry1.get())
    Celsius= (Fahrenheit -32)*5.0/9.0
    Entry2.delete(0, tk.END)
    Entry2.insert(0, f"{Celsius:.2f}")
    
def convertir_a_Fahrenheit():
    Celsius=float (Entry2.get())
    Fahrenheit= (Celsius*9/5) +32
    Entry1.delete(0, tk.END)
    Entry1.insert(0, f"{Fahrenheit:.2f}")
    
def borrar():
    Entry1.delete(0, tk.END)
    Entry1.insert(0, "0,0")
    Entry2.delete(0, tk.END)
    Entry2.insert(0, "0,0")

app=tk.Tk()
app.title("Conversor de Temperatura")

Label1= tk.Label(app, text= "Fahrenheit:")
Label1.grid(row=0, column=0)

Entry1=tk.Entry(app)
Entry1.grid(row=0, column=1)

Button1=tk.Button(app, text="Convertir a Celsius", command=convertir_a_Celsius)
Button1.grid(row=0, column=2)

Label2=tk.Label(app, text= "Celsius:")
Label2.grid(row=1, column=0)

Entry2=tk.Entry(app)
Entry2.grid(row=1, column=1)

Button2=tk.Button(app, text="Convertir a Fahrenheit:", command=convertir_a_Fahrenheit)
Button2.grid(row=1, column=2)

Button3=tk.Button(app, text="Restablecer", command=borrar)
Button3.grid(row=2, column=1)

app.geometry()

app.mainloop()
