class Person:
    def __init__(self, name, gender, age, birthday):
        self.name = name
        self.gender = gender
        self.age = age
        self.birthday = birthday
    def describe_person(self):
        print(f"My friend is called {self.name} and she is a {self.gender}."
             f" She is {self.age} years old." 
             f" {self.name} celebrates birthday on {self.birthday} each year.")
my_person = Person("Jane", "female", 24, "3-02-2000")
my_person.describe_person()
my_person = Person("Jack", "male", 27, "4-02-2011")
my_person.describe_person()
my_person = Person("Faith", "female", 28, "3-11-1996")
my_person.describe_person()
my_person = Person("Lilian", "female", 36, "4-08-1989")
my_person.describe_person()
my_person = Person("Glady", "female", 32, "20-02-1992")
my_person.describe_person()
