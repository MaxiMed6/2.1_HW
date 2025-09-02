class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: name={self.name}, salary={self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self,name, salary)
        self.department = department

    def __str__(self):
        return f"Manager: name={self.name}, salary={self.salary}, department={self.department}"


class Developer (Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self,name, salary)
        self.programming_language = programming_language


    def __str__(self):
        return f"Developer: name={self.name}, salary={self.salary}, programming_language={self.programming_language}"



class TeamLead (Manager, Developer):
    def __init__(self,name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def __str__(self):
        return f"TeamLead: name={self.name}, salary={self.salary}, department={self.department}, programming_language={self.programming_language}, team_size={self.team_size}"



if __name__ == "__main__":
    team_lead = TeamLead("Dean Winchester", 20000, "Impala_lover", "Python", 3)
    print(team_lead)


if __name__ == "__main__":
    second_team_lead = TeamLead("Sam Winchester", 24000, "College_student","Java", 6)
    print(second_team_lead)

