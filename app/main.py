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
        if ("wife" in people[index] and people[index]["wife"] is not None
                and not hasattr(result[index], "wife")):
            result[index].wife = people[index]["wife"]
            for num in range(0, len(result)):
                if result[num].name is result[index].wife:
                    result[num].husband = result[index]
                    result[index].wife = result[num]
        elif ("husband" in people[index]
              and people[index]["husband"] is not None
              and not hasattr(result[index], "husband")):
            result[index].husband = people[index]["husband"]
            for num in range(0, len(result)):
                if result[num].name is result[index].husband:
                    result[num].wife = result[index]
                    result[index].husband = result[num]
    return result
