# CODETECH-TASK_2

COMPANY : CODETECH IT SOLUTIONS

NAME : Santosh jagan kakde

INTERN ID : CT08JNL

**DOMAIN NAME ** : Python Programming

BATCH DURATIONS : 5th, 2025 to February 5th, 2025

MENTOR NAME : Neela Santhosh Kumar

Task Description: Generate and Analyze Data Report from CSV
Objective:
The task is to create a Python script that reads data from a CSV file, performs data analysis to generate summary statistics and missing values, and then creates a PDF report of the analysis. The report will be saved with a unique filename if the file already exists.

Steps to Complete the Task:
Reading Data from CSV:

Implement a function read_data() that takes a file path to a CSV file and reads the data into a pandas DataFrame.
If the file contains encoding issues, handle them by trying to read the file with an alternative encoding (ISO-8859-1).
Return None if the file cannot be read.
Analyzing the Data:

Implement a function analyze_data() to perform basic data analysis:
Generate summary statistics for each column, including mean, count, and unique values using describe().
Identify and count the missing values in each column using isnull().sum().
Generating the PDF Report:

Create a function generate_pdf_report() that uses the FPDF library to generate a PDF report from the data analysis.
Include a title ("Data Analysis Report").
Add sections for column summaries and missing values.
Save the report to the specified output path.
If an error occurs during PDF creation, handle the exception and print an error message.
Ensuring Unique File Name:

Implement a function get_unique_output_filename() to check if a PDF file with the specified name already exists.
If it does, append an index (e.g., data_analysis_report_1.pdf) to create a unique filename.
Ensure that the file is saved without overwriting any existing files.
Testing the Script:

Run the script by providing a sample CSV file (sample_data.csv).
Ensure that the analysis (summary statistics and missing values) is correctly reflected in the generated PDF report.
Verify that the report is saved with a unique filename if it already exists.
Expected Deliverables:
A Python script that:

Reads data from a CSV file.
Performs data analysis (summary and missing values).
Generates a PDF report containing the analysis.
Saves the report with a unique filename if needed.
Example usage:

Input: CSV file (sample_data.csv).
Output: A PDF report (data_analysis_report.pdf or data_analysis_report_1.pdf if the first exists).
Example Output:
The generated PDF report will contain the following sections:

Title: "Data Analysis Report".
Column Summary: Summary statistics for each column in the CSV.
Missing Values: Number of missing values for each column.


**generated pdf output**

https://github.com/santosh-patil-hub/CODETECH-TASK_1/issues/4#issue-2781756376
