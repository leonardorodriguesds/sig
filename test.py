class User:
    def __init__(self, first_name, last_name, register):
        self.first_name = first_name
        self.last_name = last_name
        self.register = register
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def gerRegister(self):
        return self.register
    def setFirstName(self, first_name):
        self.first_name = first_name
    def setLastName(self, last_name):
        self.last_name = last_name
    def setRegister(self, register):
        self.register = register

class Petient(User):
    def __init__(self, first_name, last_name, register, date_birth):
        super(Petient, self).__init__(first_name, last_name, register)

petient = Petient('Teste', 'Teste2', '0101', '1')
print(petient.first_name)