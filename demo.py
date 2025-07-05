from error import *
from datetime import date
from campania import Campania
from anuncio import *

try:
    #
    campania = Campania("Campaña Inicial", date.today(), date.today(), [{"tipo": "Video", "sub_tipo": "instream"}])

    #
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    nuevo_sub_tipo = input("Ingrese el nuevo subtipo para el anuncio de video: ")

    # 
    campania.nombre = nuevo_nombre
    if campania.anuncios and isinstance(campania.anuncios[0], Video):
        campania.anuncios[0].sub_tipo = nuevo_sub_tipo

    print(campania)

except (LargoExcedidoError, SubTipoInvalidoError) as e:
    with open("error.log", "a") as f:
        f.write(f"{type(e).__name__}: {e}\n")
    print(f"Error: {e}")