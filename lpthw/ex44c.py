class Parent(object):

    def altered(self):
         print "PARENT altered()"
         
class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
    
    
dad = Parent()
son = Child()

dad.altered()
son.altered() # Defined the classes "Parent" and "Child" and printed out Parent and Child that is before and after altered. 
