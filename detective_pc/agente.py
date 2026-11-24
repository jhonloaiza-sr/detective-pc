#Importamos Ollama
import ollama
#Importamos Any de typing
from typing import Any
#Importar configuracion de detective_pc.configuracion
from detective_pc.configuracion import Configuracion
#Importat detectivearchivos de detective_pc.herramientas
from detective_pc.herramientas import DetectiveArchivos

#Definimos la clase del agente
class AgenteDetective:
    #Se define el constructor
    def __init__(self, config : Configuracion, detective : DetectiveArchivos)-> None:
        #Se guarda config
        self.config : Configuracion = config
        #Se guarda detective
        self.detective : DetectiveArchivos = detective
        #Se crea un diccionario que mapea el texto de cada método objeto
        self.herramientas : dict[str,Any] = {
            #Herramienta 1. Lista carpetas y archivos
            "listar_contenido": self.detective.listar_contenido,
            #Herramienta 2. Busca archivos por extension
            "buscar_por_extension": self.detective.buscar_por_extension,
            #Herramienta 3. Encuentra los archivos más pesados
            "buscar_mas_pesados": self.detective.buscar_mas_pesados,
            #Herramienta 4. Mueve un archivo a una subcarpeta pidiendo permiso humano primero
            "mover_archivo": self.detective.mover_archivo
            }
        self.lista_tools : list[Any] = list(self.herramientas.values())
        self.historial : list[Any] = [{"role": "system", "content": self.config.instrucciones}]

    #Método privado auxiliar que ejecuta una herramienta de forma segura sin que un error cierre el programa.
    def _ejecutar_herramienta(self, nombre: str, argumentos: dict[str, Any]) -> str:
        # Buscamos el método en el diccionario usando su nombre en texto.
        funcion = self.herramientas.get(nombre)
        # Si el modelo pidió una herramienta que no existe, devolvemos un aviso en texto.
        if not funcion:
            # Informamos al modelo del error para que no insista con esa herramienta.
            return f"Error: La herramienta '{nombre}' no existe."
        # Intentamos ejecutar la función desempaquetando el diccionario de argumentos con '**'.
        try:
            # Llamamos al método real y convertimos su resultado a texto.
            return str(funcion(**argumentos))
        # Si el modelo envió algún argumento equivocado, capturamos el error y se lo contamos como texto.
        except Exception as error:
            # Devolvemos el error para que el agente pueda corregirse en su respuesta.
            return f"Error al ejecutar '{nombre}': {error}"




    def responder(self,pregunta:str)-> str:

        self.historial.append({"role": "user", "content": pregunta})

        try:

            respuesta = ollama.chat(model = self.config.modelo,
                        messages = self.historial,
                        tools = self.lista_tools,
                        think = False)
            
            self.historial.append(respuesta.message)

        except Exception as error:
            return f"Error al comunicarse con Ollama {error}"


        if respuesta.message.tool_calls:
            for llamada in respuesta.message.tool_calls:
                nombre = llamada.function.name
                argumentos = llamada.function.arguments
                print(f"[Herramienta]: {nombre} ({argumentos})")

                resultado: str = self._ejecutar_herramienta(nombre,argumentos)

                self.historial.append({"role": "tool", "content": resultado})

            try:
                # Ahora el modelo lee los datos reales que encontró la herramienta y redacta su respuesta en español.
                respuesta_final = ollama.chat(model=self.config.modelo, messages=self.historial, think=False)
                # Guardamos la respuesta definitiva en la memoria del agente.
                self.historial.append(respuesta_final.message)
                # Devolvemos el texto final (o vacío si viniera None).
                return respuesta_final.message.content or ""
            # Si falla la segunda llamada, devolvemos el error sin romper el programa.
            except Exception as error:
                # Retornamos el mensaje de error.
                return f"Error al comunicarse con Ollama: {error}"

        # Si el modelo no necesitó herramientas (ej. un saludo), devolvemos su respuesta directa.
        return respuesta.message.content or "" 
        


