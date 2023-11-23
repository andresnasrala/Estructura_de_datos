from Grafo import Grafo

if __name__ == "__main__":
    g = Grafo(4)

    g.insertarVertices(["A","B","C","D"])

    g.insertarAristas([
        ("A","C",3),("A","B",7),
        ("B","D",2),
        ("C","B",2),("C","D",8)
    ])

    print(g.camino("D","A"))