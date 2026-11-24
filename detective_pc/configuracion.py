#Importamos la libreria path
from pathlib import Path 

#Definimos la clase configuración
class Configuracion:
    #Definimos el constructor
    def __init__(self)-> None:
        #Definimos el modelo Ollama
        self.modelo : str = "qwen3.5:9b"
        #Apuntamos a la carpeta de descarga
        self.carpeta_objetivo : Path = Path.home()/"Downloads"
        #Definimos el rol del agente
        self.instrucciones : str = "Eres un agente detective de archivos en Windows 11 y tienes que responder en español"

    #Definir metodo que devuelve texto indicando el modelo que usa y carpeta 
    def mostrar_resumen(self)-> str:
        return f"El módelo usado es {self.modelo} y la carpeta de interes es {self.carpeta_objetivo}"

    


