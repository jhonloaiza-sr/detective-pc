#Importar Configuración 
from detective_pc.configuracion import Configuracion
#Importar DetectiveArchivos 
from detective_pc.herramientas import DetectiveArchivos
#Importar AgenteDetective
from detective_pc.agente import AgenteDetective

def main()-> None:
    #Se crea el objeto configuracion
    config = Configuracion()
    #Se crea el objeto detective
    detective = DetectiveArchivos(config.carpeta_objetivo)
    #Se crea el objeto del agente
    agente = AgenteDetective(config, detective)
    #Se imprime un titulo de bienvenida
    print(config.mostrar_resumen())

    #Ciclo conversacional
    while True:
        #Ingresa la pregunta del usuario en consola
        pregunta : str = input("Tú: ").strip().lower()
        #Se condiciona la salida o finalizacion de la conversacion
        if pregunta in ("salir", "exit"):
            #Mensaje de salida
            print("Hasta luego, estare atento")
            break
        if not pregunta:
            continue
        
        respuesta = agente.responder(pregunta)
        print(f"Detective: {respuesta}")

if __name__ == "__main__":
    main()

            






