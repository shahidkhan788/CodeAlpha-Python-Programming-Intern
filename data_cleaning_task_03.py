import pandas as pd

def clean_data(input_file, output_file):
    """
    Cleans the data in the input CSV file and writes the cleaned data to the output CSV file.
    
    Tasks performed:
      - Loads the CSV file into a DataFrame.
      - Removes duplicate rows.
      - Strips leading and trailing whitespace from string columns.
      - Fills missing values:
          - Numeric columns: using the median.
          - Categorical columns: using the mode.
      - Saves the cleaned DataFrame to a new CSV file.
    
    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path where the cleaned CSV file will be saved.
    """
    try:
        # Load the data
        df = pd.read_csv(input_file)
        print(f"Data loaded successfully with {len(df)} rows.")
        
        # Remove duplicate rows
        initial_count = len(df)
        df.drop_duplicates(inplace=True)
        print(f"Removed {initial_count - len(df)} duplicate rows.")

        # Trim whitespace from string columns
        str_cols = df.select_dtypes(include=['object']).columns
        for col in str_cols:
            df[col] = df[col].astype(str).str.strip()

        # Fill missing values for numeric columns with the median
        num_cols = df.select_dtypes(include=['int64', 'float64']).columns
        for col in num_cols:
            if df[col].isnull().sum() > 0:
                median_value = df[col].median()
                df[col].fillna(median_value, inplace=True)
                print(f"Filled missing values in numeric column '{col}' with median: {median_value}")

        # Fill missing values for object columns with the mode
        for col in str_cols:
            if df[col].isnull().sum() > 0:
                mode_value = df[col].mode()[0]
                df[col].fillna(mode_value, inplace=True)
                print(f"Filled missing values in categorical column '{col}' with mode: {mode_value}")

        # to fetch only file name of csv from the given path
        output_file = str(output_file).split("\\")
        output_file = output_file[-1]
        
        # Save the cleaned data to a new CSV file
        df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    input_csv = r"raw_data.csv"   # Replace with your input file path
    output_csv = r"cleaned_data.csv"  # Replace with your desired output file path
    clean_data(input_csv, output_csv)
