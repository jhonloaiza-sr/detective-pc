# El Detective de tu PC (Agente Local en POO)

Agente conversacional 100% local construido en Python con **Programación Orientada a Objetos (POO)**, **`uv`** y **Tool Calling nativo en Ollama** (`qwen3.5:9b` con `think=False`), capaz de inspeccionar y organizar carpetas reales en Windows 11.

## Estructura Modular

```text
detective-pc/
├── main.py                      # Bucle conversacional en consola
└── detective_pc/
    ├── configuracion.py         # Clase Configuracion (modelo, ruta objetivo y rol)
    ├── herramientas.py          # Clase DetectiveArchivos (listar, buscar por extensión y más pesados, y mover con seguridad)
    └── agente.py                # Clase AgenteDetective (memoria, roles y ciclo Tool Calling con Ollama)
```

## Herramientas y Seguridad

* `listar_contenido`: Lista carpetas y archivos de la ruta vigilada.
* `buscar_por_extension`: Filtra archivos por extensión y calcula su peso en MB.
* `buscar_mas_pesados`: Ordena los archivos de mayor a menor tamaño.
* `mover_archivo`: Mueve archivos a subcarpetas con **confirmación humana obligatoria** (*Human-in-the-Loop*) y validación de rutas (`is_relative_to`) para no salir de la carpeta autorizada.

## Cómo ejecutarlo

```powershell
# Instalar dependencias con uv
uv sync

# Iniciar el agente en consola
uv run main.py
```

*(Requiere tener [Ollama](https://ollama.com/) activo con el modelo `qwen3.5:9b` descargado).*
