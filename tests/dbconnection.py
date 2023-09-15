from utils.DatabaseUtils import DatabaseUtils

select_query = "SELECT ProductName FROM test.product;"

result_set = DatabaseUtils.select(select_query)
print(result_set)