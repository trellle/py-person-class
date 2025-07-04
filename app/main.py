class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for elem in people:
        person = Person(elem["name"], elem["age"])
        if elem.get("wife"):
            person.wife = elem["wife"]
        elif elem.get("husband"):
            person.husband = elem["husband"]
        result.append(person)
        person = None
    for elem1 in result:
        for elem2 in result:
            if hasattr(elem1, "wife") and elem1.wife is elem2.name:
                elem2.husband = elem1
                elem1.wife = elem2
            elif hasattr(elem1, "husband") and elem1.husband is elem2.name:
                elem2.wife = elem1
                elem1.husband = elem2
    return result
