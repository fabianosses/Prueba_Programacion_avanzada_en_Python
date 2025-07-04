

class Anuncio:
    def __init__(self, ancho = int, alto = int, url_archivo = str, url_clic = str, sub_tipo = str):
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

    @ancho.setter
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

    @ancho.setter
    def url_clic (self, url_clic):
        self.__url_clic = url_clic

    @property
    def sub_tipo (self):
        return self.__sub_tipo

    @ancho.setter
    def sub_tipo (self, sub_tipo):
        self.__sub_tipo = sub_tipo

    def mostrar_formatos():
        pass

    def comprimir_anuncios():
        pass
    
    def redimensionar_anuncio():
        pass


class Campania:
    pass

class Video:
    pass

class Display:
    pass

class Social:
    pass

