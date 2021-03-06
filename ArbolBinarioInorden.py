class Nodo(object):
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        
#Se crean los nodos de tal manera que sea un arbol que vaya así
#------------------
#         A
#       /  \
#      B    C
#     / \  / \
#    D  E  F  G
#------------------
        
p=Nodo("A")
r=p
t=p
q=p

p=Nodo("B")
r.left=p
t=p
p=Nodo("C")
r.right=p
q=p
p=Nodo("D")
t.left=p
p=Nodo("E")
t.right=p
p=Nodo("F")
q.left=p
p=Nodo("G")
q.right=p

#Metodo para recorrer el nodo a su .left, siempre y cuando este no sea None
def GoLeft(nodo):
    if(nodo.left!=None):
        nodo=nodo.left
        Ino(nodo)

#Metodo para recorrer el nodo a su .right, siempre y cuando este no sea None
def GoRight(nodo):
    if(nodo.right!=None):
        nodo=nodo.right
        Ino(nodo)
    
#Metodo para recorrer todo el arbol en InOrden
#Primero recorrera el subarbol izquierdo
#Despues imprimira la raiz   
#Y al final recorrera el subarbol derecho
def Ino(nodo):
    GoLeft(nodo)
    print(nodo.data)
    GoRight(nodo)
    
Ino(r)