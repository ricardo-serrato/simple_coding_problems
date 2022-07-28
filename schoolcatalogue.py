class School:
    def __init__(self, name, level, numberOfstudents):
        self.name = name
        self.level = level
        self.numberOfstudents = numberOfstudents

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfstudents} students. "

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberofstudents(self):
        return self.numberOfstudents

    def set_numberofstudnets(self, number):
        self.numberOfstudents = number


class PrimarySchool(School):
    def __init__(self, name, numberOfstudent, pickupPolicy):
        super().__init__(name, 'primary', numberOfstudent)
        self.pickupPolicy = pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + f"The pickup policy is:  {self.pickupPolicy}"

    def get_policy(self):
        return self.pickupPolicy


class Highschool(School):
    def __init__(self, name, numberOfstudent, sportsTeam):
        super().__init__(name, 'High', numberOfstudent)
        self.sportsTeam = sportsTeam

    def get_sportsteam(self):
        return self.sportsTeam

    def __repr__(self):
        x = super().__repr__()
        return x + f"Our school has the following sports: {self.sportsTeam}"


policy = 'This is the policy that students must follow'
ps = PrimarySchool('python2', 500, policy)
print(ps.get_name())
print(ps.get_level())
print(ps.get_numberofstudents())
ps.set_numberofstudnets(800)
print(ps.get_numberofstudents())
print(ps.get_policy())
print(ps)
print(' ')
s1 = School('python', 'middle', 500)
print(s1.get_name())
print(s1.get_level())
print(s1.get_numberofstudents())
s1.set_numberofstudnets(800)
print(s1.get_numberofstudents())
print('')
hs = Highschool('python6', 500, ['Tennis', 'Basketball'])
print(hs.get_sportsteam())
print(hs)
