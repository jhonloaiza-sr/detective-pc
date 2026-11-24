# El Detective de tu PC (Agente Local en POO)

Agente conversacional 100% local construido en Python con **Programación Orientada a Objetos (POO)**, **`uv`** y **Tool Calling nativo en Ollama** (`qwen3.5:9b`), capaz de inspeccionar carpetas reales en Windows 11 y responder preguntas sobre archivos locales.

## Estructura Modular

```text
detective-pc/
├── main.py                      # Bucle conversacional en consola
└── detective_pc/
    ├── configuracion.py         # Clase Configuracion (modelo, ruta objetivo y rol)
    ├── herramientas.py          # Clase DetectiveArchivos (listar, buscar por extensión y más pesados)
    └── agente.py                # Clase AgenteDetective (memoria y ciclo Tool Calling con Ollama)
```

## Cómo ejecutarlo

```powershell
# Instalar dependencias con uv
uv sync

# Iniciar el agente en consola
uv run main.py
```

*(Requiere tener [Ollama](https://ollama.com/) activo con el modelo `qwen3.5:9b` descargado).*
