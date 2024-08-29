class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        p = file.read()
        file.close()
        return p
    def add(self, *products):
        pro = self.get_products()
        for new_product  in products:
                if pro.find(f'{new_product.name}') == -1: #Проверка вхождения строки 
                    file = open(self.__file_name, 'a')
                    file.write(f'{new_product}\n')
                    file.close()
                else: print(f'Продукт {new_product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5,'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())