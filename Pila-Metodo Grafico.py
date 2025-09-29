import tkinter as tk
from tkinter import messagebox

class PilaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Pila (LIFO)")
        self.pila = []

        # Entrada de datos
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.push_btn = tk.Button(btn_frame, text="Push (Apilar)", command=self.push, width=15, bg="lightgreen")
        self.push_btn.grid(row=0, column=0, padx=5)

        self.pop_btn = tk.Button(btn_frame, text="Pop (Desapilar)", command=self.pop, width=15, bg="lightcoral")
        self.pop_btn.grid(row=0, column=1, padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Vaciar Pila", command=self.clear, width=15, bg="lightblue")
        self.clear_btn.grid(row=0, column=2, padx=5)

        # Área gráfica para mostrar la pila
        self.canvas = tk.Canvas(root, width=300, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.draw_pila()

    def push(self):
        valor = self.entry.get().strip()
        if valor:
            self.pila.append(valor)
            self.entry.delete(0, tk.END)
            self.draw_pila()
        else:
            messagebox.showwarning("Advertencia", "Ingrese un valor para apilar")

    def pop(self):
        if self.pila:
            valor = self.pila.pop()
            messagebox.showinfo("Elemento desapilado", f"Se desapiló: {valor}")
            self.draw_pila()
        else:
            messagebox.showerror("Error", "La pila está vacía")

    def clear(self):
        self.pila.clear()
        self.draw_pila()

    def draw_pila(self):
        self.canvas.delete("all")
        x1, y1 = 50, 350
        x2, y2 = 250, 390
        for i, elem in enumerate(reversed(self.pila)):
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightyellow")
            self.canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text=str(elem), font=("Arial", 12))
            y1 -= 40
            y2 -= 40

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGUI(root)
    root.mainloop()
