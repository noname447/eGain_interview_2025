import pandas as pd
from datetime import datetime


if __name__ == '__main__':
    # Load the Excel file
    file_path = r'C:\Users\yilin\Downloads\Website visitor IP address log file 1.xlsx'
    df = pd.read_excel(file_path, engine='openpyxl')

    # Data cleansing steps
    # Drop rows with missing values
    df.dropna(inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert timestamp to datetime format
    df['Date & Time (UTC)'] = pd.to_datetime(df['Date & Time (UTC)'], format="%d/%b/%Y:%H:%M:%S")

    # Split Page URL columns into multiple levels
    df_split = df['Page URL'].str.split('/', n = 6, expand=True)
    df_split.columns = ['URl Level 0', 'URl Level 1', 'URl Level 2', 'URl Level 3', 'URl Level 4', 'URl Level 5', 'URL Extras']
    df_split = df_split.drop(columns=['URl Level 0'])
    df = pd.concat([df, df_split], axis=1)

    # Delete some irrelevant columns to reduce the size of dateset
    df = df.drop(['Domain', 'Request Type', 'User Agent'], axis=1)

    # Output the cleaned data to CSV
    output_file = r'C:\Users\yilin\Downloads\cleansed weblogs.csv'
    df.to_csv(output_file, index=False)
    print(f"Cleaned data has been saved to {output_file}")


    # df_limited = df.head(1000)
    # output_file = r'C:\Users\yilin\Downloads\cleansed weblogs first 1000.csv'
    # df_limited.to_csv(output_file, index=False)
    # print(f"Cleaned data has been saved to {output_file}")


