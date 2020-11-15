People = ["John", "Paul", "Sara", "Susan"]
for persons in People:
    print(f"Current Person: {persons}")


#Breaking out of a loop
for persons in People:
    if persons == "Sara":
        break
    print(f"Current Person: {persons}")
      
#Continue: This will not break the loop, rather, it will skip and cont
for persons in People:
    if persons == "Sara":
        continue
    print(f"Curent Person: {persons}")


class Run:
    #constructor
    def __Sun__(self, time, place):
        self.time = time
        self.place = place
    
def greeting(self):
    return f"Good {self.time}, are you {place}"

Mary = Run("morning","home")

print(Mary.greeting())

