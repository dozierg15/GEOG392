import os, sys, math
# creating the initial classes
class shape:
  def __init__(self):
      pass
  def bring_area(self):
      pass

class Rectangle(shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def bring_area(self):
        return self.l * self.w

class Triangle(shape):
   def __init__(self, b, h):
        self.b = b
        self.h = h
   def bring_area(self):
       return 0.5 * self.b * self.h

class Circle(shape):
  def __init__(self,d):
      self.radius_squared = (0.5 * d)**2
  def bring_area(self):
      return math.pi * self.radius_squared

# opens and reads path - path name does not include c: because I am running visual studio code on mac as opposed to windows 
i_handle = open('/Users/garrettdozier/Desktop/Classes/Fall 21/GEOG 392/shapes.txt')
# creating variable of lines read from text file
data_lines_overall = i_handle.readlines()
print(data_lines_overall)
# seeking the 0
i_handle.seek(0)
# stripping then splitting first value
data_text_initial = i_handle.read().strip().split("\n")
print(data_text_initial)
# closing file
i_handle.close()
# creating for and else if statements to return value of shape calculations
for line in data_text_initial:
  data_items_part = line.split(",")
  if data_items_part[0] == "Rectangle":
      r = Rectangle(float(data_items_part[1]),float(data_items_part[2]))
      print("Rectangle Area:",r.bring_area())
  elif data_items_part[0] == "Triangle":
      t = Triangle(float(data_items_part[1]),float(data_items_part[2]))
      print("Triangle Area:",t.bring_area())
  else:
      c = Circle(float(data_items_part[1]))
      print("Circle Area:", c.bring_area())
 
 

