class Pizza(object):
    
    @classmethod
    def produce(cls,k,l):
    	print "in class method produce "
    	return cls(k,l)
    @staticmethod
    def mix_ingredients(x, y):
    	print 'x ' + str(x) + ' and ' + str(y)
        return x + y
    def __init__(self,cheese,vegetables):
 		self.cheese=cheese
 		self.vegetables=vegetables   	
    def cook(self):
        print self.mix_ingredients(self.cheese, self.vegetables)
        return self.mix_ingredients(self.cheese, self.vegetables)     
	
        
    
class Pizzac(Pizza):
	abc=3
	@staticmethod
	def mix_ingredients(x, y):    
	    print 'child x ' + str(x) + ' and ' + str(y)
	    return (x + y)*10  
	
	

a=Pizza(3,5);
#print(a);
#Pizza(4,7).cook();

b=Pizzac(7,7)
b.cook()
b.mix_ingredients(8,8)
Pizzac.mix_ingredients(10,10)
print(str(Pizzac.abc))
instn=Pizza.produce(100,100)
instn.cook()



import abc
 
class BasePizza(object):
    __metaclass__  = abc.ABCMeta
 
    @abc.abstractmethod
    def get_ingredients(self):
         """Returns the ingredient list."""
 
class DietPizza(BasePizza):
	@staticmethod
	def get_ingredients():
		return None
        
hh=DietPizza()
print hh.get_ingredients()
