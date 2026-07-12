from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, nombre: str):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def agregar_cliente(self, cliente: Cliente):
        for cliente_registrado in self.clientes:
            if cliente_registrado.id_cliente == cliente.id_cliente:
                return False
        self.clientes.append(cliente)
        return True

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente(self, id_cliente: int):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None