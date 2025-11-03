import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True
        else:
            return self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor == nodo.valor:
            return False
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
                return True
            return self._insertar(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
                return True
            return self._insertar(nodo.der, valor)

    def buscar(self, valor):
        n = self.raiz
        while n:
            if valor == n.valor:
                return n
            elif valor < n.valor:
                n = n.izq
            else:
                n = n.der
        return None

    
    def eliminar(self, valor, modo="predecesor"):
        self.raiz, eliminado = self._eliminar(self.raiz, valor, modo)
        new_root = self.raiz.valor if self.raiz else None
        completo = self.es_completo()
        return eliminado, new_root, completo

    def _eliminar(self, nodo, valor, modo):
        if nodo is None:
            return nodo, False
        if valor < nodo.valor:
            nodo.izq, eliminado = self._eliminar(nodo.izq, valor, modo)
            return nodo, eliminado
        elif valor > nodo.valor:
            nodo.der, eliminado = self._eliminar(nodo.der, valor, modo)
            return nodo, eliminado
        else:
           
            if nodo.izq is None:
                return nodo.der, True
            if nodo.der is None:
                return nodo.izq, True
            
            if modo == "predecesor":
                pred = nodo.izq
                while pred.der:
                    pred = pred.der
                nodo.valor = pred.valor
                nodo.izq, _ = self._eliminar(nodo.izq, pred.valor, modo)
            else:
                succ = nodo.der
                while succ.izq:
                    succ = succ.izq
                nodo.valor = succ.valor
                nodo.der, _ = self._eliminar(nodo.der, succ.valor, modo)
            return nodo, True

    def inorden(self):
        res = []
        def _in(n):
            if n:
                _in(n.izq)
                res.append(n.valor)
                _in(n.der)
        _in(self.raiz)
        return res

    def preorden(self):
        res = []
        def _pre(n):
            if n:
                res.append(n.valor)
                _pre(n.izq)
                _pre(n.der)
        _pre(self.raiz)
        return res

    def postorden(self):
        res = []
        def _post(n):
            if n:
                _post(n.izq)
                _post(n.der)
                res.append(n.valor)
        _post(self.raiz)
        return res

    def nivel_por_niveles(self):
        res = []
        if not self.raiz:
            return res
        cola = [self.raiz]
        while cola:
            n = cola.pop(0)
            res.append(n.valor)
            if n.izq:
                cola.append(n.izq)
            if n.der:
                cola.append(n.der)
        return res

    def altura(self):
        def _h(n):
            return 0 if not n else 1 + max(_h(n.izq), _h(n.der))
        return _h(self.raiz)

    def contar_nodos(self):
        def _c(n):
            return 0 if not n else 1 + _c(n.izq) + _c(n.der)
        return _c(self.raiz)

    def contar_hojas(self):
        def _h(n):
            if not n:
                return 0
            if not n.izq and not n.der:
                return 1
            return _h(n.izq) + _h(n.der)
        return _h(self.raiz)

    def es_completo(self):
        if not self.raiz:
            return True
        queue = [self.raiz]
        found_null = False
        while queue:
            node = queue.pop(0)
            if node is None:
                found_null = True
            else:
                if found_null:
                    return False
                queue.append(node.izq)
                queue.append(node.der)
        return True

    def clear(self):
        self.raiz = None


class VisualArbolApp:
    NODE_RADIUS = 22
    X_SPACING = 70
    Y_SPACING = 80
    MARGIN = 40

    def __init__(self, root):
        self.root = root
        self.root.title("Árbol Binario (Visualización Vertical)")

        self.arbol = ArbolBinario()

        main = ttk.Frame(root, padding=8)
        main.pack(fill=tk.BOTH, expand=True)

        controls = ttk.Frame(main)
        controls.grid(row=0, column=0, sticky="ns", padx=6, pady=6)

        canvas_frame = ttk.Frame(main)
        canvas_frame.grid(row=0, column=1, sticky="nsew", padx=6, pady=6)
        main.columnconfigure(1, weight=1)
        main.rowconfigure(0, weight=1)

        info_frame = ttk.Frame(main)
        info_frame.grid(row=0, column=2, sticky="ns", padx=6, pady=6)

        ttk.Label(controls, text="Valor:").pack(anchor="w")
        self.entry_val = ttk.Entry(controls, width=12)
        self.entry_val.pack(anchor="w", pady=(0, 6))

        ttk.Button(controls, text="Insertar", command=self.insertar).pack(fill="x")
        ttk.Button(controls, text="Eliminar (predecesor)", command=lambda: self.eliminar(modo="predecesor")).pack(fill="x", pady=(4, 0))
        ttk.Button(controls, text="Eliminar (sucesor)", command=lambda: self.eliminar(modo="sucesor")).pack(fill="x", pady=(4, 0))
        ttk.Button(controls, text="Buscar", command=self.buscar).pack(fill="x", pady=(4, 0))
        ttk.Separator(controls).pack(fill="x", pady=6)
        ttk.Button(controls, text="InOrden", command=self.mostrar_inorden).pack(fill="x")
        ttk.Button(controls, text="PreOrden", command=self.mostrar_preorden).pack(fill="x", pady=(4, 0))
        ttk.Button(controls, text="PostOrden", command=self.mostrar_postorden).pack(fill="x", pady=(4, 0))
        ttk.Button(controls, text="Niveles (BFS)", command=self.mostrar_niveles).pack(fill="x", pady=(4, 0))
        ttk.Separator(controls).pack(fill="x", pady=6)
        ttk.Button(controls, text="Limpiar árbol", command=self.limpiar_arbol).pack(fill="x")
        ttk.Button(controls, text="Actualizar dibujo", command=self.redibujar).pack(fill="x", pady=(4, 0))

        # ----- CANVAS -----
        self.canvas = tk.Canvas(canvas_frame, bg="white", height=600, width=900)
        hbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        vbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        vbar.grid(row=0, column=1, sticky="ns")
        hbar.grid(row=1, column=0, sticky="ew")
        canvas_frame.columnconfigure(0, weight=1)
        canvas_frame.rowconfigure(0, weight=1)

        ttk.Label(info_frame, text="Información / Recorridos:").pack(anchor="w")
        self.txt_info = scrolledtext.ScrolledText(info_frame, width=36, height=30, wrap=tk.WORD)
        self.txt_info.pack(fill="both", expand=True)

        self.node_positions = {}
        self.redibujar()

    def obtener_valor_entry(self):
        s = self.entry_val.get().strip()
        if s == "":
            messagebox.showwarning("Entrada", "Ingrese un valor (entero).")
            return None
        try:
            return int(s)
        except ValueError:
            messagebox.showwarning("Entrada", "Ingrese un número entero válido.")
            return None

    def insertar(self):
        val = self.obtener_valor_entry()
        if val is None:
            return
        if not self.arbol.insertar(val):
            messagebox.showinfo("Insertar", f"El valor {val} ya existe.")
        self.entry_val.delete(0, tk.END)
        self.redibujar()
        self.mostrar_info()

    def eliminar(self, modo="predecesor"):
        val = self.obtener_valor_entry()
        if val is None:
            return
        eliminado, nueva_raiz, es_completo = self.arbol.eliminar(val, modo=modo)
        if eliminado:
            nueva_raiz_text = str(nueva_raiz) if nueva_raiz is not None else "Árbol vacío"
            completo_text = "Sí" if es_completo else "No"
            messagebox.showinfo("Eliminar",
                                f"Valor {val} eliminado.\nNueva raíz: {nueva_raiz_text}\n¿Árbol completo?: {completo_text}")
        else:
            messagebox.showinfo("Eliminar", f"Valor {val} no encontrado.")
        self.entry_val.delete(0, tk.END)
        self.redibujar()
        self.mostrar_info()

    def buscar(self):
        val = self.obtener_valor_entry()
        if val is None:
            return
        nodo = self.arbol.buscar(val)
        if nodo:
            messagebox.showinfo("Buscar", f"Valor {val} encontrado.")
            self.redibujar(highlight=val)
        else:
            messagebox.showinfo("Buscar", f"Valor {val} no encontrado.")
        self.entry_val.delete(0, tk.END)

    def limpiar_arbol(self):
        if messagebox.askyesno("Confirmar", "¿Deseas eliminar todo el árbol?"):
            self.arbol.clear()
            self.redibujar()
            self.txt_info.delete("1.0", tk.END)

    def mostrar_inorden(self):
        seq = self.arbol.inorden()
        self.txt_info.delete("1.0", tk.END)
        self.txt_info.insert(tk.END, f"InOrden: {seq}\n")

    def mostrar_preorden(self):
        seq = self.arbol.preorden()
        self.txt_info.delete("1.0", tk.END)
        self.txt_info.insert(tk.END, f"PreOrden: {seq}\n")

    def mostrar_postorden(self):
        seq = self.arbol.postorden()
        self.txt_info.delete("1.0", tk.END)
        self.txt_info.insert(tk.END, f"PostOrden: {seq}\n")

    def mostrar_niveles(self):
        seq = self.arbol.nivel_por_niveles()
        self.txt_info.delete("1.0", tk.END)
        self.txt_info.insert(tk.END, f"Niveles: {seq}\n")

    def mostrar_info(self):
        a = self.arbol
        completo = "Sí" if a.es_completo() else "No"
        self.txt_info.insert(tk.END, f"Altura: {a.altura()} | Nodos: {a.contar_nodos()} | Hojas: {a.contar_hojas()} | Completo: {completo}\n")

    def calcular_posiciones(self):
        """Calcula posiciones verticales: raíz arriba, hijos abajo (simple recursivo con offset)."""
        self.node_positions.clear()

        def _set_pos(nodo, x, y, offset):
            if nodo is None:
                return
            self.node_positions[nodo] = (x, y)
            if nodo.izq:
                _set_pos(nodo.izq, x - offset, y + self.Y_SPACING, max(20, offset / 1.6))
            if nodo.der:
                _set_pos(nodo.der, x + offset, y + self.Y_SPACING, max(20, offset / 1.6))

        if self.arbol.raiz:
            
            canvas_width = int(self.canvas.winfo_width() or 900)
            start_x = canvas_width // 2
            _set_pos(self.arbol.raiz, start_x, self.MARGIN + 40, 220)

    def redibujar(self, highlight=None):
        self.canvas.delete("all")
        if self.arbol.es_vacio():
            self.canvas.create_text(450, 200, text="Árbol vacío", fill="#666666", font=("Arial", 16))
            
            self.txt_info.delete("1.0", tk.END)
            return
        self.calcular_posiciones()

        
        for nodo, (x, y) in self.node_positions.items():
            if nodo.izq and nodo.izq in self.node_positions:
                x2, y2 = self.node_positions[nodo.izq]
                self.canvas.create_line(x, y + self.NODE_RADIUS - 2, x2, y2 - self.NODE_RADIUS + 2, width=2)
            if nodo.der and nodo.der in self.node_positions:
                x2, y2 = self.node_positions[nodo.der]
                self.canvas.create_line(x, y + self.NODE_RADIUS - 2, x2, y2 - self.NODE_RADIUS + 2, width=2)

        # DIBUJAR NODOS
        for nodo, (x, y) in self.node_positions.items():
            r = self.NODE_RADIUS
            fill = "#4a90e2" if nodo.valor != highlight else "#3fbf7f"
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill, outline="black", width=2)
            self.canvas.create_text(x, y, text=str(nodo.valor), fill="white", font=("Arial", 10, "bold"))

        
        xs = [p[0] for p in self.node_positions.values()] or [0]
        ys = [p[1] for p in self.node_positions.values()] or [0]
        pad = 120
        left, top, right, bottom = min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad
        if right <= left:
            right = left + 900
        if bottom <= top:
            bottom = top + 600
        self.canvas.configure(scrollregion=(left, top, right, bottom))

       
        self.txt_info.delete("1.0", tk.END)
        self.mostrar_info()


def main():
    root = tk.Tk()
    app = VisualArbolApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()


