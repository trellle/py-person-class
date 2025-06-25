class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    result = []
    for index in range(0, len(people)):
        result.append(Person(people[index]["name"], people[index]["age"]))
    for index in range(0, len(people)):
        if people[index]["wife"] is not None and not result[index].wife:
            result[index].wife = people[index]["wife"]
            for num in range(0, len(result)):
                if result[num].name is result[index].wife:
                    result[num].husband = result[index].name
        elif (people[index]["husband"] is not None
              and not result[index].husdand):
            result[index].husband = people[index]["husband"]
            for num in range(0, len(result)):
                if result[num].name is result[index].husband:
                    result[num].wife = result[index].name
    return result
