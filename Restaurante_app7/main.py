from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 40)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 40)
    print("7. Salir")

def registrar_producto(restaurante):
    print("\n--- Registrar producto ---")
    try:
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = float(input("Precio: "))
        
        producto = Producto(nombre, categoria, precio)
        restaurante.agregar_producto(producto)
        print("\nProducto registrado correctamente.")
    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("\nError: El precio debe ser un número válido.")
        else:
            print(f"\n{e}")

def listar_productos(restaurante):
    print("\n--- Lista de productos ---")
    productos = restaurante.listar_productos()
    if productos:
        for producto in productos:
            producto.mostrar_informacion()
    else:
        print("No existen productos registrados.")

def buscar_producto(restaurante):
    print("\n--- Buscar producto ---")
    nombre = input("Ingrese el nombre del producto: ")
    producto = restaurante.buscar_producto(nombre)
    if producto:
        print("\nProducto encontrado:")
        producto.mostrar_informacion()
    else:
        print("\nNo se encontró el producto.")

def registrar_cliente(restaurante):
    print("\n--- Registrar cliente ---")
    try:
        nombre = input("Nombre: ").strip()
        correo = input("Correo electrónico: ").strip()
        id_cliente = int(input("ID del cliente: "))

        if not nombre or not correo:
            print("\nEl nombre y el correo no pueden estar vacíos.")
            return

        cliente = Cliente(nombre, correo, id_cliente)
        exito = restaurante.agregar_cliente(cliente)
        if exito:
            print("\nCliente registrado correctamente.")
        else:
            print(f"\nError: Ya existe un cliente con el ID {id_cliente}.")
    except ValueError:
        print("\nError: El ID del cliente debe ser un número entero válido.")

def listar_clientes(restaurante):
    print("\n--- Lista de clientes ---")
    clientes = restaurante.listar_clientes()
    if clientes:
        for cliente in clientes:
            print(f"ID: {cliente.id_cliente} | Nombre: {cliente.nombre} | Correo: {cliente.correo}")
    else:
        print("No existen clientes registrados.")

def buscar_cliente(restaurante):
    print("\n--- Buscar cliente ---")
    try:
        id_cliente = int(input("Ingrese el ID del cliente: "))
        cliente = restaurante.buscar_cliente(id_cliente)
        if cliente:
            print("\nCliente encontrado:")
            print(f"ID: {cliente.id_cliente} | Nombre: {cliente.nombre} | Correo: {cliente.correo}")
        else:
            print("\nNo se encontró el cliente.")
    except ValueError:
        print("\nError: Ingrese un número de ID válido.")

def main():
    restaurante = Restaurante()
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("\nGracias por utilizar el sistema Restaurante.")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()