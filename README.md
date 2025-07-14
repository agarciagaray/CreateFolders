# 📁 Generador de Estructura de Directorios

## Descripción 📄
Esta herramienta de escritorio desarrollada en Python permite crear estructuras de directorios de forma rápida y sencilla a partir de un archivo de texto. Ideal para desarrolladores que buscan generar proyectos con arquitecturas predefinidas de manera consistente y eficiente.

## Características ✨
- **Interfaz gráfica moderna**: Desarrollada con `customtkinter` para una experiencia visual atractiva.
- **Previsualización**: Revisa la estructura antes de crearla.
- **Flexibilidad**: Selecciona la ubicación de destino y admite múltiples niveles de directorios.
- **Carga desde archivos**: Importa estructuras desde archivos de texto plano.

## Requisitos Previos 📋
- Python 3.x (preferiblemente 3.9 o superior)
- Gestor de paquetes `pip`

## Instalación 🔧
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/generador-estructura-directorios.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd generador-estructura-directorios
   ```
3. Instala las dependencias:
   ```bash
   pip install customtkinter
   ```

## Uso 🚀
1. Ejecuta la aplicación:
   ```bash
   python folder_structure_generator.py
   ```
2. Desde la interfaz gráfica:
   - Haz clic en **"Cargar Archivo"** para seleccionar tu archivo de texto con la estructura.
   - Usa **"Seleccionar Destino"** para definir la ubicación de los directorios.
   - (Opcional) Revisa la estructura con **"Vista Previa"**.
   - Finalmente, haz clic en **"Crear Directorios"**.

### Formato del Archivo de Texto 📝
El archivo debe describir la estructura con indentaciones. Ejemplo:
```
proyecto/
    src/
        controllers/
        models/
        views/
    tests/
    docs/
    resources/
```

## Ejemplos de Uso 💡
### Estructura Básica
```
mi-proyecto/
    src/
    tests/
    docs/
    README.md
```

### Estructura MVC
```
proyecto-mvc/
    app/
        controllers/
        models/
        views/
    config/
    public/
    tests/
```

## Contribución 🤝
¡Las contribuciones son bienvenidas! Para participar:
1. Haz fork del repositorio.
2. Crea una rama: `git checkout -b feature/AmazingFeature`.
3. Realiza tus cambios y commitea: `git commit -m 'Add some AmazingFeature'`.
4. Push a la rama: `git push origin feature/AmazingFeature`.
5. Abre un Pull Request.

## Licencia 📃
Este proyecto está bajo la Licencia MIT. Ver [LICENSE.md](LICENSE.md) para más detalles.

## Autor ✒️
- **[Alejandro García Garay]** - [agarciagaray](https://github.com/agarciagaray/CreateFolders.git)

## Agradecimientos 🎁
- A la comunidad de Python por sus herramientas y librerías.
- A `customtkinter` por la interfaz moderna.
```