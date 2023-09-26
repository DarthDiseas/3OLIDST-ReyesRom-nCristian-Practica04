import tkinter as tk

app=tk.Tk()
app.title("Conversor de Temperatura")

Label= tk.Label(app, text= "Fahrenheit:")
Label.grid(row=0, column=0)

Entry=tk.Entry(app)
Entry.grid(row=0, column=1)

Button=tk.Button(app, text="Convertir a Fahrenheit")#, command=convertir_a_celsius)
Button.grid(row=0, column=2)

Label=tk.Label(app, text= "Celsius:")
Label.grid(row=1, column=0)

Entry=tk.Entry(app)
Entry.grid(row=1, column=1)

Button=tk.Button(app, text="Restablecer:")#, command=convertir_a_fahrenheit)
Button.grid(row=1, column=2)

Button=tk.Button(app, text="Restablecer")#, command=borrar)
Button.grid(row=2, column=1)

app.geometry("HOLA")

app.mainloop()
