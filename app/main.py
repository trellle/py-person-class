class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(elem["name"], elem["age"]) for elem in people]
    for index in range(0, len(people)):
        if ("wife" in people[index] and people[index]["wife"] is not None
                and not hasattr(result[index], "wife")):
            result[index].wife = people[index]["wife"]
            for elem in result:
                if elem.name is result[index].wife:
                    elem.husband = result[index]
                    result[index].wife = elem
        elif ("husband" in people[index]
              and people[index]["husband"] is not None
              and not hasattr(result[index], "husband")):
            result[index].husband = people[index]["husband"]
            for elem in result:
                if elem.name is result[index].husband:
                    elem.wife = result[index]
                    result[index].husband = elem
    return result
