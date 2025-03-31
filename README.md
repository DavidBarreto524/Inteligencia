# Sistema Inteligente de Rutas con NetworkX

## Descripción
Este proyecto implementa un sistema inteligente para encontrar la mejor ruta entre dos puntos en un sistema de transporte masivo. Utiliza la biblioteca `networkx` para modelar el sistema como un grafo dirigido, donde cada ruta tiene un tiempo y un costo asociado.

## Requisitos
Antes de ejecutar el programa, asegúrate de tener instalada la biblioteca `networkx`. Si no la tienes instalada, usa el siguiente comando:

```bash
pip install networkx
```

## Funcionamiento
El sistema funciona de la siguiente manera:
1. Se crea un **grafo dirigido** que representa las rutas del sistema de transporte.
2. Se agregan las rutas con sus respectivos tiempos y costos.
3. Se implementa una función que evalúa todas las rutas disponibles y selecciona la mejor opción basada en los criterios de **menor tiempo y menor costo**.
4. Se ejecuta la función para encontrar la mejor ruta entre dos puntos específicos.

## Uso
Para ejecutar el programa, simplemente corre el archivo Python en tu terminal o entorno de desarrollo:

```bash
python nombre_del_archivo.py
```

## Ejemplo de Salida
Si ejecutas el programa con los datos actuales, podrías obtener un resultado como:

```
Mejor opción: A -> B, Tiempo: 25 min, Costo: 1.5 USD
```

Si deseas modificar o agregar nuevas rutas, puedes hacerlo editando las líneas donde se definen los **edges** en el código:

```python
G.add_edge("A", "C", tiempo=15, costo=2.0)
```

## Contribución
Si deseas mejorar este sistema, puedes agregar nuevas funcionalidades como:
- Implementación de un algoritmo de búsqueda más avanzado como Dijkstra.
- Inclusión de múltiples criterios de optimización.
- Integración con datos en tiempo real.

¡Esperamos que este proyecto te ayude en la optimización de rutas en sistemas de transporte! 🚀

