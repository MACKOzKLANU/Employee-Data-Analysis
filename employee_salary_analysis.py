import csv
from matplotlib import pyplot as plt
from datetime import datetime


class Employee:
    def __init__(self, employee_id, name, department, position, salary, date_of_joining):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary
        self.date_of_joining = date_of_joining


def load_data(file_path):
    try:
        employees = []

        with open(file_path, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                employee = Employee(row[0], row[1], row[2], row[3], row[4], row[5])
                employees.append(employee)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return employees


def print_data(employees):
    data = employees
    for employee in data:
        print(employee.employee_id, employee.name, employee.department, employee.position, employee.salary, employee.date_of_joining)


def clean_data(employees):
    pass


def average_salary_by_department(employees):
    data = employees
    list_of_departaments = []
    for employee in data:
        list_of_departaments.append(employee.department)

    departament_salary_list = {}
    for employee in data:
        if employee.department in departament_salary_list:
            departament_salary_list[employee.department] += int(employee.salary)
            print(departament_salary_list[employee.department])
        else:
            departament_salary_list[employee.department] = int(employee.salary)

    for data in departament_salary_list:
        print(data, departament_salary_list[data])
        departament_salary_list[data] = int(departament_salary_list[data]) / int(list_of_departaments.count(data))
        print(departament_salary_list[data])
        print(list_of_departaments.count(data))
    print(departament_salary_list)

    plt.bar(departament_salary_list.keys(), departament_salary_list.values())
    plt.xlabel('Department')
    plt.ylabel('Average Salary')
    plt.title('Average Salary by Department')
    plt.show()


def salary_distribution_histogram(employees):
    data = employees
    salary_list = []
    for employee in data:
        salary_list.append(employee.salary)

    plt.hist(salary_list, bins=20, edgecolor='black')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.title('Salary Distribution Histogram')
    plt.show()


def top_5_earners_pie_chart(employees):
    data = employees
    top_5_earners_dict = {}

    sorted_employees = sorted(data, key=lambda x: int(x.salary), reverse=True)
    top_5_earners = sorted_employees[:5]

    for employee in top_5_earners:
        top_5_earners_dict[employee.name] = int(employee.salary)
    print(top_5_earners_dict)

    plt.pie(top_5_earners_dict.values(), labels=top_5_earners_dict.keys(), autopct='%1.1f%%')
    plt.title('Top 5 Earners Proportion of Total Payroll')
    plt.show()


def box_plot_by_position(employees):
    positions_salary = {}

    for employee in employees:
        if employee.position in positions_salary:
            positions_salary[employee.position].append(int(employee.salary))
        else:
            positions_salary[employee.position] = [int(employee.salary)]

    plt.boxplot(positions_salary.values(), labels=positions_salary.keys())
    plt.xlabel('Position')
    plt.ylabel('Salary')
    plt.title('Box Plot of Salaries by Position')
    plt.show()


def scatter_plot_service_vs_salary(employees):
    current_year = datetime.now().year
    print(current_year)
    working_time_dict = {}
    for employee in employees:
        if employee.salary in working_time_dict:
            working_time_dict[employee.salary].append(int(current_year - int(employee.date_of_joining)))
        else:
            working_time_dict[employee.salary] = [current_year - int(employee.date_of_joining)]
    print(working_time_dict)

    plt.scatter(working_time_dict.values(), working_time_dict.keys())

    plt.xlabel('Years of Service')
    plt.ylabel('Salary')
    plt.title('Scatter Plot of Years of Service vs. Salary')
    plt.show()


# average_salary_by_department(load_data("data.csv"))
# salary_distribution_histogram(load_data("data.csv"))
# top_5_earners_pie_chart(load_data("data.csv"))
# box_plot_by_position(load_data("data.csv"))
# scatter_plot_service_vs_salary(load_data("data.csv"))