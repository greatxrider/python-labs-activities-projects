class Complex:
    # Attributes
    real = 0
    imaginary = 0

    # Methods
    def __init__(self, real=real, imaginary=imaginary):
        self.real = real 
        self.imaginary = imaginary 

    def add(self, ComplexNumber):
        return Complex(self.real+ComplexNumber.real, self.imaginary+ComplexNumber.imaginary)

    def subtract(self, ComplexNumber):
        return Complex(self.real-ComplexNumber.real, self.imaginary-ComplexNumber.imaginary)

    def multiply(self, ComplexNumber):
        real      = self.real*ComplexNumber.real      - self.imaginary*ComplexNumber.imaginary
        imaginary = self.real*ComplexNumber.imaginary + self.imaginary*ComplexNumber.real 
        return Complex(real, imaginary)

    def divide(self, ComplexNumber):
        conjugate = Complex(ComplexNumber.real, -ComplexNumber.imaginary)
        numerator = self.multiply(conjugate)
        denominator = ComplexNumber.multiply(conjugate)
        return Complex(numerator.real/denominator.real, numerator.imaginary/denominator.real)

    def display(self):
        if self.imaginary<0:
            print ("{} - {}i".format(self.real, -self.imaginary))
        else:
            print ("{} + {}i".format(self.real, self.imaginary))
            


if __name__ == "__main__":
    c1 = Complex(real=3.0, imaginary=-2.0)
    c2 = Complex(real=2.0, imaginary=-6.0)
    c3 = c1.divide(c2)
    c3.display()
    
    
