class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health ="good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Add your method here!
    def description(self):
        print self.name
        print self.age
        
print Animal("sedred",8)
hippo = Animal("herty",7)
sloth = Animal("her",57)
ocelot = Animal("herthjhjy",75)
print hippo.health
print sloth.health
print ocelot.health
print hippo.description()
