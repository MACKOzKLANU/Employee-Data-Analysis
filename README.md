# Employee Data Analysis

This Python script analyzes employee data stored in a CSV file. The script defines a class `Employee` to represent individual employees and provides functions to load, clean, and visualize the data.

## Table of Contents
- [Employee Data Analysis](#employee-data-analysis)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Usage](#usage)
  - [Functions](#functions)
    - [1. `load_data(file_path)`](#1-load_datafile_path)
    - [2. `print_data(employees)`](#2-print_dataemployees)
    - [3. `clean_data(employees)`](#3-clean_dataemployees)
    - [4. `average_salary_by_department(employees)`](#4-average_salary_by_departmentemployees)
    - [5. `salary_distribution_histogram(employees)`](#5-salary_distribution_histogramemployees)
    - [6. `top_5_earners_pie_chart(employees)`](#6-top_5_earners_pie_chartemployees)
    - [7. `box_plot_by_position(employees)`](#7-box_plot_by_positionemployees)
    - [8. `scatter_plot_service_vs_salary(employees)`](#8-scatter_plot_service_vs_salaryemployees)
  - [Example](#example)

## Overview
This script is designed for the analysis of employee data stored in a CSV file. It includes functions to load the data, clean it, and visualize various aspects such as average salary by department, salary distribution histogram, top 5 earners pie chart, box plot of salaries by position, and a scatter plot of years of service vs. salary.

## Usage
1. Ensure you have Python installed on your system.
2. Clone the repository or download the script.
3. Provide your employee data in a CSV file (e.g., "data.csv").
4. Modify the script to specify the correct file path in the function calls.
5. Run the script.

## Functions

### 1. `load_data(file_path)`
   - **Input:** `file_path` - Path to the CSV file containing employee data.
   - **Output:** List of `Employee` objects.

### 2. `print_data(employees)`
   - **Input:** List of `Employee` objects.
   - **Output:** Prints employee data.

### 3. `clean_data(employees)`
   - **Input:** List of `Employee` objects.
   - **Output:** To be implemented.

### 4. `average_salary_by_department(employees)`
   - **Input:** List of `Employee` objects.
   - **Output:** Displays a bar chart of average salary by department.

### 5. `salary_distribution_histogram(employees)`
   - **Input:** List of `Employee` objects.
   - **Output:** Displays a histogram of salary distribution.

### 6. `top_5_earners_pie_chart(employees)`
   - **Input:** List of `Employee` objects.
   - **Output:** Displays a pie chart of the top 5 earners' proportion of the total payroll.

### 7. `box_plot_by_position(employees)`
   - **Input:** List of `Employee` objects.
   - **Output:** Displays a box plot of salaries by position.

### 8. `scatter_plot_service_vs_salary(employees)`
   - **Input:** List of `Employee` objects.
   - **Output:** Displays a scatter plot of years of service vs. salary.

## Example
```python
# Example Usage
# Uncomment the following lines and provide the correct file path
# for your employee data CSV file.

# employee_data = load_data("data.csv")
# average_salary_by_department(employee_data)
# salary_distribution_histogram(employee_data)
# top_5_earners_pie_chart(employee_data)
# box_plot_by_position(employee_data)
# scatter_plot_service_vs_salary(employee_data)
```

