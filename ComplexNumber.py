class Complex():

    real = (float)
    imaginary = (float)

    def __init__(self, realnumber, imaginarynumber):
        self.real = realnumber
        self.imaginary = imaginarynumber
        
    def Add(self, Complexnumber):
        return Complex(self.real + Complexnumber.real , self.imaginary + Complexnumber.imaginary)
    def Subtract(self, Complexnumber):
        return Complex(self.real-Complexnumber.real, self.imaginary - Complexnumber.imaginary)
    def Multiply(self, Complexnumber):
        return Complex((self.real*Complexnumber.real) - (self.imaginary*Complexnumber.imaginary), (self.real*Complexnumber.imaginary) + (self.imaginary*Complexnumber.real))
    def Divide(self, Complexnumber):
        sr = self.real
        cr = Complexnumber.real
        si = self.imaginary
        ci = Complexnumber.imaginary
        Div = cr**2 + ci**2
        return Complex((sr*cr + si*ci)/Div , (si*cr -sr*ci)/Div)

    def display(self):
        if self.imaginary >= 0:
            print("{} + {}i".format(self.real, self.imaginary))
        elif self.imaginary < 0:
            print("{} - {}i".format(self.real, -self.imaginary))
    
        


if __name__ == "__main__":

    c1 = Complex(realnumber=1, imaginarynumber =2)
    c2 = Complex(realnumber=3, imaginarynumber =4)

    c3= c1.Add(c2)
    c3.display()

    c4=c1.Subtract(c2)
    c4.display()

    c5 = c1.Multiply(c2)
    c5.display()

    c6 = c1.Divide(c2)
    c6.display()
    