# Tuples used in real time scenario and suppose if i want to delete emp_id = 102
emp_id = (101, 102, 103)
tmp_emp_id = list(emp_id)
del tmp_emp_id[1]
emp_id = tuple(tmp_emp_id)
print(type(tmp_emp_id))
print(emp_id)
print(type(emp_id))
