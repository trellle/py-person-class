class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    people = [Person(person["name"], person["age"]) for person in people_data]
    for index, person in enumerate(people_data):
        wife = people_data[index].get("wife")
        if wife:
            people[index].wife = Person.people[wife]
        husband = people_data[index].get("husband")
        if husband:
            people[index].husband = Person.people[husband]
    return people
