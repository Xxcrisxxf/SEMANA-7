class Producto:
    #Constructor para los productos
    def __init__(self , nombre:str , categoria: str, precio:float , disponible:bool = True ):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible  = disponible
    #Creamos un metodo  especial para representar la clase como texto
    @property
    def precio(self) -> int:
        return self.__precio
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            print("Error el precio puesto es menor a 0")
        else:
            self.__precio = nuevo_precio
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre (self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacio ")
        else:
            self.__nombre = nuevo_nombre
    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str):
        if not nueva_categoria.strip():
            raise ValueError("La categoría no puede estar vacia.")
        self.__categoria = nueva_categoria.strip()

    # Método para mostrar la información de forma legible
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Agotado"
        print(f"Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Estado: {estado}")