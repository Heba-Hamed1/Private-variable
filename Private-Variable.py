class Employee:
    def __init__(self, Name, ID, Address):
        self.__Name = Name
        self.__ID = ID
        self.__Address = Address
        
    def __display_info(self):
        print("Name:", self.__Name)
        print("ID:", self.__ID)
        print("Address:", self.__Address)
        
    def accessPrivateFunction(self):
        self.__display_info()
        
    def get_Name(self):
        return self.__Name 
        
    def set_name(self, Name):
        self.__Name = Name 
        
    def get_ID(self):
        return self.__ID
        
    def set_ID(self, ID):
        self.__ID = ID
  
    def get_Address(self):
        return self.__Address
        
    def set_Address(self, Address):
        self.__Address = Address 
        

obj = Employee("Heba", 2033003, "Egypt")
obj.accessPrivateFunction()
obj.set_ID(2003)
obj.set_name("Heba Hamed")
obj.set_Address("Madrid")
obj.accessPrivateFunction()  

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        