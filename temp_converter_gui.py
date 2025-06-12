import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def c_to_f(c): return (c * 9 / 5) + 32
def f_to_c(f): return (f - 32) * 5 / 9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15
def f_to_k(f): return c_to_k(f_to_c(f))
def k_to_f(k): return c_to_f(k_to_c(k))

# Main logic
def convert_temp():
    try:
        value = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result.set(f"{value:.2f} {to_unit}")
        else:
            if from_unit == "Celsius":
                temp = c_to_f(value) if to_unit == "Fahrenheit" else c_to_k(value)
            elif from_unit == "Fahrenheit":
                temp = f_to_c(value) if to_unit == "Celsius" else f_to_k(value)
            elif from_unit == "Kelvin":
                temp = k_to_c(value) if to_unit == "Celsius" else k_to_f(value)

            result.set(f"{temp:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Setup
app = tk.Tk()
app.title("🌡️ Temperature Converter")
app.geometry("400x250")
app.resizable(False, False)

style = ttk.Style(app)
style.theme_use("clam")

# Widgets
tk.Label(app, text="Enter Temperature:", font=("Arial", 12)).pack(pady=10)
entry_temp = tk.Entry(app, font=("Arial", 12), justify='center')
entry_temp.pack()

frame = tk.Frame(app)
frame.pack(pady=10)

combo_from = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=10, font=("Arial", 11))
combo_from.set("Celsius")
combo_from.grid(row=0, column=0, padx=10)

tk.Label(frame, text="to", font=("Arial", 12)).grid(row=0, column=1)

combo_to = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=10, font=("Arial", 11))
combo_to.set("Fahrenheit")
combo_to.grid(row=0, column=2, padx=10)

tk.Button(app, text="Convert", command=convert_temp, font=("Arial", 12), bg="lightblue").pack(pady=10)

result = tk.StringVar()
tk.Label(app, textvariable=result, font=("Arial", 14, "bold"), fg="green").pack(pady=5)

app.mainloop()
