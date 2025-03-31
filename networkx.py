import networkx as nx

# Creamos un grafo dirigido para representar el sistema de transporte
G = nx.DiGraph()

# Agregamos rutas con pesos basados en tiempo y costo
G.add_edge("A", "B", tiempo=25, costo=1.5)
G.add_edge("A", "B", tiempo=40, costo=1.0)
G.add_edge("A", "B", tiempo=20, costo=2.5)

# Función para encontrar la mejor ruta basada en el criterio de menor tiempo y costo
def mejor_ruta(origen, destino):
    rutas = list(G.edges(data=True))
    mejor = None
    for ruta in rutas:
        if ruta[0] == origen and ruta[1] == destino:
            if mejor is None or (ruta[2]['tiempo'] < mejor[2]['tiempo'] and ruta[2]['costo'] < mejor[2]['costo']):
                mejor = ruta
    
    if mejor:
        print(f"Mejor opción: {mejor[0]} -> {mejor[1]}, Tiempo: {mejor[2]['tiempo']} min, Costo: {mejor[2]['costo']} USD")
    else:
        print("No se encontró una ruta óptima.")

# Ejecutar la búsqueda de la mejor ruta
mejor_ruta("A", "B")

