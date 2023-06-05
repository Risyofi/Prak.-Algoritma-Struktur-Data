class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None
        
    def preorderTrav(subpohon):
        if subpohon is not None:
            print(subpohon.data)
            preorderTrav(subpohon.kiri)
            preorderTrav(subpohon.kanan)

    def inorderTrav(subpohon):
        if subpohon is not None:
            inorderTrav(subpohon.kiri)
            print(subpohon.data)
            inorderTrav(subpohon.kanan)

    def postorderTrav(subpohon):
        if subpohon is note None:
            postorderTrav(subpohon.kiri)
            postorderTrav(subpohon.kanan)
            print(subpohon.data)
