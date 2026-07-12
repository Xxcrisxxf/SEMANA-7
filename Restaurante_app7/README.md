Nombre : CRISTIAN JAIR BRAVO CHIMBORAZO
Descripción del sistema
Este sistema es una aplicación de consola modular orientada a objetos (POO) diseñada para administrar las operaciones básicas de un restaurante. Permite el registro, almacenamiento en memoria, listado y búsqueda de dos componentes esenciales del negocio: Productos (comidas, bebidas, etc.) y Clientes.
 La estructura de carpetas y archivos se distribuye de la siguiente manera:

Repositorio GitHub
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── cliente.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   └── main.py
└── README.md
La clase Producto utiliza un constructor tradicional __init__ encargado de inicializar los atributos del objeto al momento de su creación dinámica. Recibe los parámetros obligatorios nombre, categoria, precio y un parámetro opcional parametrizado por defecto disponible = True.
@property : Permite acceder a los atributos privados (como __precio, __nombre o __categoria) de forma pública y segura como si fueran variables normales, protegiendo el acceso directo al estado interno del objeto.

@setter : Actúa como un filtro interceptor cuando se intenta modificar o asignar un valor a los atributos. Aquí se centralizan las validaciones del negocio; por ejemplo, si el precio asignado es menor a 0 o si las cadenas de texto se ingresan vacías, el setter bloquea la operación y lanza una excepción controlada.

La clase Cliente fue implementada utilizando el decorador @dataclass importado del módulo dataclasses de Python. Esta herramienta simplifica la creación de clases destinadas exclusivamente a almacenar datos.

El archivo main.py implementa una interfaz interactiva basada en un bucle cíclico que organiza las operaciones del restaurante en un menú numérico de siete opciones claras para el usuario. Las primeras tres opciones controlan la gestión de productos (registrar, listar y buscar por nombre), mientras que las opciones de la 4 a la 6 administran la base de clientes ( listado general y búsqueda mediante su número de identificación).

Reflexión:
En el desarrollo de software real, los datos nunca se dejan fijos  de forma estática en el código fuente. La creación dinámica de objetos a partir de las entradas proporcionadas por el usuario por medio de input() dota a las aplicaciones de verdadera flexibilidad, interactividad y escalabilidad.