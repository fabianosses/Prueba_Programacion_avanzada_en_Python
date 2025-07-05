from error import LargoExcedidoError
from anuncio import *

class Campania:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_data):
      self.__nombre = nombre
      self.__fecha_inicio = fecha_inicio
      self.__fecha_termino = fecha_termino
      self.__anuncios = (anuncios_data)

    def __crear_anuncios(self, anuncios_data):
        for anuncio_data in anuncios_data:
            tipo = anuncio_data.get("tipo")
            if tipo == "Video":
                anuncio = Video(
                    url_archivo=anuncio_data.get("url_archivo", ""),
                    url_clic=anuncio_data.get("url_clic", ""),
                    sub_tipo=anuncio_data.get("sub_tipo", ""),
                    duracion=anuncio_data.get("duracion", 0)
                )
            elif tipo == "Display":
                anuncio = Display(
                    ancho=anuncio_data.get("ancho", 0),
                    alto=anuncio_data.get("alto", 0),
                    url_archivo=anuncio_data.get("url_archivo", ""),
                    url_clic=anuncio_data.get("url_clic", ""),
                    sub_tipo=anuncio_data.get("sub_tipo", "")
                )
            elif tipo == "Social":
                 anuncio = Social(
                    ancho=anuncio_data.get("ancho", 0),
                    alto=anuncio_data.get("alto", 0),
                    url_archivo=anuncio_data.get("url_archivo", ""),
                    url_clic=anuncio_data.get("url_clic", ""),
                    sub_tipo=anuncio_data.get("sub_tipo", "")
                )
            else:
                print(f"Tipo de anuncio desconocido: {tipo}")
                continue

            self.__incorporar_anuncios(anuncio)


    def __incorporar_anuncios(self, anuncio):
        self.__anuncios.append(anuncio)

    def __str__(self):
        video_count = sum(1 for anuncio in self.__anuncios if isinstance(anuncio, Video))
        display_count = sum(1 for anuncio in self.__anuncios if isinstance(anuncio, Display))
        social_count = sum(1 for anuncio in self.__anuncios if isinstance(anuncio, Social))
        return f"Nombre de la campaña: {self.__nombre}\nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"

    @property
    def nombre (self):
        return self.__nombre

    @nombre.setter
    def nombre (self, nombre):
        if len(nombre) > 250:
            raise LargoExcedidoError ("El largo del texto supera los 250 caracteres")
        self.__nombre = nombre

    @property
    def anuncios (self):
        return self.__anuncios

    @property
    def fecha_inicio (self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio (self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_termino (self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino (self, fecha_termino):
        self.__fecha_termino = fecha_termino