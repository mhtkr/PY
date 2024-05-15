#Experiment - 7

class Cars:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def disp(self):
    print(f"Brand:{self.brand}, Model:{self.model}, Year:{self.year}")

v1 = Cars("Ferrari", "LaFerrari", 2019)
v2 = Cars("Bugatti", "Chiron", 2020)
v3 = Cars("Ford", "Mustang", 2022)

v1.disp()
v2.disp()
v3.disp()
