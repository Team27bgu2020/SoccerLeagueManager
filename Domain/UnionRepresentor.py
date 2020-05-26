from Domain.SignedUser import SignedUser


class UnionRepresentor(SignedUser):

    def __init__(self, user_name, password, name, birth_date, ip_address, user_id, salary):
        super().__init__(user_name, password, name, birth_date, ip_address, user_id)
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError('Salary cant be a negative number')

        self.__salary = salary
