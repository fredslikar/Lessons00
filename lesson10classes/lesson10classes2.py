
class House():                                                                                      
    """house desctiption"""
    def __init__(self, street, number):
        """propertis of house"""                                                                    
        self.street=street                                                                         
        self.number=number
        self.age=0
    
    def build(self):                                                                                
        """Build house"""                                                                           
        print("House on the street " + self.street + "nmbr. " + str(self.number) + " is building")  

    def aoh(self, year):
        """age of house"""
        self.age += year

House1 = House("Kyivska ",20)                                                                             
House2 = House("Kyivska ",21)
House3 = House("Dniprovska ",15)


print(House1.street)
print(House1.number)

House2.build()

House1.aoh(5)
print(House1.age)                                                                                   

class ProspectHouse(House):    
    """Houses on the prospect"""
    def __init__(self, prospect, number):
        super().__init__(number)
        self.prospect = prospect

PrHouse = ProspectHouse("Shevchenka",7)
print(PrHouse)



