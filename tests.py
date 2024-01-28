import unittest
from employee_salary_analysis import Employee, load_data, print_data, average_salary_by_department, salary_distribution_histogram, top_5_earners_pie_chart, box_plot_by_position, scatter_plot_service_vs_salary


class TestEmployeeSalaryAnalysis(unittest.TestCase):
    def setUp(self):
        self.file_path = "data.csv"

    def test_load_data_success(self):
        employees = load_data(self.file_path)
        self.assertTrue(len(employees) > 0)

    # def test_load_data_file_not_found(self):
    #     with self.assertRaises(FileNotFoundError):
    #         load_data("nonexistent_file.csv")
    def test_employee_instance_creation(self):
        employee = Employee("001", "John Doe", "HR", "Manager", 50000, "2022")

        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.employee_id, "001")
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.department, "HR")
        self.assertEqual(employee.position, "Manager")
        self.assertEqual(employee.salary, 50000)
        self.assertEqual(employee.date_of_joining, "2022")


if __name__ == '__main__':
    unittest.main()
