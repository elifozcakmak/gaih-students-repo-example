class Recipe:
    def __init__(self,materials):
        self.dict_materials= 0
        self.materials = materials
        self.quantity = 0
        self.materials_to_be_cooked=[]

    def setQuantity(self,quantity):
        self.quantity = quantity
        self.dict_materials = list(zip(self.materials,self.quantity))
    
    def printMaterials(self):
        print(self.dict_materials)
    
    def cook(self):
        print("Mix and cook the materials")

    def bake(self):
        print("Mix and bake the materials")

class Fajita(Recipe):
    def cook(self):
        print("Mix and cook the materials:", self.dict_materials)

class Pasta(Recipe):
    def cook(self):
        print("Boil water, add salt, mix, add pasta, boil for 10-15 minutes, drain the water, add oil to the pan, cook with pasta", self.dict_materials)

class Cake(Recipe):
    def bake(self):
        print("Mix and bake the materials:", self.dict_materials)

fajita = Fajita(["chicken", "onion", "red_pepper", "coriander", "garlic_clove", "olive_oil", "lime", "tabasco"])
fajita.setQuantity(["2", "1", "1", "1 tbsp", "2", "4 tbsp", "1,juiced", "4-5 drops"])
print("Fajita:", end="\n")
fajita.cook()

pasta = Pasta(["pasta","water", "salt", "oil"])
pasta.setQuantity(["1 package","1 lt","a pinch of", "1 tbsp"])
print("Pasta:", end="\n")
pasta.cook()

cake=Cake(["egg", "milk", "oil", "flour", "sugar","baking powder","vanilla"])
cake.setQuantity(["3", "1 glass", "1 glass", "3 glass", "1 glass", "1 tbsp", "1 tbsp"])
print("Cake:", end="\n")
cake.bake()
