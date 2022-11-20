

class ComplexNumbers:
    #create your class here.
	def __init__(self, r, i):
		self.real=r
		self.imag=i
		
	def plus(self, c2):
		self.real= self.real+ c2.real
		self.imag=self.imag+ c2.imag
		
	def print(self):
		print(self.real," +i", self.imag)

	def multiply(self, c2):
		r=self.real
		i=self.imag
		self.real= r*c2.real - i*c2.imag
		self.imag=r*c2.imag + i*c2.real
    
#Driver's code goes here.
 

choice=int(input())
c1=ComplexNumbers(2,3)
c2=ComplexNumbers(4,5)
if choice==1:
	c1.plus(c2)
	c1.print()
elif choice==2:
	c1.multiply(c2)
	c1.print()
else:
	print()
    
    
    
    
    
    
    
    
    
