austin = {'name': 'Austin',
        'age': 18,
        'cats': True,
        'hair_color': 'Brown'
}

ezan = {'name': 'Ezan',
        'age': 75,
        'cats': False,
        'hair_color': 'Turquoise'
}

print austin
print ezan
class Person(object):
    def __init__(self, name, age, cats, hair_color):
        self.name= 'Ausitn'
        self.age= 18
        self.cats= 'True'
        self.hair_color= 'Brown'



austin = Person(
    name='Austin',
    age= 18,
    cats= True,
    hair_color= 'Brown'
)



ezan = Person(
    name='Ezan',
    age= 75,
    cats= False,
    hair_color= 'Turquoise'
)
