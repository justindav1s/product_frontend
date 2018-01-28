class Product:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def toString(self):
        print ("Product id : ", self.id, ", name: ", self.name)