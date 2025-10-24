# class Car:          # Declare a class name
#     brand = "Toyata"    # Provide instance Attribute
#     color = "Black"     # Same as above
#
#     def feature(self):  # Declare methode/function of the product
#         print("race race race")
#
#
# my_car = Car()     # Object creation: Make a variable and call class like function)
# my_car.feature()   # Call method that you made in class Method
#
# print (my_car.brand)  # To see instance Attribute Print > object name then . then instance Attribute
# print (my_car.color)  # Same as above
# print (my_car) # to see object number
#
# sister_car = Car() # Crate object as much as you can using one class
# print (sister_car)
# brother_car = Car()
# print (brother_car)

class Student:
    student_name = "name"
    student_roll = "roll"
    def info(self):
        print (self.student_name, self.student_roll)

abc =Student()
abc.info()

print (abc.student_name)
print (abc.student_roll)



