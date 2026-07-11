import pandas as pd
import os

class EmployeeAnalyzer:
    """A professional tool to handle employee data analysis."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        
    def load_data(self):
        """Loads and validates the CSV file."""
        if os.path.exists(self.file_path):
            self.df = pd.read_csv(self.file_path)
            print(f"Successfully loaded {self.file_path}")
        else:
            print("Error: File not found.")

    def get_summary_statistics(self):
        """Calculates average salary and department counts."""
        if self.df is not None:
            stats = {
                "avg_salary": self.df['salary'].mean(),
                "dept_counts": self.df['department'].value_counts().to_dict()
            }
            return stats
        return None

    def filter_and_export(self, salary_threshold, output_filename):
        """Filters high earners and saves to a new file."""
        if self.df is not None:
            filtered_df = self.df[self.df['salary'] > salary_threshold]
            filtered_df.to_csv(output_filename, index=False)
            print(f"Exported {len(filtered_df)} records to {output_filename}")

# --- Main Application Logic ---
def main():
    # 1. Initialize
    analyzer = EmployeeAnalyzer('employee_data.csv')
    
    # 2. Process
    analyzer.load_data()
    
    # 3. Analyze
    stats = analyzer.get_summary_statistics()
    if stats:
        print(f"--- Analysis Report ---")
        print(f"Average Salary: ${stats['avg_salary']:,.2f}")
        print(f"Department Breakdown: {stats['dept_counts']}")
    
    # 4. Automate Export
    analyzer.filter_and_export(salary_threshold=70000, output_filename='senior_staff.csv')

if __name__ == "__main__":
    main()