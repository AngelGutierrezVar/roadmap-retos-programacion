"""
Ejercicio
"""

# Superclase

class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

# Subclases

class Dog(Animal):

    def sound(self):
        print("Guau!")


class Cat(Animal):

    def sound(self):
        print("Miau!")

def print_sound(animal: Animal):
    animal.sound()


my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Perro")
print_sound(my_dog)
my_cat = Cat("Gato")
print_sound(my_cat)

"""
Extra
"""

class Empleoyee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)

class Manager(Empleoyee):

    def coordinate_projects(self):
        print(f"{self.name} esta coordinando todos los proyectos de la empresa")

class ProjectManager(Empleoyee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_projects(self):
        print(f"{self.name} esta coordinando su proyecto")

class Programmer(Empleoyee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} esta programando en {self.language}")

    def add(self, employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee} no se añadira.")
        
my_manager = Manager(1, "Angel")
my_project_manager = ProjectManager(2, "Gutierrez", "Projecto 1")
my_project_manager2 = ProjectManager(3, "Miguel", "Projecto 2")
my_programmer = Programmer(4, "Nico", "Cobol")
my_programmer2 = Programmer(5, "Pedro", "Dart")
my_programmer3 = Programmer(6, "Maria", "Python")
my_programmer4 = Programmer(6, "Nancy", "Swift")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_projects()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()