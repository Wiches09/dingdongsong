""" Lab 08 """
class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None]
        self.n = cap
    

    def hashFunction(self, mykey):
        key = mykey % self.n
        return key


    def reHashFunction(self, hashkey):
        if hashkey not in self.hashtable:
            hashkey += 1
            return hashkey
        else:
            self.reHashFunction(hashkey)
    
    def insertData(self, student_obj):
        key = self.hashFunction(student_obj.getID())
        if self.hashtable[key] == None:
            self.hashtable[key] = student_obj
            print("insert", student_obj.getID(), "at index", key)
        else:
            key = self.reHashFunction(key)
            if self.hashtable[key] != None:
                print("cant insert data")
            else:
                self.hashtable[key] = student_obj
                print("insert", student_obj.getID(), "at index", key)


    def searchData(self, key):
        p = self.hashFunction(key)
        while True:
            if self.hashtable[p] != None:
                if self.hashtable[p].getID() == key:
                    print("Found", key ,"at index", p)
                    return self.hashtable[p]
                else:
                    p = self.reHashFunction(p)
                    if p > self.n:
                        print(key,"does not exist.")
                        return None
                    else:
                        continue
            else:
                print(key,"does not exist.")
                return None
            
            
        

class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getGPA(self):
        return self.gpa
    
    def printDetail(self):
        print("ID: " + str(self.id))
        print("Name: "+ self.name)
        print("GPA: "+ str(self.gpa))
        
s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)
myHash = ProbHash(3)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)

print()
std = myHash.searchData(65070001)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070077)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070021)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070042)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070032)
