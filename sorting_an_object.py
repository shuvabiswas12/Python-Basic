class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, {})'.format(self.name, self.age, self.salary)


e1 = Employee("John", 20, 15000)
e2 = Employee("Paulo", 40, 55000)
e3 = Employee("Adidas", 30, 20000)

# employee = [e1, e2, e3]
employee = (e1, e2, e3)


def employee_sort(emp):
    return emp.name


sorted_employee = sorted(employee, key=employee_sort, reverse=True)
print(sorted_employee)


from operator import attrgetter
sorted_employee_2 = sorted(employee, key=attrgetter("age"))
print(sorted_employee_2)


# abs value sorted

unsorted_list = [-4, -3, -6, 3, 5, 1]

sorted_list = sorted(unsorted_list, key=abs)  # it would be like [1, 2, 3, -4, -5 ,-6]
print(sorted_list)

sorted_list_2 = sorted(unsorted_list)
print(sorted_list_2)  # it would be like [-6, -4, -3, 1, 2, 3]

