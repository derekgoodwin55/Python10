class ImpMeas():
    def __init__(self,distance):
        
        self.distance = distance

        self.distance = self.distance.replace(" ","")
        

        if "'" in self.distance and '"' in self.distance:

            self.distance = self.distance[:-1]

            self.newlist = self.distance.split("'")

            self.inches = int(self.newlist[1]) % 12

            self.feet = int(self.newlist[0]) + (int(self.newlist[1]) // 12)

        elif "'" in self.distance and '"' not in self.distance:
            
            self.distance = self.distance[:-1]

            self.feet = int(self.distance)

            self.inches = 0

        elif "'" not in self.distance and '"' in self.distance:
            
            self.distance = self.distance[:-1]

            self.inches = int(self.distance) % 12


            self.feet = (int(self.distance) // 12)

    def __str__(self):
        return str(self.feet) + "'" + str(self.inches) + '"'

    def __repr__(self):
        return str(self.feet) + "'" + str(self.inches) + '"'

    def __add__(self, other):
        
        feet = self.feet + other.feet
        
        inches = self.inches + other.inches
        
        feet = feet + (inches // 12)
        
        inches = inches % 12
        
        mystr = str(feet) + "'" + str(inches) + '"'
        
        master_imperial = ImpMeas(mystr)
        
        return master_imperial

    def __sub__(self,other):

        a = self.feet + self.inches // 12 + self.inches % 12
        b = other.feet + other.inches // 12 + other.inches % 12

        if a > b:
            
            feet = self.feet - other.feet
            
            inches = self.inches - other.inches

        else:
            feet = other.feet - self.feet
            inches = other.inches - self.inches          
        

        feet = feet + (inches // 12)

        inches = inches % 12

        mystr = str(feet) + "'" + str(inches) + '"'

        master_imperial = ImpMeas(mystr)

        return master_imperial

    def __mul__(self,scalar):
        
        feet = self.feet * scalar
        
        inches = self.inches * scalar
        
        feet = feet + (inches // 12)
        
        inches = inches % 12
        
        mystr = str(feet) + "'" + str(inches) + '"'
        
        master_imperial = ImpMeas(mystr)
        
        return master_imperial

    def __truediv__(self,scalar):

        feet = self.feet
        
        inches = self.inches
        
        feet = feet + (inches // 12)
        
        inches = inches % 12

        total = inches + (feet * 12)

        new_total = total / scalar

        feet = new_total // 12

        inches = new_total % 12

        mystr = str(round(feet)) + "'" + str(round(inches)) + '"'
        
        master_imperial = ImpMeas(mystr)
        
        return master_imperial
        

    def __mod__(self,scalar):

        feet = self.feet
        
        inches = self.inches
        
        feet = feet + (inches // 12)
        
        inches = inches % 12

        total = inches + (feet * 12)

        new_total = total % scalar

        feet = new_total // 12

        inches = new_total % 12

        mystr = str(round(feet)) + "'" + str(round(inches)) + '"'
        
        master_imperial = ImpMeas(mystr)
        
        return master_imperial
