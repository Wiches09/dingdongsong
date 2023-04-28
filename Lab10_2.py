""" Lab 10_2 """

class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getWeight(self):
        return self.weight
    
    def getCost(self):
        return self.price / self.weight


def knapsack(amount, itemList):
    weight = 0
    itemList.sort(key=lambda x: x.getCost() ,reverse = True)
    total = 0
    print("Knapsack Size:", amount, "kg")
    print("=====================================")
    counter = 0
    while True:
        item = itemList[counter]
        weight += item.getWeight()
        if weight <= amount:
            counter += 1
            total += item.getPrice()
            print(item.getName(), "->", item.getWeight(), "kg ->", item.getPrice(), "THB")
        else:
            break
        
    print("Total:", total, "THB")

item1 = Item('stereo', 3000, 3)
item2 = Item('laptop', 2000, 2)
item3 = Item('guitar', 1500, 1.5)
itemList = [item1, item2, item3]
knapsack(3.5, itemList)

print()
print()
print("_____________________________________________________________________________")
print()
print()


item1 = Item('tablet', 7000, 0.5)
item2 = Item('perfume', 6000, 0.5)
item3 = Item('guitar', 9000, 1)
item4 = Item('air purifier', 9000, 2)
item5= Item('watch', 8000, 0.5)
itemList = [item1, item2, item3, 
item4, item5]
print()
knapsack(3, itemList)
