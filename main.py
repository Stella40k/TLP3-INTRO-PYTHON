import pprint
import requests

#Ejemplo 1
def obtener_datos(easting: int, northing: int) -> dict:
    """ Obtener datos desde una api publica para convertir Coordenadas de 
        British National Grid (Reino Unido) a coordenadas globales 
        
        args: 
        - easting: este - int
        - northing: norte - int
    """
    dtos = requests.get(url=f"https://api.getthedata.com/bng2latlong/{easting}/{northing}")
    if dtos.status_code == 400: 
        dtos = {
            "status": "bad_request",
            "error": "Datos ingresados invalidos!" 
        }
        return dtos
    return dtos.json()

def mostrar_datos(dtos: dict):
    """ Mostrar los datos obtenidos desde la API """
    if dtos["status"] == "ok":
        pprint.pprint(dtos)
    else:
        pprint.pprint(dtos) 



#Ejemplo 2

def obtener_notas() -> list:
    """ Generar notas de estudiantes """
    notas = [
        {
            "nombre": "Gabriel",
            "nota": 8.5,
            "fecha": "2022-01-01",
        },
        {
            "nombre": "Pedro",
            "nota": 7.5,
            "fecha": "2022-02-01",
        },
        {
            "nombre": "Juan",
            "nota": 9.0,
            "fecha": "2022-03-01",
        },
    ]
    return notas

def calcular_promedio(notas: list) -> float:
    """ Calcular el promedio de notas """
    lista_notas = [nota["nota"] for nota in notas ]
    total = sum(lista_notas)
    return total / len(lista_notas)


def generar_reporte(notas: list, promedio: float) -> dict: 
    """ Mostrar un reporte"""
    reporte = {
        "notas": notas,
        "promedio": promedio
        }
    
    return reporte

#Ejemplo 1: 
# dto = obtener_datos(easting=530000, northing=180000)
# mostrar_datos(dtos=dto)

#Ejemplo 2
datos = obtener_notas()
promedio = calcular_promedio(datos)
pprint.pprint(generar_reporte(notas= datos, promedio= promedio))
