class item:
    def __init__(self, id, itemName, price):
        self.id = id
        self.itemName = itemName
        self.price = price
        
def display (l , cName , cAddress):
    total = 0
    print("\n\n\n")
    print("\t     store Code      ")
    print("\t  -----------------     ")
    print(f"Name : {cName} \t Address : {cAddress}")
    for obj in l:
        print(f"Id : {obj.id}\t ItemName : {obj.itemName}\tPrice : {obj.price}")
        print("-----------------------------------------------------")
        total += obj.price
    print(f"\t\tTotal : {total}")
    print("\n")
    print("\t -------Thanks for visiting--------- ")
    print("\n\n")
            
list = []

print("\n\n")
print("Hello Everyone ........")
cName = input("Enter your name =      ")
cAddress = input("Enter your address =      ")
totalItems = int(input("Enter total item =     "))
print("\n")

for i in range(0 , totalItems):
    id = (i+1)
    name = input("Enter item name =      ")
    price = int(input("Enter price =     "))
    list.append(item(id , name , price ))
    
display(list ,cName , cAddress)
