from data.models.User import User
from utils.DatabaseUtils import DatabaseUtils

class CreateEmployees:
    def create_employees(self, user):
        query = (f"insert into Users.Employees(FirstName, LastName, Age, Email, Salary, Department)"
                 f" values ('{user.firstname}', '{user.lastname}', '{user.age}', '{user.email}', "
                 f"'{user.salary}', '{user.department}')")
        DatabaseUtils.execute(query)
