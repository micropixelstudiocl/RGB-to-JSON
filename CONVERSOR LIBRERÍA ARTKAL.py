import os
import customtkinter as ctk
from tkinter import messagebox, filedialog, Menu
import json

# Función para agregar colores al listado
def add_color():
    try:
        r = int(entry_r.get())
        g = int(entry_g.get())
        b = int(entry_b.get())
        color_name = entry_name.get()

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("Los valores RGB deben estar entre 0 y 255.")
        if not color_name.strip():
            raise ValueError("El nombre del color no puede estar vacío.")

        color_data = {"name": color_name, "rgb": {"r": r, "g": g, "b": b}}
        colors.append(color_data)
        update_listbox()
        entry_r.delete(0, "end")
        entry_g.delete(0, "end")
        entry_b.delete(0, "end")
        entry_name.delete(0, "end")
        preview_color(r, g, b)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Función para actualizar la lista de colores
# Función para actualizar la lista de colores
def update_listbox():
    listbox_colors.configure(state="normal")  # Habilitar edición temporal
    listbox_colors.delete("1.0", "end")  # Limpiar el contenido actual
    for index, color in enumerate(colors):
        r, g, b = color["rgb"]["r"], color["rgb"]["g"], color["rgb"]["b"]
        listbox_colors.insert("end", f"{index + 1}. {color['name']} - RGB({r}, {g}, {b})\n")
    listbox_colors.configure(state="disabled")  # Volver a deshabilitar

# Función para manejar el evento de la tecla Enter
def on_enter_key(event):
    add_color()

# Función para actualizar la vista previa del color
def preview_color(r, g, b):
    color_hex = f"#{r:02x}{g:02x}{b:02x}"
    preview_box.configure(fg_color=color_hex)

# Función para exportar colores a JSON
def export_to_json():
    if not colors:
        messagebox.showerror("Error", "No hay colores para exportar.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as json_file:
            json.dump(colors, json_file, indent=4)
        messagebox.showinfo("Éxito", f"Paleta exportada a {file_path}")

# Función para borrar la lista de colores
def clear_list():
    if not colors:
        messagebox.showinfo("Información", "La lista ya está vacía.")
        return
    colors.clear()
    update_listbox()
    messagebox.showinfo("Éxito", "Lista de colores borrada.")

# Función para cerrar la aplicación
def quit_program():
    root.quit()

# Función para habilitar edición en la lista
def enable_edit():
    listbox_colors.configure(state="normal")

# Función para guardar cambios tras editar
def save_changes():
    try:
        edited_lines = listbox_colors.get(0, "end")
        updated_colors = []
        for line in edited_lines:
            if line.strip():
                parts = line.split("-")
                name_part = parts[0].strip()
                rgb_part = parts[1].strip().replace("RGB(", "").replace(")", "")
                name = name_part.split(".")[1].strip()
                r, g, b = map(int, rgb_part.split(","))
                updated_colors.append({"name": name, "rgb": {"r": r, "g": g, "b": b}})
        global colors
        colors = updated_colors
        listbox_colors.configure(state="disabled")
        messagebox.showinfo("Éxito", "Cambios guardados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar cambios: {e}")

# Crear ventana principal
ctk.set_appearance_mode("dark")  # Opciones: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opciones: "blue", "dark-blue", "green"

root = ctk.CTk()
root.title("Creador de Paleta Artkal")
root.geometry("600x700")

# Lista para almacenar colores
colors = []

# Barra de menú utilizando tkinter
menu_bar = Menu(root)
menu_file = Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Exportar a JSON", command=export_to_json)
menu_file.add_command(label="Borrar lista", command=clear_list)
menu_file.add_separator()
menu_file.add_command(label="Salir", command=quit_program)
menu_bar.add_cascade(label="Archivo", menu=menu_file)

menu_edit = Menu(menu_bar, tearoff=0)
menu_edit.add_command(label="Habilitar Edición", command=enable_edit)
menu_edit.add_command(label="Guardar Cambios", command=save_changes)
menu_bar.add_cascade(label="Edición", menu=menu_edit)

root.config(menu=menu_bar)

# Entradas para valores RGB
frame_inputs = ctk.CTkFrame(root)
frame_inputs.pack(pady=10, padx=10)

ctk.CTkLabel(frame_inputs, text="R:").grid(row=0, column=0, padx=5)
entry_r = ctk.CTkEntry(frame_inputs, width=50)
entry_r.grid(row=0, column=1, padx=5)

ctk.CTkLabel(frame_inputs, text="G:").grid(row=0, column=2, padx=5)
entry_g = ctk.CTkEntry(frame_inputs, width=50)
entry_g.grid(row=0, column=3, padx=5)

ctk.CTkLabel(frame_inputs, text="B:").grid(row=0, column=4, padx=5)
entry_b = ctk.CTkEntry(frame_inputs, width=50)
entry_b.grid(row=0, column=5, padx=5)

ctk.CTkLabel(frame_inputs, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
entry_name = ctk.CTkEntry(frame_inputs, width=200)
entry_name.grid(row=1, column=1, columnspan=5, padx=5, pady=5)

# Botón para agregar color
btn_add = ctk.CTkButton(root, text="Agregar Color", command=add_color)
btn_add.pack(pady=10)

# Vista previa del color
preview_box = ctk.CTkLabel(root, text="Vista previa", width=300, height=50, fg_color="white")
preview_box.pack(pady=10)

# Listado de colores añadidos
listbox_colors = ctk.CTkTextbox(root, width=500, height=300)
listbox_colors.pack(pady=10)
listbox_colors.configure(state="disabled")

# Botones para salir
btn_quit = ctk.CTkButton(root, text="Salir", command=quit_program)
btn_quit.pack(pady=10)

# Iniciar la aplicación
root.mainloop()