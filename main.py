from scrape_html import fetch_html_headless
from extract_table import extract_table_to_csv
import pandas as pd


def scrape_pages(base_url, page_number_start, page_number_end):
    """
    Scrape a range of paginated URLs and extract table data to CSV files.
    For each page in the range, fetch HTML and save it, then extract the table and save as CSV.
    """
    for i in range(page_number_start, page_number_end):
        fetch_html_headless(f"{base_url}/{str(i)}", f"data/html/page_{i}.html")
        print(f"Saved page {i} to data/html/page_{i}.html")
        n_rows = extract_table_to_csv(f"data/html/page_{i}.html", f"data/csv/page_{i}.csv")
        print(f"Extracted {n_rows} rows to data/csv/page_{i}.csv")

def combine_csvs(csv_paths, out_path):
    """
    Combine multiple CSV files into a single CSV file.
    Assumes all CSVs have the same header.
    """

    combined_df = pd.concat([pd.read_csv(p) for p in csv_paths], ignore_index=True)
    combined_df.to_csv(out_path, index=False)
    print(f"Combined {len(csv_paths)} CSVs into {out_path}, total rows: {len(combined_df)}")


# Scrape pages and extract tables
base_url = "https://publicwww.com/websites/zsiqscript"
scrape_pages(base_url, 1, 21)
csv_files = [f"data/csv/page_{i}.csv" for i in range(1, 21)]
combine_csvs(csv_files, "data/data_combined.csv")