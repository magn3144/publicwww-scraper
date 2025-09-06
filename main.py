from scrape_html import fetch_html_headless, scrape_pages
from extract_table import extract_table_to_csv
import pandas as pd


def combine_csvs(csv_paths, out_path):
    """
    Combine multiple CSV files into a single CSV file.
    Assumes all CSVs have the same header.
    """

    combined_df = pd.concat([pd.read_csv(p) for p in csv_paths], ignore_index=True)
    combined_df.to_csv(out_path, index=False)
    print(f"Combined {len(csv_paths)} CSVs into {out_path}, total rows: {len(combined_df)}")

def sort_com(combined_csv_path, out_path):
    """
    Filter rows in a combined CSV to only those where the 'Url' column contains '.com'.
    Saves the filtered rows to a new CSV file.
    """
    df = pd.read_csv(combined_csv_path)
    filtered_df = df[df['Url'].str.contains('.com', na=False)]
    filtered_df.to_csv(out_path, index=False)
    print(f"Saved {len(filtered_df)} rows containing .com to {out_path}")


# Scrape pages and extract tables
# login_publicwww(email, password)
base_url = "https://publicwww.com/websites/zsiqscript"
scrape_pages(base_url, 21, 100)
csv_files = [f"data/csv/page_{i}.csv" for i in range(1, 21)]
combine_csvs(csv_files, "data/data_combined.csv")
sort_com("data/data_combined.csv", "data/data_combined_sorted.csv")