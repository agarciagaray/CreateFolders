import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import re
from pathlib import Path

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class FolderStructureGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Estructura de Carpetas")
        self.root.geometry("900x700")
        
        # Centrar la ventana en la pantalla
        self.center_window()
        
        # Variables
        self.txt_file_path = ctk.StringVar()
        self.output_directory = ctk.StringVar()
        self.output_directory.set(os.getcwd())  # Directorio actual por defecto
        
        self.setup_ui()
    
    def center_window(self):
        """Centra la ventana en la pantalla manteniendo el tamaño original"""
        # Usar las dimensiones fijas que ya establecimos
        window_width = 900
        window_height = 700
            
        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calcular posición para centrar
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        # Establecer la geometría con la posición centrada
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
    def setup_ui(self):
        # Frame principal con padding
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título principal
        title_label = ctk.CTkLabel(
            main_frame, 
            text="Generador de Estructura de Carpetas", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=(20, 30))
        
        # Frame superior para controles
        controls_frame = ctk.CTkFrame(main_frame)
        controls_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Sección de archivo de entrada
        file_label = ctk.CTkLabel(
            controls_frame, 
            text="Archivo de entrada (.txt):", 
            font=ctk.CTkFont(size=14, weight="bold")
        )
        file_label.pack(anchor="w", padx=20, pady=(20, 5))
        
        file_frame = ctk.CTkFrame(controls_frame)
        file_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        self.file_entry = ctk.CTkEntry(
            file_frame, 
            textvariable=self.txt_file_path,
            placeholder_text="Selecciona el archivo .txt con la estructura...",
            height=35
        )
        self.file_entry.pack(side="left", fill="x", expand=True, padx=(15, 10), pady=15)
        
        browse_file_btn = ctk.CTkButton(
            file_frame, 
            text="Examinar", 
            command=self.browse_file,
            width=100,
            height=35
        )
        browse_file_btn.pack(side="right", padx=(0, 15), pady=15)
        
        # Sección de directorio de salida
        dir_label = ctk.CTkLabel(
            controls_frame, 
            text="Directorio de salida:", 
            font=ctk.CTkFont(size=14, weight="bold")
        )
        dir_label.pack(anchor="w", padx=20, pady=(0, 5))
        
        dir_frame = ctk.CTkFrame(controls_frame)
        dir_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        self.dir_entry = ctk.CTkEntry(
            dir_frame, 
            textvariable=self.output_directory,
            placeholder_text="Directorio donde se crearán las carpetas...",
            height=35
        )
        self.dir_entry.pack(side="left", fill="x", expand=True, padx=(15, 10), pady=15)
        
        browse_dir_btn = ctk.CTkButton(
            dir_frame, 
            text="Examinar", 
            command=self.browse_directory,
            width=100,
            height=35
        )
        browse_dir_btn.pack(side="right", padx=(0, 15), pady=15)
        
        # Botones de acción
        buttons_frame = ctk.CTkFrame(controls_frame)
        buttons_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Frame para botones de la izquierda
        left_buttons_frame = ctk.CTkFrame(buttons_frame, fg_color="transparent")
        left_buttons_frame.pack(side="left", padx=15, pady=15)
        
        preview_btn = ctk.CTkButton(
            left_buttons_frame, 
            text="🔍 Vista Previa", 
            command=self.show_preview,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        preview_btn.pack(side="left", padx=(0, 10))
        
        generate_btn = ctk.CTkButton(
            left_buttons_frame, 
            text="📁 Generar Carpetas", 
            command=self.generate_folders,
            width=170,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        generate_btn.pack(side="left")
        
        # Frame para controles de la derecha
        right_controls_frame = ctk.CTkFrame(buttons_frame, fg_color="transparent")
        right_controls_frame.pack(side="right", padx=15, pady=15)
        
        # Selector de tema
        theme_label = ctk.CTkLabel(
            right_controls_frame, 
            text="Tema:",
            font=ctk.CTkFont(size=12)
        )
        theme_label.pack(side="left", padx=(0, 5))
        
        self.theme_var = ctk.StringVar(value="System")
        theme_menu = ctk.CTkOptionMenu(
            right_controls_frame,
            values=["Light", "Dark", "System"],
            command=self.change_theme,
            variable=self.theme_var,
            width=100
        )
        theme_menu.pack(side="left", padx=(0, 10))
        
        # Botón de salir
        exit_btn = ctk.CTkButton(
            right_controls_frame, 
            text="❌ Salir", 
            command=self.exit_application,
            width=80,
            height=35,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"),
            hover_color=("gray80", "gray20")
        )
        exit_btn.pack(side="right")
        
        # Área de vista previa
        preview_frame = ctk.CTkFrame(main_frame)
        preview_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        preview_label = ctk.CTkLabel(
            preview_frame, 
            text="Vista Previa y Resultados", 
            font=ctk.CTkFont(size=16, weight="bold")
        )
        preview_label.pack(pady=(15, 10))
        
        # Área de texto con scroll
        self.preview_text = ctk.CTkTextbox(
            preview_frame,
            font=ctk.CTkFont(family="Consolas", size=12),
            wrap="word"
        )
        self.preview_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Barra de estado
        self.status_frame = ctk.CTkFrame(main_frame)
        self.status_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="✅ Listo para generar estructura de carpetas",
            font=ctk.CTkFont(size=12),
            anchor="w"
        )
        self.status_label.pack(fill="x", padx=15, pady=10)
    
    def change_theme(self, new_theme):
        """Cambia el tema de la aplicación"""
        ctk.set_appearance_mode(new_theme)
        
    def exit_application(self):
        """Cierra la aplicación"""
        self.root.quit()
        self.root.destroy()
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if file_path:
            self.txt_file_path.set(file_path)
            self.status_label.configure(text=f"📄 Archivo seleccionado: {os.path.basename(file_path)}")
            
    def browse_directory(self):
        directory = filedialog.askdirectory(title="Seleccionar directorio de salida")
        if directory:
            self.output_directory.set(directory)
            self.status_label.configure(text=f"📁 Directorio de salida: {directory}")
            
    def parse_structure(self, content):
        """Parsea el contenido del archivo y extrae la estructura de carpetas"""
        lines = content.strip().split('\n')
        folders = []
        
        for line_num, line in enumerate(lines):
            original_line = line
            
            # Si la línea contiene una carpeta (termina en /)
            if '/' in line and (line.strip().endswith('/') or line.rstrip().endswith('/')):
                # Extraer el nombre de la carpeta
                # Buscar la última parte que termina en /
                parts = line.split('/')
                folder_name = None
                for part in reversed(parts):
                    clean_part = re.sub(r'[├└│─┐┘┌└┴┬┤├┼\s]', '', part)
                    if clean_part:
                        folder_name = clean_part
                        break
                
                if folder_name:
                    # Calcular nivel de indentación más sofisticado
                    # Método 1: Contar caracteres de árbol y espacios
                    tree_chars = len(re.findall(r'[├└│─┐┘┌└┴┬┤├┼]', line))
                    leading_spaces = len(line) - len(line.lstrip())
                    
                    # Método 2: Posición del nombre de la carpeta en la línea
                    folder_position = line.find(folder_name)
                    
                    # Usar la posición como indicador de nivel
                    indent_level = folder_position // 4  # Asumir 4 espacios por nivel
                    
                    folders.append((folder_name, indent_level, line_num, original_line))
                    
        return folders
    
    def build_folder_paths(self, folders):
        """Construye las rutas completas de las carpetas"""
        folder_paths = []
        path_stack = []  # Stack para mantener la jerarquía: [(carpeta, nivel_indentación)]
        
        for folder_name, indent_level, line_num, original_line in folders:
            # Limpiar el stack: remover carpetas que están al mismo nivel o más profundas
            while len(path_stack) > 0 and path_stack[-1][1] >= indent_level:
                path_stack.pop()
            
            # Construir la ruta completa
            if path_stack and indent_level > 0:
                # Hay carpetas padre, construir ruta anidada
                parent_path = path_stack[-1][0]
                full_path = os.path.join(parent_path, folder_name)
            else:
                # Es una carpeta raíz
                full_path = folder_name
                
            folder_paths.append(full_path)
            path_stack.append((full_path, indent_level))
            
        return folder_paths
    
    def show_preview(self):
        """Muestra una vista previa de las carpetas que se crearán"""
        if not self.txt_file_path.get():
            messagebox.showwarning("Advertencia", "Por favor selecciona un archivo de texto.")
            return
            
        try:
            with open(self.txt_file_path.get(), 'r', encoding='utf-8') as file:
                content = file.read()
                
            # Limpiar el área de texto
            self.preview_text.delete(1.0, "end")
            
            # Mostrar contenido raw para debug
            self.preview_text.insert("end", "📄 CONTENIDO DEL ARCHIVO:\n")
            self.preview_text.insert("end", "=" * 60 + "\n")
            lines = content.strip().split('\n')
            for i, line in enumerate(lines):
                self.preview_text.insert("end", f"Línea {i+1}: '{line}'\n")
                # Mostrar análisis de caracteres
                self.preview_text.insert("end", f"  Longitud: {len(line)}, Espacios iniciales: {len(line) - len(line.lstrip())}\n")
                
            self.preview_text.insert("end", "\n" + "=" * 60 + "\n")
                
            folders = self.parse_structure(content)
            folder_paths = self.build_folder_paths(folders)
            
            # Mostrar debug de la interpretación
            self.preview_text.insert("end", "🔍 DEBUG - Carpetas detectadas:\n")
            for folder_name, indent_level, line_num, original_line in folders:
                self.preview_text.insert("end", f"  '{folder_name}' (nivel: {indent_level}) - Línea {line_num+1}\n")
                self.preview_text.insert("end", f"    Línea original: '{original_line}'\n")
            
            self.preview_text.insert("end", "\n📁 Carpetas que se crearán:\n\n")
            
            for path in folder_paths:
                full_path = os.path.join(self.output_directory.get(), path)
                # Mostrar con indentación visual
                depth = path.count(os.sep)
                indent = "  " * depth
                folder_name = os.path.basename(path)
                self.preview_text.insert("end", f"{indent}📁 {folder_name}\n")
                
            self.preview_text.insert("end", f"\n🗂️ Rutas completas:\n")
            for path in folder_paths:
                full_path = os.path.join(self.output_directory.get(), path)
                self.preview_text.insert("end", f"  {full_path}\n")
                
            self.status_label.configure(text=f"✅ Vista previa generada: {len(folder_paths)} carpetas detectadas")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer el archivo: {str(e)}")
            self.preview_text.insert("end", f"❌ ERROR: {str(e)}\n")
            
    def generate_folders(self):
        """Genera la estructura de carpetas"""
        if not self.txt_file_path.get():
            messagebox.showwarning("Advertencia", "Por favor selecciona un archivo de texto.")
            return
            
        if not self.output_directory.get():
            messagebox.showwarning("Advertencia", "Por favor selecciona un directorio de salida.")
            return
            
        try:
            # Leer el archivo
            with open(self.txt_file_path.get(), 'r', encoding='utf-8') as file:
                content = file.read()
                
            # Parsear la estructura
            folders = self.parse_structure(content)
            folder_paths = self.build_folder_paths(folders)
            
            # Crear las carpetas
            created_folders = []
            for path in folder_paths:
                full_path = os.path.join(self.output_directory.get(), path)
                try:
                    os.makedirs(full_path, exist_ok=True)
                    created_folders.append(full_path)
                except Exception as e:
                    messagebox.showerror("Error", f"Error al crear la carpeta {full_path}: {str(e)}")
                    return
                    
            # Mostrar resultado
            messagebox.showinfo(
                "Éxito", 
                f"✅ Se crearon {len(created_folders)} carpetas exitosamente.\n\n"
                f"📁 Directorio base: {self.output_directory.get()}"
            )
            
            self.status_label.configure(text=f"🎉 Proceso completado: {len(created_folders)} carpetas creadas exitosamente")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante el proceso: {str(e)}")

def main():
    root = ctk.CTk()
    app = FolderStructureGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()