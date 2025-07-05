from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio (ABC):
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho (self):
        return self.__ancho

    @ancho.setter
    def ancho (self, ancho):
        self.__ancho = ancho

    @property
    def alto (self):
        return self.__alto

    @alto.setter
    def alto (self, alto):
        self.__alto = alto

    @property
    def url_archivo (self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo (self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_clic (self):
        return self.__url_clic

    @url_clic.setter
    def url_clic (self, url_clic):
        self.__url_clic = url_clic

    @property
    def sub_tipo (self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo (self, sub_tipo):
        if (isinstance(self,Video) and sub_tipo in Video.SUB_TIPOS
            or isinstance(self,Social) and sub_tipo in Social.SUB_TIPOS
            or isinstance(self,Display) and sub_tipo in Display.SUB_TIPOS):
            self.__sub_tipo = sub_tipo
        else:
            raise SubTipoInvalidoError("error de tipo invalido.")

    @staticmethod
    def mostrar_formatos():
        print("FORMATOS DISPONIBLES:")
        print("======================")
        return [f"{Video.FORMATO} - {Display.FORMATO} - {Social.FORMATO}"]


    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, duracion, subtipo):
        self.ancho = 1 
        self.alto = 1
        self.__duracion = duracion if duracion > 0 else 5
        self.sub_tipo = subtipo

    @property
    def duracion (self):
        return self.__duracion

    @duracion.setter
    def duracion (self, duracion):
        self.__duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")