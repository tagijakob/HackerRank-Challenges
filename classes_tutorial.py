class employee:
    ## Class variables
    raise_amount = 1.04 # will be used as instance variable
    num_of_emps = 0     # will be used as class variable

    ## attributes ---------------------------------------
    def __init__(self, first, last, pay):
        # defining instance attributes
        self.first=first
        self.last = last
        self.pay =pay
        self.email = first+"."+last+"@company.com"

        # defining global attributes (shared with all instances)
        employee.num_of_emps += 1

    ## regular methods !!!
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    ## Class variables:
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        # use self.raise_amount instead of raise_amount, because it will
        # give us the ability to change variable for one instant of the object,
        # instead of whole bunch of them

    ## class methods --------------------------------
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # emp_str = "Taguhi-Hakobyam-20000"
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    ## static methods
    # those are methods that are not using any attributes/variables from the class
    # basically could've written out of the class

    @staticmethod
    def is_workday(day):
        if (day.weekday()==5) or (day.weekday()==6):
            return False
        return True

## Developer will be the subclass, which inherits attributes and
class Developer(employee):
    raise_amount = 1.10

print("Number of employees at inception: " +str(employee.num_of_emps))
emp_1 = employee("Taguhi", "Hakobyan", 20000)
emp_2 = employee("Daria", "Kim", 30000)
print(emp_1.fullname())
print(emp_2.fullname())

print("Number of employees after a while " +str(employee.num_of_emps))
print(emp_1.first + "'s salary before the raise: " + str(emp_1.pay))
emp_1.apply_raise()
print(emp_1.first + "'s salary after the raise: " + str(emp_1.pay))


import datetime
my_day  = datetime.date(2016,7,10)
print(employee.is_workday(my_day))