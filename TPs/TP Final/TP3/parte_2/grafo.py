import random

class Grafo:
    '''
    Constructor del TDA Grafo, cuenta con un booleano como parámetro que 
    indica si el grafo a utilizar es dirigido (inicializado en False).
    '''
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.vertices = dict()
        self.entrantes = dict()

    def __iter__(self):
        return iter(self.vertices)

    def __len__(self):
        return len(self.vertices)

    def __contains__(self, v):
        return v in self.vertices


    def validar_vertice(self, v):
        if v not in self:
            raise Exception(f"El vértice {str(v)} no se encuentra en el grafo")

    def agregar_vertice(self, v):
        '''
        Agrega el parámetro como vértice al grafo, si se encuentra en el grafo levanta una excepción.
        '''
        if v in self.vertices:
            raise Exception(f"El vértice {str(v)} ya se encuentra en el grafo")
        
        self.vertices[v] = dict()
        self.entrantes[v] = dict()
    
    def agregar_arista(self, v, w, peso=1):
        '''
        Agrega una arista entre los vértices pasados por parámetro 
        con su respectivo peso, si ya está en el grafo levanta una excepción.
        '''
        #Caso de no estar alguno de esos vértices en el grafo.
        self.validar_vertice(v)
        self.validar_vertice(w)

        #Caso de existir la arista
        if not self.estan_unidos(v, w):  
            self.vertices[v][w] = peso
            self.entrantes[w][v] = None

        if not self.dirigido:
            self.vertices[w][v] = peso

    def eliminar_arista(self, v, w):
        '''
        Elimina la arista entre los vértices pasados por parámetro, de no existir levanta una excepción.
        '''
        if self.estan_unidos(v, w):
            del self.vertices[v][w]
        if not self.dirigido:
            self.vertices[w][v]
    
    def eliminar_vertice(self, v):
        '''
        Elimina el vértice pasado por parámetro, de no estar en el grafo levanta una excepción.
        En caso de estar en el grafo también elimina todas las aristas de las cuales formaba parte.
        '''
        self.validar_vertice(v)

        for vertice in self.vertices:
            if v in self.vertices[vertice].keys():
                del self.vertices[vertice][v]
        
        del self.vertices[v]

    def obtener_vertices(self):
        '''
        Devuelve una lista con los vértices del grafo.
        '''
        return list(self.vertices)
    
    def vertice_aleatorio(self):
        '''
        Devuelve un vértice aleatorio.
        '''
        return random.choice(list(self.vertices))

    def adyacentes(self, v):
        '''
        Recibe por parámetro un vértice, en caso de no existir en el grafo
        levanta una excepción y en caso contrario devuelve una lista de sus adyacentes.
        '''
        self.validar_vertice(v)
        return self.vertices[v]
    
    def estan_unidos(self, v, w):
        '''
        Devuelve un booleano indicando si los vértices pasados por parámetro están unidos.
        ''' 
        self.validar_vertice(v)
        self.validar_vertice(w)
        
        return w in self.vertices[v] 
    
    def obtener_peso(self, v, w):
        '''
        Devuelve el peso de la arista entre los vértices 
        pasados por parámetro.
        '''
        return self.vertices[v][w]


    def obtener_entrantes(self, v):
        '''
        Devuelve un diccionario con un vértice como clave 
        y como valor un set de vértices conectados a la clave
        '''
        self.validar_vertice(v)
        return self.entrantes[v]
    
    def orden_topologico(self):
        '''
        Devuelve una lista con los vértices del grafo en orden topológico.
        Si el grafo contiene ciclos, lanza una excepción.
        '''
        if not self.dirigido:
            raise Exception("El orden topológico solo está definido para grafos dirigidos.")

        # Contamos el grado de entrada de cada vértice
        grado_entrada = {v: len(self.entrantes[v]) for v in self.vertices}
        
        # Inicializamos la cola con los vértices de grado 0
        cola = [v for v in self.vertices if grado_entrada[v] == 0]

        orden = []
        
        while cola:
            v = cola.pop(0)
            orden.append(v)
            
            for w in self.vertices[v]:
                grado_entrada[w] -= 1
                if grado_entrada[w] == 0:
                    cola.append(w)
        
        if len(orden) != len(self.vertices):
            raise Exception("El grafo contiene ciclos, no se puede obtener un orden topológico.")
        
        return orden

    def ford_fulkerson(self):
        pass