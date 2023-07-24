from matplotlib import pyplot as plt


class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

A = _SimpulPohonBiner('T')
B = _SimpulPohonBiner('E')
C = _SimpulPohonBiner('K')
D = _SimpulPohonBiner('N')
E = _SimpulPohonBiner('I')
F = _SimpulPohonBiner('K')
G = _SimpulPohonBiner(' ')
H = _SimpulPohonBiner('I')
I = _SimpulPohonBiner('N')
J = _SimpulPohonBiner('F')
K = _SimpulPohonBiner('O')
L = _SimpulPohonBiner('R')
M = _SimpulPohonBiner('M')
N = _SimpulPohonBiner('A')
O = _SimpulPohonBiner('T')
P = _SimpulPohonBiner('I')
Q = _SimpulPohonBiner('K')
R = _SimpulPohonBiner('A')


def inorder(node):
    if node is not None:
        inorder(node.kiri)
        print(node.data, end=" ")
        inorder(node.kanan)

def postorder(node):
    if node is not None:
        postorder(node.kiri)
        postorder(node.kanan)
        print(node.data, end=" ")

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.kiri)
        preorder(node.kanan)
"""
## urutan preorder
A.kiri = B; A.kanan = H
B.kiri = C; B.kanan = D
D.kiri = E; D.kanan = F
F.kiri = G; H.kanan = J
H.kiri = I; J.kiri = K
K.kiri = L; K.kanan = M
M.kiri = N; N.kanan = O
O.kanan = P; P.kanan = Q

# Traversal preorder
print("Preorder traversal:")
preorder(A)
print()

E.kiri = B; E.kanan = G
B.kiri = A; B.kanan = D
D.kiri = C
G.kiri = F; G.kanan = I
I.kiri = H; I.kanan = J
J.kanan = K
K.kanan = L
L.kanan = M
M.kanan = N
N.kanan = O
O.kanan = P
P.kanan = Q
Q.kanan = R
Q.kiri = R
"""

# Traversal inorder
print("Inorder traversal:")
inorder(E)
print()

R.kiri = D; R.kanan = Q
D.kiri = A; D.kanan = C
C.kiri = B
Q.kiri = E; Q.kanan = P
P.kiri = F; P.kanan = O
O.kiri = G; O.kanan = N
N.kiri = H; N.kanan = M
M.kiri = I; M.kanan = L
L.kiri = J; L.kanan = K
# Traversal postorder
print("Postorder traversal:")
postorder(R)
print()

