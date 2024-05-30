import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

df = pd.read_excel(r'C:\Users\Abraham\Downloads\aeropuertos.xlsx')
dfc = pd.read_csv(r'C:\Users\Abraham\Downloads\costos.csv',  sep=';' , header = None, names =['origen', 'destino', 'duracion', 'precio'])

G = nx.from_pandas_edgelist(
    dfc,
    source='origen',
    target='destino',
    edge_attr=['duracion', 'precio'],
    create_using=nx.DiGraph
)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrowsize=20)

edge_labels_duration = nx.get_edge_attributes(G, 'duracion')
edge_labels_price = nx.get_edge_attributes(G, 'precio')

edge_labels_combined = {key: f"dur: {value}, price: {edge_labels_price[key]}" for key, value in edge_labels_duration.items()}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_combined, font_color='red')

plt.title('Graph with Duration and Cost')
plt.show()


def comprobar_vuelo(G, ciudad1, ciudad2):
    if G.has_edge(ciudad1, ciudad2) or G.has_edge(ciudad2, ciudad1):
        return "Hay vuelos entre {} y {}.".format(ciudad1, ciudad2)
    else:
        return "No hay vuelos entre {} y {}.".format(ciudad1, ciudad2)
        
def ruta_mas_barata(G, ciudad1, ciudad2):
    try:
        path = nx.dijkstra_path(G, ciudad1, ciudad2, weight='precio')
        return "La ruta mas barata entre {} y {} es: {}".format(ciudad1, ciudad2, ' -> '.join(path))
    except nx.NetworkXNoPath:
        return "No hay rutas entre {} y {}.".format(ciudad1, ciudad2)

def tiempo_total_de_vuelo(G, ciudad1, ciudad2):
    try:
        duration = nx.dijkstra_path_length(G, ciudad1, ciudad2, weight='duracion')
        return "La duracion total del vuelo entre {} a {} es: {} minutos".format(ciudad1, ciudad2, duration)
    except nx.NetworkXNoPath:
        return "No hay rutas entre {} y {}.".format(ciudad1, ciudad2)

def encontrar_ruta(G, ciudad1, ciudad2):
    try:
        path = nx.dijkstra_path(G, ciudad1, ciudad2, weight='precio')
        return "La ruta entre {} y {} es: {}".format(ciudad1, ciudad2, ' -> '.join(path))
    except nx.NetworkXNoPath:
        return "No hay rutas entre {} y {}.".format(ciudad1, ciudad2)
    
def ruta_mas_rapida(G, ciudad1, ciudad2):
    try:
        path = nx.dijkstra_path(G, ciudad1, ciudad2, weight='duracion')
        return "La ruta mas rapida entre {} y {} es: {}".format(ciudad1, ciudad2, ' -> '.join(path))
    except nx.NetworkXNoPath:
        return "No hay rutas entre {} y {}.".format(ciudad1, ciudad2)
    
    
ciudad1 = input("Ingrese la Ciudad de origen: ")
ciudad2 = input("Ingrese la Ciudad de destino: ")

while(True):
    print("1. Comprobar si hay vuelos entre {} y {}.".format(ciudad1, ciudad2))
    print("2. Encontrar la ruta mas barata entre {} y {}.".format(ciudad1, ciudad2))
    print("3. Encontrar la duracion total del vuelo entre {} y {}.".format(ciudad1, ciudad2))
    print("4. Encontrar la ruta entre {} y {}.".format(ciudad1, ciudad2))
    print("5. Encontrar la ruta mas rapida entre {} y {}.".format(ciudad1, ciudad2))
    print("6. Salir")
    
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        print(comprobar_vuelo(G, ciudad1, ciudad2))
    elif opcion == 2:
        print(ruta_mas_barata(G, ciudad1, ciudad2))
    elif opcion == 3:
        print(tiempo_total_de_vuelo(G, ciudad1, ciudad2))
    elif opcion == 4:
        print(encontrar_ruta(G, ciudad1, ciudad2))
    elif opcion == 5:
        print(ruta_mas_rapida(G, ciudad1, ciudad2))
    elif opcion == 6:
        break
    else:
        print("Opcion invalida. Intente de nuevo.")