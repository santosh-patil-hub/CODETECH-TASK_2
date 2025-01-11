
import pandas as pd
import sys

try:
    from fpdf import FPDF
except ImportError:
    print("The 'fpdf' module is not installed. Please install it using 'pip install fpdf'.")
    sys.exit(1)

def read_data(file_path):
    """
    Reads data from a CSV file, handling potential encoding issues.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Dataframe containing the CSV data.
    """
    try:
        return pd.read_csv(file_path)
    except UnicodeDecodeError:
        print("UTF-8 decoding failed. Trying an alternative encoding (ISO-8859-1)...")
        try:
            return pd.read_csv(file_path, encoding='ISO-8859-1')
        except Exception as e:
            print(f"Error reading file '{file_path}' with fallback encoding: {e}")
            return None
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def analyze_data(data):
    """
    Analyzes the dataframe to generate a summary and missing values.

    Args:
        data (pd.DataFrame): Input dataframe.

    Returns:
        dict: Dictionary containing column summary and missing values.
    """
    return {
        "column_summary": data.describe(include='all').transpose(),
        "missing_values": data.isnull().sum(),
    }

def generate_pdf_report(analysis, output_file):
    """
    Generates a PDF report from the analysis data.

    Args:
        analysis (dict): Analysis dictionary containing summary and missing values.
        output_file (str): Path to save the PDF report.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, "Data Analysis Report", ln=True, align="C")
    pdf.ln(10)

    # Column Summary
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "Column Summary:", ln=True)
    pdf.set_font("Arial", size=12)
    for col, stats in analysis["column_summary"].iterrows():
        pdf.cell(0, 10, f"Column: {col}", ln=True)
        for stat_name, stat_value in stats.items():
            pdf.cell(0, 10, f"  {stat_name}: {stat_value}", ln=True)
        pdf.ln(5)

    # Missing Values
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "Missing Values:", ln=True)
    pdf.set_font("Arial", size=12)
    for col, missing in analysis["missing_values"].items():
        pdf.cell(0, 10, f"  {col}: {missing}", ln=True)

    try:
        pdf.output(output_file)
        print(f"Report saved successfully: {output_file}")
    except Exception as e:
        print(f"Failed to save PDF report: {e}")

if __name__ == "__main__":
    input_file = "sample_data.csv"  # Change to the correct file path
    output_file = "report/data_analysis_report.pdf"

    data = read_data(input_file)
    if data is not None:
        analysis = analyze_data(data)
        generate_pdf_report(analysis, output_file)
