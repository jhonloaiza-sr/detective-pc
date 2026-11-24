#Importamos Path de pathlib
from pathlib import Path

#Creamos la clase DetectiveArchivos
class DetectiveArchivos:
    #Inicializamos el constructor
    def __init__(self, carpeta: Path)-> None:
        #Definimos donde se guarda la carpeta
        self.carpeta : Path = carpeta

    #Definimos el metodo verificar existencia y recorre los elementos clasificando cada elemento
    def listar_contenido(self) -> str:
        #Instrucciones que Ollama lee
        """
        Lista todas las carpetas y archivos dentro de la carpeta vigilada.
        """

        #Se verifica si la carpeta existe
        if not self.carpeta.exists():
            #Mensaje de error
            return f"Error: la carpeta {self.carpeta} no existe"

        
        #Se crea una lista vacia de almacenamiento
        lista : list[str] = []

        #Ciclo for para recorrer los elementos de la carpeta
        for item in self.carpeta.iterdir():
            #Se verifica si es carpeta
            if item.is_dir():
                #Se agrega a la lista
                lista.append(f"[CARPETA] {item.name}")
            #Si es archivo
            else:
                #Se agrega a la lista
                lista.append(f"[ARCHIVO] {item.name}")

            if not lista:
                return "La carpeta esta completamente vacia"
            
        #Se retorna la lista
        return "\n".join(lista)

    #Se define metodo para encontrar las extensiones
    def buscar_por_extension(self, extension: str)-> str:
        #Se especifica los tipos de extensiones
        """
        Busca archivos que terminen en una extensión específica (ej. '.pdf', '.exe', '.jpg') y muestra su tamaño en MB.
        """

        if not self.carpeta.exists():
            return f"Error: La carpeta {self.carpeta} no existe."

        #Se almacena las extensiones 
        extension = extension.strip().lower()

        #Si  no empieza en punto  se le agrega
        if not extension.startswith("."):
            #Se auto escribe agregando el punto al inicio
            extension = f".{extension}"

        encontrados : list[Path] = [
            item 
            for item in self.carpeta.iterdir() 
            if item.is_file() and item.suffix.lower() == extension]

        if not encontrados:
            return f"No se encontraron archivos con extensión {extension}"

        resultado : list[str] = []

        for archivo in encontrados:
            mb: float = archivo.stat().st_size / (1024 * 1024)
            resultado.append(f"{archivo.name} ({mb: .2f} MB)")
        

        return "\n".join(resultado)


     # Método 3 (Bonus): encuentra los archivos más pesados ordenados de mayor a menor.
    def buscar_mas_pesados(self, limite: int = 5) -> str:
        # Docstring para que Ollama sepa usar 'limite' cuando el usuario pida el top de archivos pesados.
        """Devuelve los archivos más pesados de la carpeta ordenados de mayor a menor tamaño en MB."""
        # Verificamos si la carpeta existe.
        if not self.carpeta.exists():
            # Retornamos error si no existe.
            return f"Error: La carpeta '{self.carpeta}' no existe."

        # Reunimos únicamente los elementos que son archivos reales (ignorando subcarpetas).
        archivos: list[Path] = [item for item in self.carpeta.iterdir() if item.is_file()]
        # Si no hay archivos, avisamos.
        if not archivos:
            # Retornamos mensaje de carpeta sin archivos.
            return "No hay archivos en esta carpeta."

        # Ordenamos la lista de archivos de mayor a menor tamaño ('reverse=True') usando 'st_size' como criterio.
        ordenados: list[Path] = sorted(archivos, key=lambda f: f.stat().st_size, reverse=True)
        # Recortamos la lista para quedarnos solo con los primeros 'limite' archivos.
        top: list[Path] = ordenados[:limite]

        # Formateamos cada archivo con su nombre y tamaño en MB y lo devolvemos unido por saltos de línea.
        return "\n".join(f"- {f.name} ({f.stat().st_size / (1024 * 1024):.2f} MB)" for f in top)

    #Metodo para mover archivos
    def mover_archivo(self,nombre_archivo: str, carpeta_destino: str)-> str:
        #Se especifica a Ollama que hace el método
        """
        Te encargas de trasladar el archivo que se ubica en el parametro nombre_archivo el cual debe incluir la extension (ej, .pdf, .txt, .exe) a la carpeta que se encuentra en el parametro carpeta_destino que es el nombre de la subcarpeta donde se guardará (ej, "Notas").
        """
        #Se almacena el origen del archivo
        origen : Path = self.carpeta/ nombre_archivo
        #Se verifica si es un archivo
        if not origen.is_file():
            #Imprime error si no hay archico
            return f"No se encontro el archivo {nombre_archivo}"
        #Confirmacion del usuario si se quiere realizar el traslado
        confirmacion = input(f"[SEGURIDAD] Confirmas mover '{nombre_archivo}' a '{carpeta_destino}'? (s/n): ").strip().lower()
        #Se verifica confimación
        if confirmacion not in ("s", "si", "sí"):
            #Mensaje de que cancela la operacion
            return"operación cancelada por el usuario."
        #Se almacena la dirección de la nueva carpeta
        carpeta_nueva : Path = self.carpeta/carpeta_destino
        #Se crea la carpeta si ya esta no se crea
        carpeta_nueva.mkdir(parents = True, exist_ok = True)
        #Se almacena el destino del archivo de origen
        destino : Path = carpeta_nueva/origen.name
        #Se verifica si ya esta en el destino
        if destino.exists():
            #Retorna mensaje de error
            return f"Error: Ya existe {origen.name} dentro de la carpeta {carpeta_destino}"

        try:
            origen.rename(destino)
            return "se realizo el traslado con exito"
        except Exception as error:
            return f"Error al mover el archivo: {error}"

        



        





