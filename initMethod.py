class Employee:
   
   def __init__(self, first, last, pay):
       self.first = first
       self.last  = last
       self.pay   = pay
       self.email = first + '.' + last + '@company.com'
 
emp_1 = Employee('Corey', 'Schafer', 5000)
 
print(emp_1.email)


'''
print(emp_2)
 
 #instances----attributes
 
emp_1.first = 'Corey'
emp_1.last = 'Shafer'
emp_1.email = 'shafer@email.com'
 
emp_2.first = 'Test'
emp_2.last = 'emp2'
emp_2.email = 'test@email.com'
 
print(emp_1.email)
print(emp_2.email) '''
 
 