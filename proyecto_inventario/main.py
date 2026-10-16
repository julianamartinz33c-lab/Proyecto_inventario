import asyncio
#Importar funciones de otro archivo 
from database import leer_base_datos, guardar_base_datos

async def iniciar_sistema():
    print("Iniciando el sistema...")
    datos = await leer_base_datos()
    print(f"Base de datos cargada con: {len(datos)} registros.")

asyncio.run(iniciar_sistema())