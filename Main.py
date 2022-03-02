from Dog import Dog

Rex = Dog("Golden", 8)      # make a Dog instance, Rex
Spot = Dog("Pit Bull", 12)  # make another Dog instance, Spot
Rex.addTrick("roll over")   # add a trick to Rex
Spot.addTrick("sit")        # add a trick to Spot
Spot.addTrick("play dead")  # add another trick to Spot

print(Rex.kind)             # print kind, which is inherited by all Dogs
print(Spot.kind)
print(Rex.breed)            # breed is specified at instantiation
print(Rex.age)              # age is specified at instantiation
print(Spot.breed)
print(Spot.age)
print(Rex.tricks)           # all dogs have a tricks array
print(Spot.tricks)

Spot.age += 1               # you can modify Dog properties
Spot.weight = 70            # i just added a property to Spot from outside the class.  this is bad form.

print(Spot.age)             # see the age has been modified
print(Spot.weight)          # you're allowed to do this, but ew.
print(Spot.bark())          # the bark method returns "arf"