import pytest

from data.models.User import User
from tests.create_employees import CreateEmployees
from utils.DatabaseUtils import DatabaseUtils

class TestMigration:

    @staticmethod
    def get_user_data():
        query = "select * from Users.users;"
        return DatabaseUtils.select(query)

    @pytest.mark.parametrize("first_name, last_name, age, email, salary, department", get_user_data())
    def test_migration(self, first_name, last_name, age, email, salary, department):
        user = User(first_name, last_name, age, email, salary, department)
        create_employee = CreateEmployees()
        create_employee.create_employees(user)
