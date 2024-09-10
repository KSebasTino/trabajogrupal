class Geometria:
    def area_cuadrado(self, lado):
        return self._area_rectangulo(lado, lado)

    def area_rectangulo(self, ancho, alto):
        return self._area_rectangulo(ancho, alto)

    def perimetro_cuadrado(self, lado):
        return self._perimetro_rectangulo(lado, lado)

    def perimetro_rectangulo(self, ancho, alto):
        return self._perimetro_rectangulo(ancho, alto)

    def _area_rectangulo(self, ancho, alto):
        return ancho * alto

    def _perimetro_rectangulo(self, ancho, alto):
        return 2 * (ancho + alto)
