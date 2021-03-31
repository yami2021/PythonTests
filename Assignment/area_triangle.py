class AreaTriangle:

    def inputdetails(self):
            base = float(input("Enter your value of base: "))
            height = float(input("Enter your value of height: "))

            triangle.tri_area(base,height)


    def tri_area(self,base,height):
        self.base=base
        self.height=height
        area = (self.base * self.height) /  2
        print("The area of Triangle is {}".format(area))


triangle = AreaTriangle()
triangle.inputdetails()

answer = input("do you want area of triangle? (Y?N)")
if answer == "y":
    triangle.inputdetails()
else :
      print("Thank You")
                  
                  


