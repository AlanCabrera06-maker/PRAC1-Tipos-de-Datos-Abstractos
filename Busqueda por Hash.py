import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import hashlib
import os



def generar_hash(ruta, algoritmo):
    hasher = hashlib.new(algoritmo)

    try:
        with open(ruta, "rb") as f:
            while True:
                bloque = f.read(8192)
                if not bloque:
                    break
                hasher.update(bloque)
        return hasher.hexdigest()
    except:
        return "ERROR"



class HashCarpeta:

    def __init__(self, root):
        self.root = root
        root.title("Generador Visual de HASH por Carpeta")
        root.geometry("1200x700")

        self.algoritmos = [
            "md5", "sha1", "sha256", "sha512", "sha3_256"
        ]

        
        ttk.Button(root, text="Seleccionar Carpeta",
                   command=self.cargar_carpeta).pack(pady=10)

        self.lbl_carpeta = ttk.Label(root, text="No se ha seleccionado carpeta")
        self.lbl_carpeta.pack()

        ttk.Label(root, text="Algoritmo:").pack()
        self.combo = ttk.Combobox(
            root,
            values=self.algoritmos,
            state="readonly",
            width=15
        )
        self.combo.current(0)
        self.combo.pack()

        ttk.Button(root, text="▶ Calcular HASH", command=self.procesar).pack(pady=10)

       
        columnas = ("Archivo", "Ruta", "HASH")

        self.tree = ttk.Treeview(root, columns=columnas, show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=400)

        self.scroll = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side="right", fill="y")

        
        self.total = ttk.Label(root, text="")
        self.total.pack(pady=5)

    

    def limpiar_tabla(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

  

    def cargar_carpeta(self):
        self.carpeta = filedialog.askdirectory()
        self.lbl_carpeta.config(text=self.carpeta)

   

    def procesar(self):
        if not hasattr(self, "carpeta") or not self.carpeta:
            return messagebox.showerror("Error", "Seleccione una carpeta.")

        self.limpiar_tabla()

        algoritmo = self.combo.get()

        contador = 0

        for root, _, files in os.walk(self.carpeta):
            for archivo in files:
                ruta = os.path.join(root, archivo)

                hash_archivo = generar_hash(ruta, algoritmo)

                self.tree.insert("", "end",
                    values=(archivo, ruta, hash_archivo)
                )

                contador += 1

        self.total.config(text=f" Archivos procesados: {contador}")

        messagebox.showinfo("Listo", f"Se calcularon HASH para {contador} archivos.")




if __name__ == "__main__":
    root = tk.Tk()
    HashCarpeta(root)
    root.mainloop()


