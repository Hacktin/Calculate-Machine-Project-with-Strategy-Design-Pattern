
import math

class Mathematical:

    def __init__(self, sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2



    def OperationofMath(self):
        print("Operation completed")



class Squart(Mathematical):

    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)

    def OperationofMath(self):
        return math.sqrt(self.sayi1)



class Factorial(Mathematical):
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)

    def OperationofMath(self):
        return math.factorial(self.sayi2)



class Sub(Mathematical):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def OperationofMath(self):
        return self.sayi1+self.sayi2


class Extraction(Mathematical):
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)

    def OperationofMath(self):
        return self.sayi1-self.sayi2




class User:

    def __init__(self,operation,sayi1,sayi2):
        self.operation=operation
        self.sayi1=sayi1
        self.sayi2=sayi2
        ##operation=Mathematical(self.sayi1,self.sayi2)



    def DoTheOperation(self):
        return self.operation.OperationofMath()







operation1=Squart(16,4)

operation2=Squart(25,16)

operation3=Factorial(4,5)

operation4=Sub(4,3)

operation5=Extraction(11,5)

User=User(operation5,operation5.sayi1,operation5.sayi2)

sonuc=User.DoTheOperation()

print(sonuc)



