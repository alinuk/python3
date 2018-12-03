class Employee:
  
   num_of_emps = 0
   raise_amount = 1.04   #class variable
   
   def __init__(self, first, last, pay):
     #instances
       self.first = first                         
       self.last  = last
       self.pay   = pay
       self.email = first + '.' + last + '@company.com'
       
       Employee.num_of_emps += 1 #create new employee
       
   def fullname(self):
       return '{} {}'.format(self.first, self.last)
       
       
       
   def apply_raise(self):   #method
       self.pay = int(self.pay * Employee.apply_raise)
       
   @classmethod
   def set_raise_amt(cls, amount):
       cls.raise_amt = amount
     
       
       
       
 
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)
 
Employee.set_raise_amt(1.06)



print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(Employee.num_of_emps)

#print(Employee.__dict__)
#print(emp_1.__dict__)










 
 