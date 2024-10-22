from PIL import Image
from igraph import Graph
from igraph import plot
import matplotlib.pyplot as plt


#Edges sao as arstas
grafo1 = Graph(edges = [(0,1), (1,2), (2,3), (3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount())
print(grafo1)

grafo2 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(3,2),(2,1),(1,0),(0,3)])
grafo2.vs['label'] = range(grafo2.vcount())
plot(grafo2, target="grafo2.png", bbox=(300, 300))
print("Salvo em imgaem")

img = Image.open("grafo2.png")
plt.imshow(img)
plt.axis('off')  # Ocultar os eixos
plt.show()