import csv
from matplotlib import pyplot as plt
from datetime import datetime

class Employee:
    def __init__(self, employee_id, name, department, position, salary, date_of_joining):
        """
        Initializes an Employee object.

        Parameters:
        - employee_id (str): Unique identifier for the employee.
        - name (str): Name of the employee.
        - department (str): Department to which the employee belongs.
        - position (str): Job position of the employee.
        - salary (str): Salary of the employee.
        - date_of_joining (str): Date when the employee joined.

        Returns:
        - None
        """
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary
        self.date_of_joining = date_of_joining


def load_data(file_path):
    """
    Loads employee data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file containing employee data.

    Returns:
    - List[Employee]: List of Employee objects.
    """
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
    """
    Prints employee data.

    Parameters:
    - employees (List[Employee]): List of Employee objects.

    Returns:
    - None
    """
    data = employees
    for employee in data:
        print(employee.employee_id, employee.name, employee.department, employee.position, employee.salary, employee.date_of_joining)


def clean_data(employees):
    """
    To be implemented.
    """
    pass


def average_salary_by_department(employees):
    """
    Calculates and displays the average salary by department.

    Parameters:
    - employees (List[Employee]): List of Employee objects.

    Returns:
    - None
    """
    data = employees
    list_of_departments = []
    for employee in data:
        list_of_departments.append(employee.department)

    department_salary_list = {}
    for employee in data:
        if employee.department in department_salary_list:
            department_salary_list[employee.department] += int(employee.salary)
        else:
            department_salary_list[employee.department] = int(employee.salary)

    for data in department_salary_list:
        department_salary_list[data] = int(department_salary_list[data]) / int(list_of_departments.count(data))

    plt.bar(department_salary_list.keys(), department_salary_list.values())
    plt.xlabel('Department')
    plt.ylabel('Average Salary')
    plt.title('Average Salary by Department')
    plt.show()


def salary_distribution_histogram(employees):
    """
    Displays a histogram of salary distribution.

    Parameters:
    - employees (List[Employee]): List of Employee objects.

    Returns:
    - None
    """
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
    """
    Displays a pie chart of the top 5 earners' proportion of the total payroll.

    Parameters:
    - employees (List[Employee]): List of Employee objects.

    Returns:
    - None
    """
    data = employees
    top_5_earners_dict = {}

    sorted_employees = sorted(data, key=lambda x: int(x.salary), reverse=True)
    top_5_earners = sorted_employees[:5]

    for employee in top_5_earners:
        top_5_earners_dict[employee.name] = int(employee.salary)

    plt.pie(top_5_earners_dict.values(), labels=top_5_earners_dict.keys(), autopct='%1.1f%%')
    plt.title('Top 5 Earners Proportion of Total Payroll')
    plt.show()


def box_plot_by_position(employees):
    """
    Displays a box plot of salaries by position.

    Parameters:
    - employees (List[Employee]): List of Employee objects.

    Returns:
    - None
    """
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
    """
    Displays a scatter plot of years of service vs. salary.

    Parameters:
    - employees (List[Employee]): List of Employee objects.

    Returns:
    - None
    """
    current_year = datetime.now().year
    working_time_dict = {}
    for employee in employees:
        if employee.salary in working_time_dict:
            working_time_dict[employee.salary].append(int(current_year - int(employee.date_of_joining)))
        else:
            working_time_dict[employee.salary] = [current_year - int(employee.date_of_joining)]

    plt.scatter(working_time_dict.values(), working_time_dict.keys())
    plt.xlabel('Years of Service')
    plt.ylabel('Salary')
    plt.title('Scatter Plot of Years of Service vs. Salary')
    plt.show()


# Example Usage
# Uncomment the following lines and provide the correct file path
# for your employee data CSV file.

# employee_data = load_data("data.csv")
# average_salary_by_department(employee_data)
# salary_distribution_histogram(employee_data)
# top_5_earners_pie_chart(employee_data)
# box_plot_by_position(employee_data)
# scatter_plot_service_vs_salary(employee_data)
